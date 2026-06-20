# Design Review

## Domain-Identity Fit Check (Run First on Existing Projects)

Before reviewing screens, check if the identity fits the product domain. A mismatch means even well-executed screens feel wrong.

| Domain | Suitable Identity | Wrong Identity |
|--------|------------------|----------------|
| Developer tool (CLI, proxy, terminal) | Technical, compact, dense, minimal color | Premium dark SaaS, rounded cards, gradients |
| Consumer e-commerce | Spacious, editorial, visual-first | Compact, data-dense, monospace |
| Banking / finance | Professional, calm, trustworthy, spacious | Playful, techy, dense |
| Analytics dashboard | Data-first, compact, precise labels | Decorative, playful, spacious |
| Health / fitness | Motivational, energetic, human | Corporate, medical-green, clinical |
| Enterprise B2B | Professional, efficient, moderate density | Consumer-playful, editorial-spacious |

**If identity and domain don't fit, the identity must change.** A gradient SaaS skin on a terminal proxy manager is wrong. Domain determines identity, not the other way around.

## Identity Coherence (Run After Domain Fit)

Before asking anything else, verify the screen belongs in this identity:

- Does the palette match the identity? (If no, the wrong color was used)
- Do the typefaces and scale match the identity? (If no, wrong font or size)
- Does the density match the identity? (If no, spacing is wrong)
- Does the shape language match the identity? (If no, wrong border radius)
- Does the layout follow identity's layout patterns? (If no, wrong layout template)
- Does the screen violate any hard constraint? (If yes, redesign immediately)

**Identity coherence is not optional.** A screen that violates identity is wrong regardless of how good it looks in isolation.

## Mandatory Questions

For every screen or flow, ask each question. If the answer is "no," redesign.

### Removal

- Can any screen be removed?
- Can any step in this flow be removed?
- Can any field in this form be removed?
- Can any button/control be removed?

### Automation

- Can any user decision be automated?
- Can any data entry be prefilled?
- Can any state be inferred rather than explicitly set?
- Can any notification be suppressed until actionable?

### Shortening

- Can the number of steps to complete the primary task be reduced?
- Can any loading state be eliminated with optimistic updates?
- Can any confirmation dialog be replaced with undo?

### Clarity

- Does the primary action have the most visual weight?
- Is it obvious what the user should do first?
- Are error messages actionable (what happened + how to fix)?
- Is the user's current location always clear?

### Efficiency

- Can power users complete tasks faster (keyboard shortcuts, bulk actions, templates)?
- Are default values sensible for the most common case?
- Is search available where finding items is part of the workflow?

## Comparative Approaches

When deciding between design directions, apply each lens:

### Linear Lens
**Scenario:** User needs speed above all (trading, dispatch, admin actions).
- Could this be a single-page experience instead of multi-page?
- Can primary action be a keyboard shortcut?
- Can secondary features be hidden behind a command palette?
- Remove one step from every flow. Then remove another.

### Notion Lens
**Scenario:** User needs flexibility (content management, wikis, project tracking).
- Can content be broken into blocks/components users rearrange?
- Can the user extend or customize without developer help?
- Where can templates reduce starting friction?
- Does progressive disclosure work better than modal dialogs?

### GitHub Lens
**Scenario:** User needs to scan dense information (monitoring, logs, code review, analytics).
- Can data density be increased? (Smaller fonts, tighter spacing, fewer lines)
- Can every row/item show more information without overwhelming?
- Is there a keyboard-driven navigation path for every action?
- Would a table outperform cards for this data?

### Apple Lens
**Scenario:** Confidence is critical (payments, banking, healthcare, onboarding).
- Can the user undo every action?
- Is every state explained in plain language?
- Does the interface make the user feel in control?
- Polish the transition, microcopy, and error states before adding features.

If none of the four lenses clearly fits, the default is Apple (confidence) — users trust products that feel considered.
