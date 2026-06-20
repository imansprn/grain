# Design Principles

| # | Principle | Meaning |
|---|-----------|---------|
| 1 | Product before pixels | Understand the product purpose before choosing colors, fonts, or layouts. Every visual decision must serve a product goal. |
| 2 | Workflow before layout | Design the user's journey through tasks before arranging elements on a screen. Layout should make workflows efficient, not just look balanced. |
| 3 | Clarity before aesthetics | A clear interface that users understand immediately beats a beautiful interface they don't. Polish comes after comprehension. |
| 4 | Simplicity before flexibility | Default to the simplest solution. Add configurability only when real user needs demand it. Avoid premature abstraction. |
| 5 | Discoverability over cleverness | Users should find features without training. Obvious beats clever every time. Custom gestures and hidden shortcuts are technical debt for usability. |
| 6 | Consistency over novelty | Use established patterns users already know. Novel interactions must be justified by significant efficiency gains. |
| 7 | Accessibility by default | Accessible design is better design for everyone. High contrast, readable text, keyboard navigation, and screen reader support are not optional. |

## Application

When evaluating any design decision, ask:

- Does this violate any of the 7 principles?
- If yes, is the violation justified by a specific user need?
- If not justified, remove or redesign it.

---

## Conflict Resolution

Principles tension against each other regularly. Here is how to resolve the most common conflicts:

### Clarity vs. Consistency (P3 vs. P6)

**Conflict:** An established pattern exists (e.g., icon-only toolbar), but users in this context don't recognize the icons without labels.

**Resolution:** Clarity wins. The point of consistency is that familiar patterns reduce learning cost — but if users in this domain don't share the assumed familiarity, the pattern isn't actually consistent with their mental model. Add labels. Deviation is justified.

**Example:** A developer tool using icon-only navigation is consistent with the developer tool genre. The same icon-only nav on a tool for non-technical operations staff breaks clarity. Add labels for the second audience even if it looks "less clean."

---

### Simplicity vs. Accessibility (P4 vs. P7)

**Conflict:** Adding keyboard navigation, ARIA attributes, and focus management makes the component more complex to build and maintain.

**Resolution:** Accessibility wins, always. Simplicity means don't add complexity without reason — accessibility is a reason. The "simplest solution" is the one that works for the widest range of users, not the one with the fewest lines of code.

---

### Discoverability vs. Simplicity (P5 vs. P4)

**Conflict:** Making every feature discoverable (tooltips, empty states, onboarding hints) adds UI surface. Keeping the interface simple means hiding some features.

**Resolution:** Resolve by user segment. For features used daily by power users, discoverability matters less — those users will invest time to learn. For features that are critical to first-time success (onboarding actions, first-use flows), discoverability wins over simplicity. Progressive disclosure is the synthesis: simple by default, discoverable when needed.

---

### Consistency vs. Workflow (P6 vs. P2)

**Conflict:** The established pattern for this type of screen (e.g., a horizontal tab strip) doesn't match the workflow (a linear wizard with enforced step order).

**Resolution:** Workflow wins when the task has inherent order or dependencies. Tabs imply parallel, equal-weight content — use them when steps are non-linear. Use a wizard (step indicator + linear progression) when steps must happen in sequence. Adopting tabs for a wizard to feel "consistent with the rest of the app" creates a mismatched mental model that hurts task completion.

---

### Product vs. Aesthetics (P1 vs. P3)

**Conflict:** The product purpose is clear, but the design that best serves it is visually minimal to the point of feeling unfinished or low-effort.

**Resolution:** Ship the minimal version. Visual richness that doesn't serve the product purpose is decoration — and decoration obscures function. A table with good typography and clear hierarchy is complete. Padding it with illustrations, gradient headers, and stat cards to make it "feel designed" violates P1. If the output looks sparse, the question to ask is: "what product goal would visual richness serve?" If there's no answer, don't add it.

---

### Simplicity vs. Discoverability in Power Tools (P4 vs. P5)

**Conflict:** Developer tools, admin panels, and monitoring dashboards accumulate many controls. Making all features discoverable produces feature dump syndrome. Hiding them produces discoverability debt.

**Resolution:** Use the 80/20 rule deliberately. The 20% of features used 80% of the time are always visible and labeled. The rest are behind progressive disclosure — secondary menus, right-click context menus, command palettes, or settings. This is not inconsistency; it is deliberate tiering. Document the tiers in the identity's layout rules so the decision is explicit and repeatable.
