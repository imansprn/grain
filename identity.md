# Design Identity

A design identity is a set of constraints chosen deliberately. Replit looks like Replit because it has hard rules — orange/black palette, monospace type, terminal aesthetic, no gradients. These constraints prevent generic output by making certain slop patterns mechanically impossible.

**Rule:** Define identity before any screen sketch. Every screen is derived from identity. If a screen doesn't look like it belongs, it's wrong.

---

## 1. Color

### Define

| Role | Count | Example |
|------|-------|---------|
| Primary | 1-2 hues | Blue (#2563eb) + Indigo (#4f46e5) |
| Neutral | 2-3 values | White (#fff), Grey-50 (#f8f9fa), Grey-900 (#111) |
| Accent | 0-1 | Amber (#f59e0b) — use sparingly |
| Semantic | 3 max | Green (success), Red (error), Yellow (warning) |

### Banned

- Rainbow palettes (every section different color)
- Unmotivated gradients
- Multiple accent colors competing
- Pure black on pure white (#000 on #fff — too harsh)
- Chart colors that don't match the palette

### How It Prevents Slop

A 2-color palette cannot produce the rainbow-card-grid pattern. A neutral-only palette with one accent cannot produce the gradient-hero pattern.

---

## 2. Typography

### Define

| Property | Constraint | Example |
|----------|------------|---------|
| Families | 1-2 max | Inter (UI) + JetBrains Mono (code) |
| Scale | 4-6 sizes max | 12 / 14 / 16 / 20 / 24 / 32 |
| Weights | 2-3 max | 400 / 500 / 600 |
| Line height | Fixed range | 1.4 (body) / 1.1 (headings) |

### Banned

- System font stack as identity (no choice made)
- More than 2 font families
- Display fonts for body text
- Light weights on light backgrounds (below 400 on white)

### How It Prevents Slop

2 families with 6 sizes and 3 weights cannot produce the 10-style typography chaos of a generic template.

---

## 3. Density

### Define

| Density | Spacing Unit | Use Case |
|---------|--------------|----------|
| Spacious | 24-32px base | Content-heavy, reading, landing pages |
| Moderate | 16-20px base | Most apps — balanced information + whitespace |
| Compact | 8-12px base | Data-dense — dashboards, tables, monitoring |

### Banned

- Mixed density without reason (spacious hero then compact form)
- Inconsistent padding within same screen type
- No spacing system (pixel values chosen per-element)

### How It Prevents Slop

A density rule eliminates the "everything floating with too much space" or "everything cramped" problems. It forces consistency.

---

## 4. Shape

### Define

| Radius | Value | Feel |
|--------|-------|------|
| None | 0px | Sharp, technical, industrial |
| Subtle | 4-6px | Neutral, professional |
| Rounded | 8-12px | Friendly, consumer |

Pick one. Apply everywhere. No mixing unless there's a semantic reason.

### Banned

- 16px+ radius on enterprise/technical products
- Different radius on cards vs inputs vs buttons without reason
- Fully circular elements without purpose (avatar OK, card NO)

### How It Prevents Slop

A single radius rule eliminates the randomized-corner look of template UI.

---

## 5. Tone

### Define

3-5 words that describe the feeling. 3-5 words that describe what it is NOT.

| Identity | Is | Is Not |
|----------|----|--------|
| Replit | Technical, playful, dense | Corporate, spacious, decorative |
| Linear | Fast, minimal, precise | Friendly, colorful, explanatory |
| Stripe | Professional, trustworthy, clean | Playful, dense, experimental |

### How It Prevents Slop

Tone rules make the agent reject stock illustrations (not "technical"), gradients (not "minimal"), large illustrations (not "dense").

---

## 6. Layout Patterns

### Define

List the layout patterns this identity uses. List the layout patterns it explicitly rejects.

| Identity | Uses | Rejects |
|----------|------|---------|
| Terminal/developer tool | Sidebar-nav, dense tables, monospace grids | Hero-image, card-grid, image-text alternating |
| Consumer SaaS | Centered navigation, spacious cards, illustrations | Terminal-dense, data tables as primary UI |
| Data/analytics | Full-width tables, compact headers, sticky controls | Hero sections, decorative illustrations |

### How It Prevents Slop

Layout rules prevent the alternating image-text grid by making it an explicit reject. The agent cannot fall into the template pattern because the identity forbids it.

---

## 7. Motion

### Define

| Level | What Moves | Duration |
|-------|------------|----------|
| Still | Nothing | 0ms |
| Subtle | Transitions only (page, modal, hover) | 150-200ms |
| Expressive | Micro-interactions, loading, scroll-triggered | 200-500ms |

### Banned

- Motion that doesn't serve a purpose
- Decorative parallax on enterprise apps
- Animation that delays task completion
- Inconsistent easing (ease-in-out everywhere vs spring proper)

---

## 8. Hard Constraints

Write 3-5 explicit rules that start with "We never...".

Examples:
- We never use circular icons inside colored backgrounds for features
- We never use gradients
- We never use stock photography of people
- We never use rounded cards on technical screens
- We never put illustrations in the hero section

These are the most powerful anti-slop tool. They are mechanically checkable. A screen either violates a constraint or it doesn't.

---

---

## Platform Adaptation

The same 8 identity dimensions apply across platforms, but some values map differently:

### Density

| Platform | Typical Range | Example |
|----------|--------------|---------|
| Web (enterprise/SaaS) | Compact to moderate | CRM, analytics, admin panels |
| Web (marketing/content) | Spacious | Landing pages, editorial, e-commerce |
| Mobile (iOS) | Moderate to spacious | Banking, fitness, shopping — touch targets demand room |
| Desktop (thick client / power user) | Compact | Trading, IDE, monitoring — dense data per screen |

### Shape

| Platform | Typical Range | Why |
|----------|--------------|-----|
| Web / Desktop | 0-6px | Professional, technical. Higher radii feel consumer. |
| Mobile | 8-16px | Rounded feels native on mobile. 0px on mobile feels industrial. |

### Motion

| Platform | Typical Range | Why |
|----------|--------------|-----|
| Web (desktop-first) | Still to subtle | Users expect instant response. Decorative motion on desktop is noise. |
| Mobile | Subtle to expressive | Native apps use transitions for wayfinding. Sheets, cards, tab switches benefit from motion. |

### Layout Patterns Per Platform

| Platform | Typical Patterns | Avoid |
|----------|-----------------|-------|
| Web | Multi-column, side panels, slide-overs, tables | Gesture-driven navigation, bottom sheets as primary layout |
| Mobile | Bottom nav, stacked screens, modal sheets, cards | Multi-column layouts, right-click menus, hover-dependent UIs |
| Desktop | Fixed multi-panel, floating panels, context menus, keyboard shortcuts | Mobile navigation patterns (hamburger menus, swipe gestures as primary) |

### Example Identity Values Per Platform

Compare how the same identity dimension is set differently:

```yaml
# Web CRM (compact, 4px, subtle)
density: compact
shape: 4px
motion: subtle

# Desktop trading (compact, 0px, still)
density: compact
shape: 0px
motion: still

# Mobile banking (spacious, 8px, subtle)
density: spacious
shape: 8px
motion: subtle

# Mobile fitness (moderate, 12px, expressive)
density: moderate
shape: 12px
motion: expressive
```

The identity stays the same shape across platforms — a mobile banking app and its web admin should share palette, type, tone, and constraints. Only density, shape, motion, and layout patterns adapt per platform.

---

## Identity Template

```yaml
identity:
  name: <product name>
  color:
    primary: ["#hex1", "#hex2"]
    neutral: ["#hex1", "#hex2", "#hex3"]
    accent: "#hex"
    banned: ["list of patterns"]
  typography:
    families: ["Font1", "Font2"]
    scale: [12, 14, 16, 20, 24]
    weights: [400, 500, 600]
    banned: ["list"]
  density: spacious | moderate | compact
  shape:
    radius: "0px | 4px | 8px"
    banned: ["list"]
  tone:
    is: ["word1", "word2", "word3"]
    is_not: ["word1", "word2", "word3"]
  layout:
    uses: ["pattern1", "pattern2"]
    rejects: ["pattern1", "pattern2"]
  motion: still | subtle | expressive
  hard_constraints:
    - "We never ..."
    - "We never ..."
    - "We never ..."
  dials:
    variance: 5      # 1-10
    motion: 2        # 1-10
    density: 7       # 1-10
```

---

## 9. Three Dials (Quantified Identity)

After defining the 8 identity dimensions, set three numeric dials. Every layout, motion, and density decision is gated by these. They translate identity into measurable output targets.

| Dial | Range | Meaning |
|------|-------|---------|
| `DESIGN_VARIANCE` | 1–10 | 1 = symmetric grid, equal padding, centered. 10 = asymmetric columns, massive white-space zones, irregular rhythm |
| `MOTION_INTENSITY` | 1–10 | 1 = static, hover/active only. 10 = scroll-pinned reveals, physics-based micro-interactions, animated state transitions |
| `VISUAL_DENSITY` | 1–10 | 1 = art-gallery spacing. 10 = cockpit — every pixel earns its place, monospace numbers, hairline dividers |

**Defaults:** `VARIANCE: 5 / MOTION: 2 / DENSITY: 7` for product UI (dashboards, admin, SaaS apps).

### Dial Inference by Brief

| Signal | VARIANCE | MOTION | DENSITY |
|--------|----------|--------|---------|
| Developer / CLI tool | 3–4 | 1–2 | 8–9 |
| Analytics / monitoring dashboard | 4–5 | 2–3 | 8–10 |
| CRM / admin panel | 5–6 | 2–3 | 6–8 |
| Consumer SaaS (B2C) | 6–7 | 4–5 | 4–5 |
| Marketing / landing page | 7–9 | 5–7 | 3–4 |
| Mobile banking / fintech | 4–5 | 3–4 | 5–6 |
| Mobile fitness / consumer health | 6–7 | 5–7 | 4–5 |

### How Dials Constrain Output

| Dial | Low → | High → |
|------|-------|--------|
| VARIANCE < 4 | Symmetric grid, consistent paddings | — |
| VARIANCE > 7 | — | Asymmetric columns, mixed rhythm |
| MOTION < 3 | No scroll animation, transitions ≤ 150ms | — |
| MOTION > 5 | — | Scroll-triggered reveals, animated empty states |
| DENSITY > 7 | — | Compact spacing (8–12px base), no card wrappers, hairline dividers |
| DENSITY < 4 | — | Spacious sections, cards OK, large whitespace |

State dials at the top of your design output: `/* Dials: V5 M2 D8 */`
