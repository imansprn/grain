# Diversification

## Purpose

Prevent consecutive outputs from feeling like the same template in different colors. Two pages for different briefs must not share the same macrostructure, theme, or nav/footer pattern.

## Limitations

This system requires filesystem write access. In chat-only sessions (no project directory open), the AI cannot write or read `log.json` — diversification silently degrades to best-effort. In that case, ask the user: *"What macrostructure did you use last time?"* and rotate manually.

When filesystem access is available, verify the file exists before reading. If it does not exist, treat this as a first run.

## Project Memory

The skill maintains a log at `.product-architect/log.json`:

```json
[
  {
    "date": "2026-06-18",
    "macrostructure": "Marquee Hero",
    "identity": "Flowly (navy, SF Pro, 4px)",
    "nav": "N5 (floating pill)",
    "footer": "Ft1 (compact)",
    "brief": "Flowly task manager landing page"
  }
]
```

Create the file on first run. Read it on subsequent runs in the same project directory.

## Diversification Rules

### Macrostructure
Must differ from the last **3** entries in the log. If last 3 were Manifesto, Bento Grid, and Long Document, pick any of the remaining 9.

### Theme Axes
If the project uses themes (colorways), consecutive outputs must differ on at least **2 of 3** axes:
- **Paper band** — dark (L < 30%) / mid (30-85%) / light (> 85%)
- **Display style** — serif / sans / mono / condensed
- **Accent hue** — warm (10-60°) / cool (200-300°) / neutral (no accent) / other (green, purple)

For identity-defined projects (our default model): identity defines fixed values, so theme rotation doesn't apply. The identity IS the theme. Diversification comes from macrostructure and nav/footer instead.

### Nav Archetype
Must differ from the last entry's nav. If previous was N1b (centered SaaS), pick N5 (floating pill), N3 (side-rail), N8 (terminal bar), or N9 (edge-aligned).

### Footer Archetype
Must differ from the last entry's footer. If previous was Ft2 (standard, 3 columns), pick Ft1 (compact), Ft4 (statement), or none.

## State Your Pick

Before writing any code, state the diversification decision:

```
Last build: Bento Grid (Coral theme). Picking Marquee Hero (different macrostructure).
Nav: N5 (was N1b). Footer: Ft1 (was Ft2).
```

This is the accountability line. Picking on the page prevents default-attractor behavior.

## Edge Cases

| Situation | Response |
|-----------|----------|
| First run in project | "No prior builds — first design for this project." Pick freely. |
| Only 1-2 prior entries | Constrain against what exists. If only 1 prior, pick any macrostructure except that one. |
| User explicitly requests same structure | Note the override in the log. State: "Repeating macrostructure at user request." |
| Component run | No log entry. Components don't trigger diversification. |

## .gitignore

Add `.product-architect/` to the project's `.gitignore` to prevent the log and preflight cache from being committed:

```
# product-ui-architect skill cache
.product-architect/
```

If no `.gitignore` exists in the project root, create one with this entry. The `.product-architect/` directory contains only local session data — it has no meaning in version control.
