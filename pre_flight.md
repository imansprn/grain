# Pre-Flight Scan

## Purpose

Read existing project code before designing to avoid stomping on established patterns. Running design work without knowing what exists is how slop replaces a working system.

## Signal Sources

Scan in order. Stop when you have enough context — you don't need all six.

1. **`design.md` or `DESIGN.md`** at project root → this is a locked design system. Read it. It overrides identity definition. If found, skip identity definition (Greenfield Step 2) and use this file as the source of truth for palette, type, spacing, motion, and constraints. State: *"DESIGN.md detected — this is a system-managed project. Deferring to existing identity."*

2. **Font stack** → `package.json` for `next/font`, `@fontsource/*`, `geist`; `<link>` to Google Fonts; `tailwind.config` `fontFamily`; `@import url()` in CSS.

3. **Palette** → OKLCH/HSL/hex values inside `:root`; `tailwind.config` `colors`; `tokens.json` or DTCG-shaped files.

4. **Motion stance** → `framer-motion`, `gsap`, `motion`, `lenis`, `lottie-react` in `package.json` → "motion-on" project. None → "motion-cut".

5. **Spacing scale** → Tailwind `spacing` extend; CSS `--space-*` pattern; 4pt or 8pt scale.

6. **Framework** → `next` (Next.js), `astro` (Astro), `vue` (Vue), `svelte` (SvelteKit), `@remix-run/*` (Remix), or vanilla HTML.

## Output Format

Emit this block before any design work, with file:line citations:

```
Pre-flight:
- Font: Geist + Geist Mono (next/font, package.json L23)
- Palette: OKLCH custom properties (app/globals.css :root)
- Motion: framer-motion 11 (package.json L41)
- Spacing: Tailwind 4pt scale (tailwind.config.ts L18)
- Framework: Next.js 15

Preserving: font stack, palette, spacing scale.
Introducing: identity constraints, macrostructure, anti-pattern detection.
```

## Caching

Write to `.product-architect/preflight.json`. Re-use on subsequent runs unless:
- User says "refresh pre-flight"
- `package.json` or `tailwind.config.*` mtimes are newer than cached file

If cached, emit one line: *"Pre-flight cached (last scan: YYYY-MM-DD). Say 'refresh' to re-scan."*

## Edge Cases

| Situation | Response |
|-----------|----------|
| No signals found | "No pre-flight signals — proceeding with full skill stack." |
| Conflicting signals | "Conflict: Geist imported but font-family: Inter hard-coded in L4. Preserving Geist; confirm or remove." |
| `design.md` found | Read it. Skip identity definition. Proceed to macrostructure. |
| User says "go ahead, don't scan" | Skip pre-flight. "Pre-flight skipped at user request." |
