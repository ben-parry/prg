# PRG Membership Page — Build Spec

## What This Is

A single-page static site for the Paradigms Research Group (PRG), a weekly reading group in Toronto. The page presents two membership tiers and links to Stripe Payment Links for checkout. The URL gets shared in a WhatsApp group chat.

## Requirements

- **Single HTML file** (inline CSS, no build step)
- **Static hosting** — GitHub Pages, Cloudflare Pages, or Vercel
- **Mobile-first** — most people open this from WhatsApp on their phone
- **Two Stripe Payment Link buttons** — placeholder URLs for now (`STRIPE_MEMBER_LINK` and `STRIPE_SUPPORTER_LINK`)
- **No framework dependencies**

## Copy

Keep it tight. The goal is: understand what this is, see the two options, pay. Nothing else.

### Header

**The Paradigms Research Group**
Season 1: Religion and Work — April to June 2026

### About (3-4 sentences max)

Every Wednesday in Toronto we read seminal papers together in silence, then hold a careful discussion. We've read close to 40 papers over the past year — from Alan Turing to Hannah Arendt to Charles Taylor.

This season we're investigating the relationship between religion and work. What are our current ideas about work? Do they have anything to do with religion? Can we treat our work religiously? Should we?

### Membership Details

**What you get:**
- Access to the full season reading list
- A high quality printed ticket 
- Added to the season's WhatsApp group
- Printed papers each session
- Access to the end-of-season party (+1 included)
- Invite anyone you want to any session

Your first session is always free. After that, membership is required. You can join mid-season but dues aren't pro-rated.

**Wednesdays, 6–9 PM, Toronto.** Other details will be shared in the WhatsApp group.

### The Two Tiers

**Season Membership — $30**
Covers printing, space, and logistics for 13 sessions. Less than $2.50 per week.

**Supporter — $400**
Everything above, plus you're helping us invest in and grow PRG.

### Footer

A project by Ben and Michelle. If you have any questions don't hesitate to reach out to us.

---

## Design Direction

### Mood

An independent journal or a William Morris–era arts society. Warm, serious, handmade-feeling. Not a startup. Not a university department. Something closer to a printed broadsheet or a Kelmscott Press colophon page.

### Inspiration

Take some inspiration from the image also in the prg folder

### Color Palette

Warm and earthy. Muted, nothing bright.

- **Background**: A warm off-white / parchment. Something like `#F5F0E8` or `#EDE8DF`.
- **Text**: Deep warm brown or charcoal, not pure black. Something like `#2C2418` or `#3B3228`.
- **Accent / buttons**: A muted terracotta, deep olive, or brick red. Something like `#8B5E3C` (terracotta) or `#5C6B4F` (olive).
- **Card backgrounds**: Slightly lighter or slightly darker than the page background. Subtle contrast, not stark.

### Typography

- **Headings**: A classic serif. Use Google Fonts — something like **Playfair Display**, **Cormorant Garamond**, or **EB Garamond**.
- **Body**: A clean readable serif or a restrained sans-serif. **Source Serif Pro** or **Inter** at comfortable size (17-18px).
- Keep type sizes restrained. The page should feel quiet, not loud.

### Layout

- Boxy and minimal. Clean rectangles. No rounded corners or only very slight ones (2-3px max).
- Generous whitespace. Let things breathe.
- Tier cards side-by-side on desktop, stacked on mobile. Simple bordered boxes — think ruled lines, not drop shadows.
- A thin border or rule line as a visual device (like a printed page).

### William Morris Background Pattern

This is the key design detail. Use a **muted, semi-transparent William Morris–style pattern** as a subtle background texture.

**Approach: Inline SVG pattern**
- Create an SVG vine/leaf motif inspired by Morris's designs (Willow Bough, Acorn, etc.)
- Embed it directly in the HTML as an inline SVG pattern — no external image dependency, keeps the single-file constraint clean.
- Apply as a `background-image` via data URI on a `body::before` pseudo-element.
- Very low opacity (`0.04` to `0.07`) — barely visible, like a watermark on old paper. "Texture of the paper" not "wallpaper."
- `background-repeat: repeat`, `background-size` around 400–600px.
- `pointer-events: none; z-index: -1` so it never interferes with content.

If we later want to swap in a raster image (e.g. a high-res scan from the V&A or rawpixel), we can base64-encode it and drop it into the same data URI slot.

### Decorative Flourishes (from inspiration image)

Bring in some devices from the inspiration image to reinforce the broadsheet / printed-treatise feel:
- **Ornamental border band** — a decorative rule or repeating ornament strip as a visual divider (e.g. between header and body, or framing the content area).
- **Drop cap** — on the first letter of the About section, styled as a large decorative initial.
- Keep these restrained — they should feel like considered typographic choices, not decoration for its own sake.

### Buttons

- Solid fill with the accent color, no gradients.
- Text in the off-white/parchment color.
- Subtle hover state — slightly darker, or a thin border appears. Keep it restrained.
- Full-width on mobile, constrained width on desktop.

### Overall Feel

Imagine someone printed this page on heavy cream stock with a letterpress. It should feel like that — warm, considered, slightly old-fashioned in the best way. The kind of thing you'd pin to a wall.

---

## Stripe Integration

No Stripe SDK. Just two `<a>` tags pointing to Stripe Payment Links.

Placeholder URLs in the code:
```
https://STRIPE_MEMBER_LINK
https://STRIPE_SUPPORTER_LINK
```

Leave an HTML comment noting where to swap these.

## Deployment

- Single `index.html` file (with the Morris pattern as inline SVG)
- No build step, no external dependencies beyond Google Fonts
- Works when opened as a local file for previewing

## What Success Looks Like

Someone taps the link in WhatsApp on their phone. It loads fast. They get it in 15 seconds. Two taps to pay. The page feels like it was made by people who read Simone Weil for fun — because it was.
