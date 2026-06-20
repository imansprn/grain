# Anti-Patterns

**Note:** Identity coherence (see `identity.md`) is the primary defense against slop. Anti-patterns below catch what identity misses. If identity is well-defined, most of these cannot occur.

## Dashboard Syndrome

**Warning signs:**
- Every screen is called a dashboard
- Charts displayed without a specific decision they inform
- Metrics shown because they're available, not because they're actionable
- Multiple unrelated widgets sharing screen space

**Fix:** Replace dashboards with task-focused screens. Each screen should enable one primary user goal. If a chart doesn't inform a specific decision, remove it.

## Card Grid Syndrome

**Warning signs:**
- Every content unit wrapped in a card with shadow/border
- All cards same size regardless of content importance
- No information hierarchy — everything visually equal
- No horizontal or vertical rhythm variation

**Fix:** Use tables for dense data, lists for scanning, timelines for sequences, workflows for processes. Cards work for heterogeneous content with equal importance. Most apps overuse them.

## Feature Dump Syndrome

**Warning signs:**
- Every possible feature on a single screen
- No progressive disclosure — all controls visible at once
- No prioritization — primary and secondary actions visually equal
- Toolbar/header crowded with icons

**Fix:** Show the 20% of features that handle 80% of tasks. Hide advanced functionality behind progressive disclosure. Use the "three-click rule" — advanced features should be available within three clicks, not visible by default.

## Sidebar Syndrome

**Warning signs:**
- Navigation sidebar with 8+ items but only 3 are used regularly
- Sidebar occupies 20%+ of horizontal space on desktop
- Content area feels like a secondary concern
- User sees a shell/navigation wrapper before meaningful content

**Fix:** Audit navigation frequency. Reduce depth. Consider top navigation, context-aware navigation, or command palettes. The measure of good navigation is how invisible it is.

## Form Hell

**Warning signs:**
- 10+ fields in a single form
- Required fields mixed with optional fields indiscriminately
- No grouping or logical progression
- No smart defaults

**Fix:** Cut fields relentlessly. Group related fields. Use progressive disclosure for advanced options. Set intelligent defaults. Every additional field reduces conversion. If a field can be derived from another field or from user data, derive it.

## Confirmation Overuse

**Warning signs:**
- "Are you sure?" on every destructive action
- Confirmation dialogs for reversible actions
- Inconsistent undo support

**Fix:** Make destructive actions reversible (undo, trash, version history). Only confirm for irreversible actions with significant consequences. Undo is always better than "Are you sure?"

## Empty State Neglect

**Warning signs:**
- Empty screens show nothing or a generic spinner
- No guidance on what to do first
- No illustration of what the screen will look like with data

**Fix:** Every empty state should: 1) Explain what this screen does, 2) Show what content will appear, 3) Provide an action to add the first item. Empty states are the most overlooked onboarding opportunity.

## Loading State Neglect

**Warning signs:**
- Full-page spinners
- No skeleton screens
- No optimistic updates
- Blocking UI during background operations

**Fix:** Show skeleton screens matching final layout. Use optimistic updates for predictable operations. Never show a full-page spinner — always preserve navigation and context.

---

# AI Slop Patterns

These are patterns unique to AI-generated UI. They occur because AI models are trained on templates, not on product thinking.

## Template Hero

**Warning signs:**
- Centered headline + subtitle + two CTA buttons (Get Started / Learn More)
- Background is a gradient or abstract geometric pattern
- Mockup image (laptop/phone showing the same product) below the fold
- Navigation bar with logo-left, links-center, CTA-right

**Fix:** Start with the user's goal, not a layout template. A hero section that every SaaS product uses is a sign you haven't thought about what makes this product different. Consider: no mockup, no dual CTAs, no geometric backgrounds.

## Alternating Image-Text Grid

**Warning signs:**
- Every section: left image / right text, then right image / left text, repeating
- Each section has an icon in a colored circle, a heading, and 2-3 bullet points
- No variation in layout across 4+ sections

**Fix:** Vary section layouts. Not everything needs an image. Not everything needs to be split 50/50. Consider full-width text sections, data tables, comparison grids, timelines, or workflow diagrams. Repetition reveals lack of content strategy.

## Card Inception

**Warning signs:**
- Cards containing cards containing cards
- Pricing page with 3-4 pricing cards, each containing feature list cards
- Dashboard with card widgets containing card list items

**Fix:** Flat hierarchy. A card inside a card means your information architecture is wrong. Flatten it — use a list inside the outer card, or make the inner card a standalone section.

## Generic Feature Illustration

**Warning signs:**
- Every feature has a colored circle/rounded-square icon background
- Icons are generic (lightbulb, rocket, chart-up, shield, gear, people)
- 3D illustrations of people with missing body parts (floating heads, no hands)
- Stock photography with color overlays

**Fix:** Use real screenshots, data visualizations, or no illustration at all. Generic icons signal generic features. If the feature is meaningful, show it working — not a lightbulb icon.

## Unmotivated Gradient

**Warning signs:**
- Gradient background with no relationship to brand
- Gradient on elements that don't need emphasis
- Multiple gradients competing on one page
- "Vibrant" gradients used to make a generic layout feel premium

**Fix:** Use color with purpose. A gradient should direct attention, signal a state, or encode information. If you can't explain why the gradient exists, remove it.

## Three-Step How-It-Works

**Warning signs:**
- Exactly 3 steps, each with a numbered circle
- "Step 1: Sign up / Step 2: Configure / Step 3: Done"
- Identical layout for each step card

**Fix:** If the process actually has 4 steps, show 4. If it has 2, show 2. If it doesn't need steps at all (most products don't), remove the section. Show the product working instead of explaining it with numbered circles.

