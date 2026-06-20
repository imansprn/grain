# Grain

<p align="center">
  <em>Expert product designer, UX designer, UI designer, art director, and design critic.</em>
</p>

<br />

A portable **Agent Skill** that raises design quality. Grain is not a code generator. Its purpose is to improve quality — through structured critique, identity-first design, and demanding review.

Three modes: **Greenfield** (new design), **Audit** (analyze existing), **Remediate** (fix existing). Every output is implementation-ready.

## Installing

```bash
npx skills add https://github.com/imansprn/grain
```

Install by skill name:

```bash
npx skills add https://github.com/imansprn/grain --skill "grain"
```

You can also copy [`SKILL.md`](SKILL.md) directly into your project or paste it into a Claude Code or Cursor conversation.

## Skill

| Skill (folder) | Install name | Description |
| --- | --- | --- |
| **grain** | `grain` | Expert product designer and design critic. Greenfield design, audit, and remediation. Identity-first process, anti-slop enforcement, structured critique output. |

## Principles

- Reject AI slop.
- Prefer clarity over decoration.
- Prefer hierarchy over complexity.
- Prefer consistency over novelty.
- Prefer usability over aesthetics.
- Prefer restraint over excess.
- Every element must justify its existence.

## Review Output Format

Every design review produces:

- **Strengths**
- **Weaknesses**
- **Design Critique**
- **UX Critique**
- **Simplification Opportunities**
- **Recommended Changes**
- **Final Verdict**

## Quick Start

| You want to… | Start here |
|-------------|-----------|
| Design a new screen from scratch | `SKILL.md` → Greenfield Process |
| Review an existing project for issues | `SKILL.md` → Audit Process |
| Fix problems in an existing project | `SKILL.md` → Remediate Process |
| Design a single component | `component_scope.md` |

## Common Questions

**How is this different from a general design AI?**
Grain never praises mediocre work and never assumes a design is good because it looks modern. It challenges decisions and acts as a demanding reviewer with a structured output format.

**What is SKILL.md?**
A portable instruction file agents load automatically. Install via `npx skills add` or copy into a repo or conversation.

**Does it work with React, Vue, Svelte, SwiftUI?**
Yes. Rules target design intent and identity — not a specific framework or platform.

## License

[MIT License](LICENSE) · Copyright (c) 2026 imansprn
