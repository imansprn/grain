# Component Scope

## When to Route to Component Flow

Most day-to-day requests are component-shaped, not page-shaped. Route to component flow when any of these fire:

1. The brief names a single UI element: button, input, card, modal, dropdown, tooltip, select, checkbox, switch, tab strip, chip, badge, banner, snackbar, popover, slider, date picker, avatar
2. The brief is short (≤ 30 words) and refers to one element
3. The user says "just the X", "only the Y", "this one element", "a single ___"
4. The target file is a single component (e.g., `Button.tsx`, `Input.css`)

If two signals fire, route component. If only page signals fire (multi-section brief, "build a landing page"), stay in page flow.

## What Component Scope Preserves

- **Identity** → Read existing identity. Component inherits from project identity. If no identity exists, define minimal identity (color, type, shape only).
- **Pre-flight scan** → Same. Read existing tokens, fonts, framework.
- **Token usage** → Must reference project tokens (`var(--color-accent)`), never inline values.

## What Component Scope Skips

- Macrostructure pick (components don't have page shapes)
- Navigation and footer archetypes
- Hero enrichment
- Section design
- Diversification tracking (no log entry for component runs)

## 8-State Checklist

Every interactive component MUST ship code for all 8 states:

| State | When | CSS |
|-------|------|-----|
| Default | Normal resting state | `.component` |
| Hover | Pointer over element | `.component:hover` |
| Focus-visible | Keyboard focus | `.component:focus-visible` |
| Active | Pressed / clicking | `.component:active` |
| Disabled | Not interactable | `.component:disabled` |
| Loading | Processing action | `.component[data-state="loading"]` |
| Error | Failed validation/action | `.component[data-state="error"]` |
| Success | Completed action | `.component[data-state="success"]` |

Each state must have distinct visual styling — not just presence. A disabled button must look disabled (reduced opacity, no pointer), not just have the attribute.

Non-interactive components (avatars, badges, chips) skip the full 8, but must handle: default, hover (if clickable), and disabled (if actionable).

## Two-File Output

**File 1**: The component artifact matching project conventions
- React/Vue/Svelte: `Button.tsx`/`Button.vue`/`Button.svelte`
- Vanilla: `button.css` + `button.html`
- Consumes tokens by name, never inlines values

**File 2**: 8-state demo wrapper — `<name>.preview.html`
- Renders all 8 states stacked vertically, each labelled
- Uses `.is-hover`, `.is-focus`, `.is-active` CSS classes to force pseudo-class styling
- User opens once, verifies, then deletes the preview file

Example state-forcing pattern:
```css
.btn:hover, .btn.is-hover { background: var(--color-hover); }
.btn:focus-visible, .btn.is-focus { outline: 2px solid var(--color-focus); }
.btn:active, .btn.is-active { transform: translateY(1px); }
```

## Output Stamp

```css
/* component: <type> · states: default · hover · focus · active · disabled · loading · error · success */
```

The `states:` line is a checklist — every state listed must have actual styling.
