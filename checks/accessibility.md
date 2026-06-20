# Accessibility Checklist

## Keyboard Navigation

- [ ] All interactive elements reachable via Tab in logical order
- [ ] Tab order matches visual order
- [ ] Focus indicators visible on all elements
- [ ] No keyboard traps (can Tab out of any element)
- [ ] Escape closes modals, dropdowns, and overlays
- [ ] Enter/Space activates focused buttons and links
- [ ] Arrow keys work for selection lists, tab panels, sliders
- [ ] Custom components have appropriate ARIA roles

## Screen Reader Support

- [ ] All images have alt text (decorative images use alt="")
- [ ] Form inputs have associated labels
- [ ] Error messages are announced via aria-live or aria-describedby
- [ ] Dynamic content updates are announced
- [ ] Headings hierarchy is logical (h1→h2→h3, no skips)
- [ ] Landmarks used (nav, main, aside, footer)
- [ ] Icons have aria-hidden="true" + text alternative
- [ ] Status messages use role="status" or aria-live="polite"

## Visual

- [ ] Color contrast meets WCAG AA (4.5:1 text, 3:1 large text)
- [ ] Color is not the only differentiator (also use icons, labels, patterns)
- [ ] Text can be zoomed to 200% without loss of content
- [ ] Line height minimum 1.5 for body text
- [ ] Links are visually distinguishable from body text
- [ ] Focus indicators have minimum 2px width

## Touch / Motion

- [ ] Touch targets minimum 44x44pt (mobile)
- [ ] Touch targets minimum 32x32pt (desktop, if touch-supported)
- [ ] No motion-only interactions (shake, tilt, swipe without fallback)
- [ ] Reduced motion media query respected (prefers-reduced-motion)
- [ ] Animations can be paused
- [ ] Auto-playing content can be stopped

## Forms

- [ ] Error messages are associated with their input
- [ ] Required fields are clearly marked
- [ ] Autocomplete attributes used for known fields (name, email, address)
- [ ] Field validation errors are shown inline, not just at top of form
- [ ] Success messages are announced

## Testing

- [ ] Navigate entire app using only keyboard
- [ ] Test with screen reader (VoiceOver, NVDA, JAWS)
- [ ] Test with browser zoom at 200%
- [ ] Test with high contrast mode
- [ ] Test with reduced motion enabled
