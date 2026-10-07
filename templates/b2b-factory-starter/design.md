# DESIGN.md · Xinghui Plastic Life Design System

> Reverse-engineered design specification and visual token inventory extracted directly from `https://www.xhplasticlife.com/`.
> Methodology based on `website-to-design-md` and `pixel-perfect-reference-ui`.

---

## 1. Visual Language & Color Palette

The visual identity embodies modern industrial B2B minimalism tailored for international buyers: high-contrast typography, restrained earthy tones, and generous white space that project credibility, compliance, and OEM manufacturing capability.

### 1.1 Color Tokens
| Token Name | Hex Value | Purpose / Usage |
| :--- | :--- | :--- |
| `--color-accent-strong` | `#516b4b` | Primary brand accent, primary CTA buttons, hero highlights, active states |
| `--color-accent` | `#8da687` | Secondary brand tint, hover states, badges, decorative borders |
| `--color-sunken` | `#e9e9d2` | Warm oatmeal sand, Trust Bridge background, subtle callout cards |
| `--color-sand` | `#dddab3` | Soft golden sand, tag highlights |
| `--color-tint` | `#eef2ee` | Light sage tint, section alternating backgrounds |
| `--color-light` | `#f7f7f7` | Off-white neutral background for feature grids |
| `--color-white` | `#ffffff` | Pure white surface, cards, inputs |
| `--color-fg` | `#1a1a1a` | High-contrast dark charcoal for primary text, H1-H6 |
| `--color-fg-muted` | `#546154` | Muted olive-gray for secondary text, descriptions, footnotes |
| `--color-border` | `#d8e0d8` | Subtle border for product cards, tables, inputs |
| `--color-overlay-dark` | `rgba(26, 26, 26, 0.62)` | Hero media dark scrim overlay |

### 1.2 Surface Layering Architecture
- `.surface-media`: Dark background / image hero with high-contrast white text (`--color-fg: #fff`).
- `.surface-sunken`: Warm oatmeal sand background (`#e9e9d2`) for high-trust value propositions.
- `.surface-tint`: Subtle pale green tint (`#eef2ee`) for process flow and workflow steps.
- `.surface-light`: Cool light gray (`#f7f7f7`) for factory capabilities and e-commerce services.
- `.surface-white`: Clean white backdrop (`#ffffff`) for product catalogs and inquiry closer forms.

---

## 2. Typography System

The pairing combines an editorial serif display for authoritative headings with a hyper-legible sans-serif stack for dense B2B product specifications.

### 2.1 Font Families
- **Display Font (`--font-display`)**: `"DM Serif Display", Georgia, "Times New Roman", serif`
  - Used for: Hero H1, Section H2 titles, category highlight banners.
  - Characteristics: High contrast, classical luxury, authoritative manufacturing presence.
- **Body Font (`--font-sans`)**: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
  - Used for: Nav items, body text, product specs, RFQ labels, FAQ answers.
- **Monospace Font (`--font-mono`)**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace`
  - Used for: SKU model codes (`BX1051`), container dimensions, HS codes, capacities.

### 2.2 Typographic Hierarchy
- **Hero H1**: `clamp(2.25rem, 5vw, 3.5rem)` / line-height `1.15` / font-weight `400` (Serif Display)
- **Section H2**: `clamp(1.75rem, 3.5vw, 2.5rem)` / line-height `1.25` / font-weight `400` (Serif Display)
- **Card H3**: `1.25rem ~ 1.5rem` / line-height `1.35` / font-weight `600`
- **Sub-card H4 / Feature title**: `1.05rem ~ 1.15rem` / line-height `1.4` / font-weight `600`
- **Eyebrow Tag**: `0.8125rem (13px)` / uppercase / letter-spacing `0.08em` / font-weight `600`
- **Body Regular**: `1rem (16px)` / line-height `1.6` / font-weight `400`
- **Body Small / Specs**: `0.875rem (14px)` / line-height `1.5` / font-weight `400`

---

## 3. Spacing, Layout & Grid Constraints

### 3.1 Breakpoints
- **Mobile**: `< 768px` (single column, full-width inputs, collapsible drawer menu)
- **Tablet**: `768px ~ 1024px` (2-column grids, condensed navbar)
- **Desktop**: `> 1024px` (3/4-column product grids, horizontal header with full multi-language dropdown)
- **Max Width Container (`.section-shell`, `.page-container`)**: `1280px` centered with `padding: 0 1.5rem` (mobile) to `0 2.5rem` (desktop).

### 3.2 Spacing Scale
- Section vertical padding: `5rem (80px)` desktop, `3.5rem (56px)` mobile.
- Card padding: `1.5rem ~ 2rem`.
- Gap in product grids: `1.75rem (28px)`.
- Gap in trust bridge: `1.5rem (24px)`.

---

## 4. Components & Interaction Patterns

1. **Top Utility Bar & Sticky Header**:
   - Social links (YouTube, Facebook, TikTok), Brand Logo, Primary Nav, Multilingual Switcher (EN, JA, RU, DE, FR, ES, KO), and prominent "Get a Quote" pill button.
2. **Trust Bridge (4-Column Bento Ribbon)**:
   - Sunken sand background (`#e9e9d2`), 4 core manufacturer guarantees with clean line dividers.
3. **Product Family Showcase (6 Cards)**:
   - High-resolution product photography with hover zoom effect (`transform: scale(1.03)`), category titles, and arrow indicator.
4. **Catalogue 63-SKU Filter Engine**:
   - Instant search input + category tab pills + live count (`63 products shown`) + responsive 3-column grid.
5. **Interactive FAQ Accordion**:
   - Clean `<details>` and `<summary>` styling with smooth rotation chevron, answering the top 3 B2B procurement queries.
6. **B2B RFQ Lead Magnet & Form**:
   - Model selection, target quantity, customization scope (Logo / Packaging / Tooling), destination country, email, phone / WhatsApp.
