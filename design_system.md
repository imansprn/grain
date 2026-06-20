# Design System Map

Before picking colors, typefaces, or layout patterns — pick the right foundation. Do not invent CSS for things that have an official package. Do not pretend an aesthetic trend is an official system.

**Rule:** If the brief matches a known system, install and use the official package. One system per project. Do not mix systems.

---

## When to Reach for a Real Design System

| Brief reads as… | Reach for | Why |
|---|---|---|
| Microsoft / enterprise SaaS / Office-adjacent | `@fluentui/react-components` | Official Fluent UI v9, Microsoft design tokens, accessible by default |
| Google-ish UI / Material-flavored product | `@material/web` + Material 3 tokens | Official web implementation, theme-able |
| IBM-style B2B / enterprise analytics | `@carbon/react` + `@carbon/styles` | Mature, highest data-density patterns in any public DS |
| Shopify app surfaces | Polaris React / Polaris web components | Required for Shopify admin UI, tokens baked in |
| Atlassian / Jira-adjacent product | `@atlaskit/*` + `@atlaskit/tokens` | Official Atlassian DS, battle-tested in dense product UI |
| GitHub-style devtool / community page | `@primer/css` or `@primer/react-brand` | Official Primer; Brand variant for marketing surfaces |
| Public-sector UK service | `govuk-frontend` | Legally expected; accessibility to WCAG 2.2 AA |
| US public-sector / trust-first service | `uswds` | Same; federal accessibility standard |
| Modern React SaaS where you own the components | `shadcn/ui` (`npx shadcn@latest add ...`) | You own the code — easy to customise. Never ship in default state |
| Fast MVP / agency project | Bootstrap 5.3 | Boring, fast, works |
| Modern accessible React foundation | `@radix-ui/themes` | Primitives + polished theme |

### Hard Rules

- **One system per project.** Never mix Fluent with Carbon in the same tree. Never import shadcn/ui components into a Material 3 app.
- **If you install a system, use its tokens.** Don't import a system and then override 90% of its values with custom CSS. At that point you're not using the system, you're fighting it.
- **shadcn/ui always needs customization.** If a shadcn component looks like the default shadcn component, it failed the identity check. Adjust radius, color, shadow, and typography to the project identity before shipping.

---

## When the Brief Is an Aesthetic, Not a System

Some directions have no single official package. Build with native CSS + Tailwind + a maintained component library.

| Aesthetic | Honest implementation |
|---|---|
| Glassmorphism / frosted glass | `backdrop-filter: blur()`, layered borders, highlight overlays. Provide solid fallback for `prefers-reduced-transparency`. |
| Bento grid | CSS Grid with mixed cell sizes. No library owns this. |
| Brutalism | Native CSS, monospace, raw borders. No library. |
| Terminal / developer | Monospace type, compact density, `bg-black` or deep-grey base. No library. |
| Dark tech | Mono + neon accent, terminal motifs. No library. |

---

## Domain → System Suggestions

| Domain | Typical System | Notes |
|--------|---------------|-------|
| Developer / CLI tool | Primer or custom terminal identity | Primer is GitHub-native and feels right for devtools |
| Analytics / monitoring | Carbon or custom compact DS | Carbon has the best data-density patterns |
| Enterprise B2B SaaS | Fluent, Carbon, or shadcn/ui customized | Match the org's existing stack |
| Consumer mobile app | No system — platform HIG | iOS: follow Apple HIG. Android: follow Material 3 |
| Admin panel / backoffice | shadcn/ui customized, or Carbon | shadcn is fast to ship; Carbon if data-density is extreme |
| E-commerce | Custom identity over Radix primitives | No major DS owns this space well |
| Fintech / banking | Custom identity, USWDS patterns for trust cues | Trust and accessibility are the primary constraints |

---

## Identity ↔ Design System Handshake

When an official system is installed, the identity framework still applies — but the source of truth for tokens shifts from your own definitions to the system's documented values. This creates a layered resolution order:

```
Design System tokens  (base layer — spacing, color roles, type scale)
    ↓
Identity overrides    (theme layer — brand accent, surface tone, radius direction)
    ↓
Component decisions   (instance layer — density, motion, state styling)
```

### What the identity controls vs. what the system controls

| Dimension | System controls | Identity overrides |
|-----------|----------------|-------------------|
| Spacing scale | Yes — use system's scale. Do not introduce new steps. | Density dial adjusts which steps you use (compact = smaller steps). |
| Color roles | Yes — system defines surface, on-surface, container roles. | Identity supplies the brand hue mapped to primary/accent tokens. |
| Type scale | Yes — system's type ramp. | Identity chooses the display typeface if allowed; body follows system. |
| Shape / radius | Often configurable via system token. | Identity direction (sharp vs. rounded) realized by setting system's shape token, not by overriding individual components. |
| Motion | System provides timing tokens. | Motion dial governs which transitions to use and at what intensity — do not add animations beyond what the system's tokens support. |
| Component states | System defines them — use them as-is. | Do not re-implement hover/focus/disabled styling. Override only when brand requires a specific treatment and the system exposes a token for it. |

### Reconciliation protocol

1. **Identify token conflicts.** After installing the system, list every identity dimension (palette, type, radius, density) and map it to a system token. Any identity value with no corresponding token is a potential override.
2. **Override via token, not raw CSS.** Prefer `--color-primary: #your-brand` over `.MuiButton-root { background: #your-brand }`. Token overrides are upgrade-safe; class overrides break on every system version bump.
3. **Flag deep overrides.** If you find yourself writing more than 10 token overrides, re-check whether the system was the right choice. A system you're fighting with 50 overrides is not a system you're using — it is a dependency you've forked without the benefits.
4. **Preserve accessible color roles.** Never remap a system's `on-primary` or `on-surface` token to a low-contrast value. The system's contrast ratios are baked into the role names — overriding them silently breaks accessibility.

---

## Stack Reference

| Stack | Default for |
|-------|------------|
| `next` + Tailwind v4 | Modern SaaS, marketing, indie builds |
| `next` + shadcn/ui | Product UI where you own the components |
| `react` + Carbon | IBM/data-dense enterprise |
| `react` + Fluent v9 | Microsoft-adjacent SaaS |
| `vue` / `nuxt` + custom | Agency and European SaaS |
| `svelte` / `sveltekit` | Performance-critical, indie |
| `astro` | Content-heavy, editorial, marketing sites |
| Kotlin Compose | Android / KMP desktop |
| SwiftUI | iOS / macOS native |
| Flutter | Cross-platform mobile |
