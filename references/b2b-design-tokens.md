# B2B Design Tokens & Industrial UI Playbook

> Example only: derive the target palette, fonts, surfaces and layout from observed evidence and its own brand; do not force this olive theme.

> A systematic guide to engineering authoritative, high-conversion visual design systems for B2B export manufacturers.

---

## 1. Visual Psychology for Overseas Buyers
Enterprise procurement officers, supermarket category managers, and Amazon brand aggregators do not evaluate websites like retail consumers. They look for:
- **Manufacturing Legitimacy**: Factory footprints, injection machines, ISO/BSCI certifications.
- **Clarity Over Flashiness**: Clear typography, high data density, structured parameter tables.
- **Earthy, Restrained Palettes**: Olive greens, deep navy, warm oatmeal, and cool slate gray communicate environmental compliance (BPA-free, LFGB) and reliability.

## 2. Standard Token Architecture
```css
:root {
  /* Brand Accents */
  --color-accent-strong: #516b4b; /* Deep Olive - Primary CTA, Hero Accents */
  --color-accent: #8da687;        /* Sage Green - Badges, Subtle Borders */
  
  /* Neutral Surfaces */
  --color-sunken: #e9e9d2;        /* Warm Sand - Trust ribbons */
  --color-tint: #eef2ee;          /* Pale Mint - Alternating section background */
  --color-light: #f7f7f7;         /* Cool Light Gray - Spec tables */
  --color-white: #ffffff;         /* Pure White - Cards, inputs */
  
  /* Contrast Typography */
  --color-fg: #1a1a1a;            /* Charcoal Black - Headings and primary text */
  --color-fg-muted: #546154;      /* Olive Gray - Descriptions and specs */
  
  /* Font Families */
  --font-display: "DM Serif Display", Georgia, serif;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}
```

## 3. Surface Layering Protocol
1. **`.surface-media`**: Dark overlay container. Requires white typography (`--color-fg: #fff`), high contrast badges.
2. **`.surface-sunken`**: Warm oatmeal background (`#e9e9d2`). Dedicated to Trust Bridge value propositions.
3. **`.surface-white`**: Crisp white backdrop. Reserved for product catalogs, SKU matrices, and lead forms.
4. **`.surface-tint`**: Gentle sage tint (`#eef2ee`). Ideal for workflow timelines and process steps.
