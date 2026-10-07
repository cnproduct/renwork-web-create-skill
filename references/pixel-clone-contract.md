# Pixel Clone Contract · Business Truth & Visual Fidelity Rules

> Derived from `PixelClone-Skill` and `claude-skill-web-clone`.
> The uncompromising ironclad rules for reverse engineering websites.

---

## 1. The Core Philosophy
- **Reference Site is the Visual Truth**: Respect the original layout, aspect ratios, typography weight, and color transitions.
- **Application is the Business Truth**: Real user interactions cannot be simulated with dummy images. Forms must submit, filters must filter, tabs must toggle, and links must resolve.

## 2. Hard Boundaries (Never Violate)
1. **Never Screenshot Interactive Elements**: Search bars, filters, dropdowns, and buttons must be real HTML inputs, never static raster graphics.
2. **Never Fabricate Unverified Code**: If an AI hallucination invents complex 500-line shaders when the target simply uses CSS flexbox and clean SVGs, always favor the true source implementation.
3. **Preserve Business Fields**: In B2B inquiry forms, never drop critical fields like Destination Country, Order Volume, or Customization Type.
4. **Responsive Integrity**: Test across 375px (iPhone), 768px (iPad portrait), 1024px (iPad landscape/laptop), and 1440px (Desktop). Prevent horizontal scroll bars caused by unconstrained wide tables.
