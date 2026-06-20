# Macrostructures

A macrostructure is a complete page shape — section order, layout patterns, heading placement, and button voice bundled as a single named choice. Picking from a named catalog prevents the "hero → alternating features → testimonials → pricing → footer" template that every LLM defaults to.

## Index

| # | Name | Best For | Avoid For |
|---|------|----------|-----------|
| 1 | Manifesto | Vision pages, about, philosophy | Feature-heavy, data pages |
| 2 | Bento Grid | Features, team, portfolio | Long-form content, narrative |
| 3 | Long Document | Blog, docs, case studies | Landing pages, marketing |
| 4 | Stat-Led | Investor pages, results, data | Storytelling, brand building |
| 5 | Marquee Hero | Product launches, events, creative | Info-dense, multi-feature SaaS |
| 6 | Workbench | Dashboards, admin, dev tools | Marketing, editorial |
| 7 | Split Screen | Comparison, before/after, bilingual | Mobile-first, content-heavy |
| 8 | Card Grid | Resource libraries, doc indexes | Hierarchical, narrative |
| 9 | Timeline | Roadmaps, history, how-it-works | Comparative content, reference |
| 10 | Gallery | Portfolios, catalogs, showcases | Documentation, data-heavy |
| 11 | Terminal | Dev tools, CLI products, technical docs | Consumer, editorial |
| 12 | Letter | Announcements, founder messages | Feature-heavy, multi-section |

**Diversification rule:** Pick a macrostructure that differs from the last 3 entries in `.product-architect/log.json`. If no log exists, this is the first run — no constraint.

---

## 1. Manifesto

- **Layout**: Single column, wide margins, bold typographic statements
- **Hero**: Large display type, no mockup, no gradient
- **Sections**: Statement → Supporting evidence → Call to action
- **Nav**: Minimal (N1a — wordmark + 1 link)
- **Footer**: Compact (Ft1 — copyright + 2 links)
- **Voice**: Declarative, first-person, conviction-driven
- **Wrong pick if:** The brief has more than 3 features to explain, needs a pricing section, or the audience needs to understand how the product works before buying. Manifesto works for brand and vision — not feature coverage.

## 2. Bento Grid

- **Layout**: Asymmetric tile grid, varied cell sizes, content blocks of different proportions
- **Hero**: Half-width statement, rest is preview tiles
- **Sections**: Hero → Grid → CTA
- **Nav**: Centered (N1b) or floating pill (N5)
- **Footer**: Standard (Ft2)
- **Voice**: Direct, benefit-focused, visual-first
- **Wrong pick if:** The content items don't all fit in a single visual glance (long body copy per tile, narrative dependencies between tiles). Bento fails when tiles need to be read in order — it implies parallel equal content.

## 3. Long Document

- **Layout**: Narrow measure (60-70ch), continuous scroll, section headers, pull quotes
- **Hero**: Title + reading time + single lede image (optional)
- **Sections**: Narrative flow with pull quotes and block quotes
- **Nav**: Minimal or hidden (N4 — command palette)
- **Footer**: Minimal (Ft1)
- **Voice**: Editorial, patient, explanatory
- **Wrong pick if:** The primary goal is conversion (sign up, buy, subscribe). Long Document is for people who are already interested and want depth — not for people deciding whether to care.

## 4. Stat-Led

- **Layout**: Data-driven narrative, prominent numbers, minimal decoration
- **Hero**: One metric + claim, not a headline
- **Sections**: Stats → Evidence → CTA
- **Nav**: Compact (N3 — side-rail or N9 — edge-aligned)
- **Footer**: Compact (Ft4 — statement)
- **Voice**: Precise, evidence-backed, restrained
- **Wrong pick if:** The stats are fabricated, estimated, or vague ("we're 10x better"). Stat-Led only works when the numbers are real and specific. Without them, it becomes the worst form of AI slop — fake social proof dressed as data.

## 5. Marquee Hero

- **Layout**: Full-bleed hero, minimal sections below, strong top weight
- **Hero**: Full viewport, bold statement, single CTA
- **Sections**: Hero → 1-2 supporting → CTA
- **Nav**: Overlaid (N2 — floating chip) or hidden (N4)
- **Footer**: Minimal or none
- **Voice**: Bold, confident, urgent
- **Wrong pick if:** The product has more than one primary CTA, needs feature explanation, or is a B2B SaaS with a long evaluation cycle. Marquee Hero bets everything on the top — it fails when the user needs context before acting.

## 6. Workbench

