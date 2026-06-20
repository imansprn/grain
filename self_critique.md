# Pre-Emit Self-Critique

Before delivering any output, score it on six axes. Any score below **3** triggers a revision pass.

## Scoring Axes

| Axis | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|
| **Philosophy** | No design rationale. Decisions are arbitrary. | Weak rationale. "It looks clean." | Basic rationale tied to identity or audience. | Clear rationale referencing identity + product purpose. | Every decision traceable to identity + domain + user need. |
| **Hierarchy** | All elements visually equal. No scan path. | Weak hierarchy. Primary action not obvious. | Primary action visible. Secondary actions clear. | Clear visual weight per element. Optimal scan path. | Hierarchy matches user priority perfectly. Glance tells you what to do. |
| **Execution** | Broken responsive, missing states, no token usage. | Responsive has issues. Skeleton states missing. | Responsive works. States present but basic. | Responsive at 3 breakpoints. All 12+ states handled. | Responsive at 4+ breakpoints. Every state polished. Animations work. |
| **Specificity** | Generic content. "Build something great." | Vague copy. Interchangeable with any competitor. | Specific to product. Real feature names. | Copy that only this product could have. | Every word unique to product. No template language. |
| **Restraint** | Every section present. Full card grid. Gradient hero. | Too many sections. Some unnecessary elements. | Removed obvious dead weight. No gratuitous elements. | Every section justified. Asks "can this be removed?" for each. | Minimal viable page. Nothing left to remove. |
| **Variety** | Template layout. Alternating image-text. Card grid. | Minor variations in section rhythm. | Different macrostructures per page type. | Variance across all structural axes. | Every page has unique fingerprint. No two pages feel templated. |

## Revision Protocol

1. Score all 6 axes
2. If any score < 3: **do not deliver** — follow the revision path for that axis below, then re-score
3. If score ≥ 3 on all: stamp and deliver

### Revision paths by axis

**Philosophy (P < 3):** Re-read the identity. For every design decision in the output, write one sentence explaining why it exists — referencing palette, type, density, shape, or tone. Remove any element you cannot justify. Re-score.

**Hierarchy (H < 3):** Identify the single most important action on each screen. Ensure its visual weight (size, contrast, position) is 2× the next most important element. Flatten competing elements. Re-score.

**Execution (E < 3):** Scan for missing states: loading skeleton, empty state, error message, disabled interaction, focus ring. Add them. Check responsive at 375px, 768px, 1280px. Re-score.

**Specificity (S < 3):** Replace all generic copy ("Build something great", "Start your journey", "Our platform") with product-specific language referencing real feature names, real data types, or real user tasks. Re-score.

**Restraint (R < 3):** Apply the removal test: hide each section and ask "does the page still make sense?" Remove any section that fails. Remove any decorative element without a function. Re-score.

**Variety (V < 3):** Check `.product-architect/log.json`. If the macrostructure matches any of the last 3 entries, pick a different one. If nav/footer repeat, swap to a different archetype. Re-score.

## Output Stamp

Include the scores in a CSS comment or markdown block at the top of deliverable output:

```
/* Self-critique: P4 H5 E3 S4 R5 V4 */
```

Stamped scores are the accountability record. If the user sees low scores later, they know the revision was skipped.
