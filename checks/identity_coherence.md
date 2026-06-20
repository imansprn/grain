# Identity Coherence Checklist

For every screen, verify against the identity definition. A screen that doesn't pass this check does not ship.

---

## The "Belongs" Test

Before running the checklist, ask one question per screen:

> *"If I dropped this screen into a competitor's app, would it look out of place — or would it blend right in?"*

If it would blend in, the identity is not doing its job. The identity should make every screen unmistakably belong to this product.

---

## Color

- [ ] All colors used are in the identity palette — no ad-hoc hex values
- [ ] No banned color patterns (gradients, warm tones if banned, illustrative palettes)
- [ ] Semantic colors (success, error, warning) match palette semantic map, not custom standalone choices
- [ ] Accent color is not overused — accent should appear ≤ 3 times per screen as a signal, not decoration
- [ ] Surface colors follow the defined elevation stack (background < panel < card < input — each one step lighter/elevated)

**Diagnostic question:** Can you explain why each color on this screen is the color it is, referencing the identity document? If the answer is "it looked right," fail this check.

---

## Typography

- [ ] Only identity font families used — no new family introduced on a single screen
- [ ] Sizes are from the identity scale — no one-off `14.5px` or `19px` values
- [ ] Weights are in the identity weight set — no `font-weight: 300` if identity only specifies 400/500/700
- [ ] Body text, labels, and code/mono use the role assignments from the identity (not arbitrary family swaps)

**Diagnostic question:** Is there any text on this screen you couldn't place in the type scale table? If yes, that's a new token introduced without identity coverage.

---

## Density

- [ ] Spacing is consistent with the identity density level (compact / balanced / spacious)
- [ ] No mixed density within the same screen type — a compact identity doesn't have one airy section in the middle
- [ ] Padding on interactive elements matches identity (e.g., compact identity: 8px vertical, not 20px)
- [ ] Line height and label spacing follow the identity's declared scale, not default framework values

**Diagnostic question:** If you set this screen beside the previous screen designed under this identity, do they feel like the same product?

---

## Shape

- [ ] Border radius matches identity direction (sharp / subtle / rounded) — not framework defaults
- [ ] No mixed radius patterns without a semantic reason (cards use one radius, inputs another, but both are documented)
- [ ] No circular containers unless identity explicitly allows them
- [ ] Shadows (if any) match the identity's shadow stance (none / subtle / layered)

**Diagnostic question:** Would the shape language change if someone redesigned this screen without reading the identity? If yes, the shape choices are not distinctive enough to enforce themselves.

---

## Tone

- [ ] Microcopy matches identity tone — no "Hey there!" on a technical identity, no clinical labels on a consumer identity
- [ ] Illustration presence matches identity — no illustrations on "no illustration" identities, even as empty-state placeholders
- [ ] Icon style matches (outlined/filled/duo-tone) — no mixing icon families
- [ ] Error messages match tone — errors on a direct/technical identity are specific and actionable, not apologetic and friendly

**Diagnostic question:** Read all the copy on the screen aloud. Does it sound like the same voice as every other screen in the product?

---

## Layout

- [ ] Layout pattern is in the identity's approved patterns (e.g., sidebar + main for Workbench, not a hero for a product screen)
- [ ] No rejected layout patterns are present (if identity rejects hero-image, there is no hero-image — even on a marketing sub-page)
- [ ] Information density per screen type matches — primary screens are not sparser than detail screens unless the hierarchy demands it

---

## Motion

- [ ] Motion level matches identity dial (M1 = functional only, no entrance animations; M5+ = transitions allowed)
- [ ] No decorative motion on still/M1 identities — no `animate*` calls without a direct user-action trigger
- [ ] Reduced motion media query (`prefers-reduced-motion`) is respected on all animated elements
- [ ] Transition timing matches identity (M1-3: `150ms ease`; M4-6: `250-300ms ease-in-out`; M7+: custom)

---

## Hard Constraints

- [ ] Zero hard constraint violations — every constraint in the identity is a binary pass/fail
- [ ] If a constraint was almost violated ("I nearly added a gradient but didn't"), note it — it means the constraint needs to be more explicit in the identity

---

## Design System Default Check

If the project uses shadcn/ui, run this additional check before shipping any screen:

- [ ] No shadcn component looks like the out-of-box default (zinc palette, default radius, default shadow)
- [ ] `--radius` CSS variable is set to the identity's shape value, not shadcn's default `0.5rem`
- [ ] `--primary` and `--accent` map to identity palette colors, not shadcn's default zinc
- [ ] Typography uses identity font families, not shadcn's default system stack
- [ ] If any of the above fail: the design system was installed but the identity handshake was not completed. Run `design_system.md` reconciliation protocol before continuing.

**Why this matters:** shadcn/ui in default state is the most common "looks designed but isn't" output. The checklist above is the only machine-checkable gate for it — the linter cannot catch default shadcn styling.

---

## Failure Protocol

If any item fails:

1. **Color / typography / density / shape / motion failures** — revise the specific screen. Do not update the identity to match the screen. The screen must match the identity.
2. **Tone failure** — revise microcopy. If the rewrite requires identity tone to be relaxed, flag for explicit identity update with rationale.
3. **Hard constraint violation** — revert the screen. No exceptions.
4. **"Belongs" test failure** — the identity may be underspecified. Add the missing dimension to the identity document, then re-evaluate the screen against the updated constraint.
5. **shadcn default failure** — do not ship. Complete the identity token handshake in `design_system.md` first.