## Fabricated Content

**Warning signs:**
- "+47% conversion" / "10x faster" / "99.9% uptime" — metrics without source
- "Trusted by 50,000+ teams" — user counts without data
- Named testimonials with portrait photos from invented people
- Client logo grid of unidentifiable companies
- "Used in 190+ countries" — geographic reach fabricated
- "4.8/5 from 2,000+ reviews" — ratings without real review platform

**Fix:** Remove every piece of data the user did not supply. Use placeholder blocks (grey `███` with "metric to confirm" label) for sections that need data. Remove testimonials entirely unless the user provides real quotes from real people. Honest copy with fewer sections beats decorated copy with invented proof. See `honest_copy.md`.

## Team Grid

**Warning signs:**
- Grid of circular photos with name + title + optional bio
- Same layout for every team member
- All photos are evenly lit headshots
- "Join our team" CTA at the bottom

**Fix:** If the team page exists because the user asked for one, fine. If it exists because "every site has one," remove it. When it does exist, vary the layout — lead team members larger, group by department, show them in context.

## Footer Dump

**Warning signs:**
- 4-column footer with 20+ links
- "Product" / "Company" / "Resources" / "Legal" columns
- Newsletter signup + social media icons

**Fix:** Show the 5 links users actually click. Everything else belongs in a sitemap, not a footer. A footer with fewer links is more useful.

---

# High-Specificity AI Tells

These patterns are distinct from the general slop patterns above. They are harder to catch because they feel intentional — they look "designed" when generated by an AI, but are recognizable as AI output to trained designers.

## Em-Dash as Design Element

**Warning signs:**
- Em-dash (`—`) in headlines, eyebrows, button text, or attribution
- "Fast — reliable — secure" in hero sections
- "Sarah Johnson — Head of Product" in testimonials
- En-dash (`–`) used as a separator in ranges

**Fix:** Remove every em-dash. In headlines: use a period or comma. In attribution: use a line break or hyphen with spaces (` - `). In ranges: use a hyphen. This is a hard rule, not a preference — the em-dash is the single most reliable AI-copy tell in production tests.

## Hero Overload

**Warning signs:**
- Hero section doesn't fit in the initial viewport — CTA requires scroll to find
- Headline wraps to 3+ lines at desktop width
- More than 4 text elements in the hero (eyebrow + headline + subtext + CTA + tagline + trust strip = 6)
- Subtext longer than 20 words

**Fix:** Hero max 4 text elements: one eyebrow (optional), one headline (≤ 2 lines), one subtext (≤ 20 words), one CTA cluster. Everything else is a separate section below. If the hero overflows, reduce font size or cut copy — do not increase padding.

## Eyebrow Everywhere

**Warning signs:**
- Every section has a small uppercase label above the heading (`FEATURES`, `HOW IT WORKS`, `PRICING`, `TESTIMONIALS`)
- All sections have the same rhythm: eyebrow → headline → body
- More than 1 eyebrow per 3 sections

**Fix:** Mechanical check: count instances of small uppercase tracking labels across all sections. If count > `ceil(sectionCount / 3)`, remove the excess. The section's position on the page categorizes it. An eyebrow that says "FEATURES" above a features section is redundant — the features are the features.

## Premium Consumer Default Palette

**Warning signs:**
- Brief is cookware, wellness, artisan goods, luxury, heritage craft, DTC home goods
- Palette defaults to: warm beige/cream backgrounds (`#f5f1ea`, `#fbf8f1`), brass/clay accents (`#b08947`, `#b6553a`), espresso text (`#1a1714`)
- Every premium-consumer project uses this same palette

**Fix:** This palette is the LLM's trained default for "premium" and is instantly recognizable. Concrete alternatives: **Cold Luxury** (silver + chrome + smoke), **Forest** (deep green + bone + amber), **Black and Tan** (off-black + warm tan, no beige), **Cobalt + Cream** (saturated blue + single neutral), **Pure monochrome + one saturated pop** (off-white + off-black + electric blue or emerald). The warm beige + brass palette is acceptable only when the brand brief explicitly names those colors.

## Default AI Font Choice

**Warning signs:**
- Using Fraunces or Instrument_Serif as display fonts for any project
- Reaching for serif type because the brief is "creative" or "premium"
- Inter used as the default sans without a stated reason

**Fix:** Fraunces and Instrument_Serif are the two most overused AI-generated display serifs — they signal AI output to designers immediately. Serif is appropriate only for genuinely editorial, luxury, or publication briefs — not for "creative agency" or "premium consumer" as defaults. For sans: prefer Geist, Outfit, Cabinet Grotesk, or Satoshi over Inter unless Inter is specifically chosen for a neutral/Linear-style identity.

## Split-Header Layout

**Warning signs:**
- Section header uses a split: large headline on the left, small explanatory paragraph floating in the top-right corner
- The right-column paragraph has no clear alignment relationship to anything else in the section

**Fix:** This pattern looks designed but communicates nothing the headline alone wouldn't. Stack vertically: headline on top, body below, max-width 65ch. Use the split only when the right column holds a real visual or interactive element — not explanatory text.

## Zigzag Section Repetition

**Warning signs:**
- 3 or more consecutive sections alternate left-image/right-text then right-image/left-text
- Page has no section that breaks the alternating rhythm

**Fix:** The zigzag pattern is the alternating-image-text anti-pattern (documented above) at the page level. Maximum 2 consecutive sections may use the same image+text-split layout. The third must use a fundamentally different structure: full-width, bento grid, vertical stack, timeline, or data table.
