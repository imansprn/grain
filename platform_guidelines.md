# Platform Guidelines

Non-obvious rules only. Standard platform knowledge (touch targets, keyboard nav, ARIA) is in `checks/accessibility.md`.

## Motion by Platform

| Platform | Range | Hard rule |
|----------|-------|-----------|
| Web product UI | M: 1–3 | No decorative parallax. Transitions on state change only. |
| Web marketing | M: 4–7 | Scroll-reveals OK. `prefers-reduced-motion` required. |
| Mobile (iOS/Android) | M: 3–6 | Sheet/card transitions are expected by platform. Spring physics feel native. |
| Desktop thick client | M: 1–2 | Instant response required. Any animation delay feels broken. |

**Universal:** Animate `transform` and `opacity` only. Never `width`, `height`, `top`, `left`. Use `IntersectionObserver` or CSS `animation-timeline: view()` — never `window.addEventListener('scroll', ...)` for animation.

## Layout Mechanics (Web — easy to get wrong)

- `min-h-[100dvh]` not `h-screen` — iOS Safari address bar causes layout jump with `h-screen`
- CSS Grid for multi-column, not `width: calc(33% - 1rem)` flexbox math
- Z-index: define a project scale (nav: 10, sticky: 20, modal: 50, toast: 100). Never `z-[9999]`

## Density by Platform

| Platform | Typical dial | Why it differs |
|----------|-------------|---------------|
| Web enterprise/SaaS | D: 6–9 | Mouse precision allows compact UI. Data density is a feature. |
| Web marketing/landing | D: 2–4 | Reading pace is slow. Whitespace aids comprehension. |
| Mobile | D: 4–6 | Touch targets force minimum spacing. Compact is painful to tap. |
| Desktop thick client | D: 8–10 | Power users maximize visible data. Animation and spacing feel wasteful. |

## Platform-Specific Identity Adaptation

The 8 identity dimensions apply across platforms. Only these four adapt per platform — palette and tone do not change:

| Dimension | Web | Mobile | Desktop |
|-----------|-----|--------|---------|
| Shape/radius | 0–6px | 8–16px | 0–4px |
| Density | varies | moderate–spacious | compact |
| Motion | still–subtle | subtle–expressive | still |
| Layout | multi-column, side panels | bottom nav, stacked screens | fixed multi-panel, context menus |
