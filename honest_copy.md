# Honest Copy

## Rule

Never invent data, metrics, testimonials, logos, or user quotes. If the user did not supply it, do not fabricate it.

This is a hard rule. It applies to every section type: hero stats, feature callouts, testimonial cards, proof bars, pricing comparisons, social proof, case study results, and all microcopy.

## What Not to Invent

| Data Type | Slop Examples | What to Do Instead |
|-----------|---------------|-------------------|
| Metrics | "+47% conversion", "10x faster", "99.9% uptime" | Remove the stat, or use `--` with labeled placeholder |
| Testimonials | "John D., CEO of Acme" with portrait photo | Remove section, or ask user for real testimonials |
| Client logos | Logo grid of invented companies | Remove section, or ask user for client list |
| User counts | "Trusted by 50,000+ teams" | Remove. Never fabricate scale. |
| Country/city stats | "Used in 190+ countries" | Remove. |
| Case study results | "Increased revenue by 300%" | Remove, or mark clearly as illustrative |
| Reviewer ratings | "4.8/5 from 2,000+ reviews" | Remove. |

## Placeholder Strategy

When a section needs data the user hasn't provided, use this pattern:

```
<!-- metric to confirm -->
███ ███████
(small grey block, labeled "verify metric")
```

In CSS: a `rgba(0,0,0,0.06)` background block with italic label text. Never use Lorem Ipsum — slop detection looks for it. Never use full-width dashes that look like real data.

## Exceptions

The only exception is demo/sample data explicitly marked as such:
- A sandbox environment or demo mode
- The user says "use dummy data" or "make up examples"
- A prototype/wireframe phase clearly labeled "not final"

In all three cases, mark each fabricated element with a visual indicator: `[demo]` suffix, different background color, or tooltip.

## Why This Matters

Fabricated data corrupts trust. A user who spots one invented testimonial will assume everything is invented. This is the fastest way to make a design feel like AI-generated slop — because the real product *doesn't have those stats* and never will.

Honest copy with fewer sections beats decorated copy with invented proof every time.