- **Layout**: Sidebar + main content area, tool-like, utility-focused
- **Hero**: None — page title + breadcrumb or command bar
- **Sections**: Navigation → Content → Context panel
- **Nav**: Sidebar (N3 — side-rail)
- **Footer**: None
- **Voice**: Utility, neutral, precise
- **Wrong pick if:** This is a marketing or informational page. Workbench signals "you are inside a tool" — using it for a landing page, documentation, or editorial content creates a mismatch that users find disorienting. It's only correct for the authenticated product shell.

## 7. Split Screen

- **Layout**: 50/50 or asymmetric split, left/right or top/bottom duality
- **Hero**: Split — one side statement, one side visual
- **Sections**: Split panels throughout
- **Nav**: Minimal (N1a)
- **Footer**: Compact (Ft1)
- **Voice**: Comparative, balanced, clear
- **Wrong pick if:** One side has significantly more content than the other (asymmetry beyond 60/40 kills the duality effect) or the content is mobile-first (split collapses to a single column, losing the point). Also wrong for more than 2 items — splits imply exactly 2 things.

## 8. Card Grid

- **Layout**: Equal-sized cards with consistent rhythm. Use only when content items have genuinely equal importance.
- **Hero**: Title + optional filter/sort bar
- **Sections**: Grid → optional detail on click
- **Nav**: Standard (N1b)
- **Footer**: Standard (Ft2)
- **Voice**: Neutral, scannable, flat hierarchy
- **Wrong pick if:** The content has hierarchy (some items are more important than others), needs a primary action above the fold, or is a generic feature list. Card Grid is the #1 AI default — avoid unless the content genuinely justifies equal-weight tiles (resource library, team directory, portfolio).

## 9. Timeline

- **Layout**: Vertical or horizontal chronological flow, step-by-step
- **Hero**: Title + timespan + key milestone count
- **Sections**: Timeline entries with alternating detail
- **Nav**: Minimal (N1a)
- **Footer**: Compact (Ft1)
- **Voice**: Narrative, sequential, milestone-focused
- **Wrong pick if:** The events don't have a strong chronological relationship, or if users need to compare items side-by-side rather than follow a sequence. Timelines also fail when there are more than ~8 entries without deep content per entry — they become overwhelming grids.

## 10. Gallery

- **Layout**: Image-led, minimal text, visual navigation
- **Hero**: Full-bleed image or first gallery item
- **Sections**: Grid of images with optional overlay text
- **Nav**: Overlaid (N2 — floating chip) or hidden
- **Footer**: Minimal or none
- **Voice**: Minimal, visual-first, context via captions
- **Wrong pick if:** The content is not primarily visual (no photography, illustrations, or UI screenshots to show) or requires explanation to make sense. Gallery fails completely when the images are stock photos or generated — it signals authenticity but delivers slop.

## 11. Terminal

- **Layout**: Monospace type, compact, minimal color, developer aesthetic
- **Hero**: One line of command output or prompt
- **Sections**: Code blocks, terminals, configuration examples
- **Nav**: Compact (N8 — terminal bar)
- **Footer**: Compact (Ft1)
- **Voice**: Technical, matter-of-fact, no decoration
- **Wrong pick if:** The audience includes non-technical users, the product is consumer-facing, or the primary action requires explanation. Terminal is legible only to people who recognize the aesthetic — using it as "different" for a general-audience product creates friction, not personality.

## 12. Letter

- **Layout**: Centered, narrow measure (50-60ch), personal tone
- **Hero**: Salutation + dateline
- **Sections**: Narrative body → signature → postscript
- **Nav**: None or single back link
- **Footer**: Minimal (Ft1)
- **Voice**: Personal, warm, direct (first-person)
- **Wrong pick if:** The message is organizational (not from a specific person), the audience expects a feature list or call-to-action, or the tone must be formal/corporate. Letter is a specific voice — it breaks if the sender or message doesn't warrant personal register.

---

## Nav Archetype Reference

| Code | Description |
|------|-------------|
| N1a | Minimal: wordmark + 1-2 inline links |
| N1b | Centered SaaS: logo-left, links-center, CTA-right |
| N2 | Floating chip: overlaid pill-shaped nav, transparent bg |
| N3 | Side-rail: vertical sidebar, icon + label |
| N4 | Hidden: no visible nav, command palette / keyboard-driven |
| N5 | Floating pill: centered floating element, elevated |
| N8 | Terminal bar: monospace bar, prompt-style |
| N9 | Edge-aligned: links along screen edge, minimal |

## Footer Archetype Reference

| Code | Description |
|------|-------------|
| Ft1 | Compact: copyright + 2-5 links, single line |
| Ft2 | Standard: 2-3 columns, links + social icons |
| Ft4 | Statement: single line, brand message or mission |
