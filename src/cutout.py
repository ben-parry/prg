import numpy as np, cv2, sys, json
from scipy import ndimage as ndi
from skimage import color, morphology
from PIL import Image

SRC = "_mss/"  # downloaded Commons thumbnails
OUT = "marginalia-cut/"

def cut(name, src, box, t0=9, t1=22, min_area=60, fill=True, erase=()):
    im = Image.open(SRC + src).convert("RGB").crop(box)
    a = np.asarray(im).astype(np.float32) / 255
    lab = color.rgb2lab(a)
    L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    chroma = np.hypot(A, B)
    # candidate background: light and fairly neutral parchment
    cand = (L > np.percentile(L, 40)) & (chroma < np.percentile(chroma, 60))
    w = cand.astype(np.float32)
    sig = max(a.shape[:2]) / 10
    bg = np.stack([ndi.gaussian_filter(lab[..., i] * w, sig) / (ndi.gaussian_filter(w, sig) + 1e-6) for i in range(3)], -1)
    dE = np.sqrt(((lab - bg) ** 2).sum(-1))
    alpha = np.clip((dE - t0) / (t1 - t0), 0, 1)
    mask = alpha > 0.5
    mask = morphology.remove_small_objects(mask, min_area)
    if fill:
        closed = morphology.closing(mask, morphology.disk(2))
        filled = ndi.binary_fill_holes(closed)
        filled = morphology.remove_small_objects(filled, min_area * 3)
        alpha = np.maximum(alpha * filled, ndi.gaussian_filter(morphology.erosion(filled, morphology.disk(1)).astype(np.float32), 0.8))
    else:
        alpha = alpha * ndi.binary_dilation(mask, iterations=2)
    for (x0, y0, x1, y1) in erase:
        alpha[y0:y1, x0:x1] = 0
    alpha = np.clip(ndi.gaussian_filter(alpha, 0.6), 0, 1)
    # trim to content
    ys, xs = np.where(alpha > 0.05)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    rgba = np.dstack([np.asarray(im)[y0:y1, x0:x1], (alpha[y0:y1, x0:x1] * 255).astype(np.uint8)])
    Image.fromarray(rgba, "RGBA").save(OUT + name + ".png")
    return rgba.shape[1], rgba.shape[0]

JOBS = json.load(open(sys.argv[1]))
for j in JOBS:
    print(j["name"], cut(**j))
