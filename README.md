# Product UI Architect

Prevents generic AI-generated interfaces. Three paths: Greenfield (new design), Audit (analyze existing), Remediate (fix existing).

**Single source of truth:** [`SKILL.md`](SKILL.md) — all process, rules, and output formats live there.

## Quick Start

| You want to… | Start here |
|-------------|-----------|
| Design a new screen from scratch | `SKILL.md` → Greenfield Process |
| Review an existing project for issues | `SKILL.md` → Audit Process |
| Fix problems in an existing project | `SKILL.md` → Remediate Process |
| Check for AI slop patterns | `python3 lint/lint.py <path>` |
| Design a single component | `component_scope.md` |

## Linter

```sh
python3 lint/lint.py /path/to/project             # human-readable
python3 lint/lint.py /path/to/project --exit-code # CI mode
python3 lint/lint.py /path/to/project --format json
```

22 deterministic rules. Covers HTML/CSS/JSX/TSX/Kotlin/Swift/Dart/Python.

## Validation

| Project | Lines | Domain | Result |
|---------|-------|--------|--------|
| CraftBy.dev (Next.js 15) | ~2000 | Developer portfolio | Identity match. Zero slop. 5 minor findings. |
| GOST (KMP Compose Desktop) | ~6600 | Premium-dark-SaaS (misapplied) | Identity mismatch. Dead screen. Sidebar bloat. 3 anti-patterns. |
