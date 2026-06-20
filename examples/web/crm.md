# CRM Example (Web)

## Design Identity

```yaml
identity:
  name: CRM for SMB sales teams
  color:
    primary: ["#2563eb (blue-600)", "#1d4ed8 (blue-700)"]
    neutral: ["#fff", "#f8fafc", "#0f172a"]
    accent: "#f59e0b (amber-500)"
    banned: ["gradients", "rainbow palettes", "multiple accent colors"]
  typography:
    families: ["Inter"]
    scale: [12, 14, 16, 20, 24]
    weights: [400, 500, 600]
    banned: ["system font stack", "display fonts", "monospace for UI"]
  density: compact  # sales reps scan fast, they don't read
  shape:
    radius: "4px"
    banned: ["rounded cards (12px+)", "circular containers"]
  tone:
    is: ["professional", "efficient", "data-driven"]
    is_not: ["playful", "friendly consumer", "decorative"]
  layout:
    uses: ["dense tables", "kanban", "slide-over panels", "compact headers"]
    rejects: ["hero sections", "card grids", "image-text rows"]
  motion: subtle
  hard_constraints:
    - "We never use circular icons with colored backgrounds for features"
    - "We never use illustrations"
    - "We never use full-page loading spinners"
    - "We never put decorative elements in the header"
```

## Product Understanding

CRM for sales teams at companies with 5-50 reps. Primary goal: help reps track deals and managers forecast revenue.

### Identity check: CRM dashboards typically show decorative charts — rejected by `tone: data-driven, is_not: decorative`. Our dense, compact identity forces a task-focused pipeline view over a widget dashboard.

## Anti-Pattern Prevention

**Dashboard Syndrome risk:** CRM dashboards typically show: total deals, conversion rate, avg deal size, activity volume, pipeline value, team performance. Most are decorative.

**Fix:** One metric that drives action: "Deals that need attention today." Everything else is a secondary view.

## Screen: Deal Pipeline

**Purpose:** Move deals through stages. Primary user action is dragging deals right.

**Primary action:** Update deal stage

**Secondary actions:** Add note, change value, change close date, assign to teammate

**Components:** Kanban board (columns = stages), deal cards (name, value, days-in-stage, next action), compact per-stage summary bar

**States:**
- Loading: skeleton board with column placeholders
- Empty: "Add your first deal" with import/demo data options
- Error: inline toast per failed operation (not full-page error)
- Success: optimistic update on stage change, subtle animation

**Design Rationale:**
- Kanban chosen because deal progression is inherently visual
- Cards show only 4 fields to keep scanning fast — details in slide-over
- Per-stage summary prevents needing a separate pipeline report

## Screen: Deal Detail (Slide-over)

**Purpose:** View and edit deal information without leaving pipeline view

**Primary action:** Edit deal field

**Components:** Activity timeline, key fields (value, stage, close date, contacts), notes, next-step reminder

**States:**
- Loading: inline skeleton for fields
- Empty activity: "Log your first call or email"
- Error: inline field-level error

## Screen: Activity Feed

**Purpose:** See recent team activity without digging

**Primary action:** Filter by person or deal

**Components:** Scrollable list with type icons (call, email, meeting, note), deal reference, timestamp

## Anti-Pattern Detection

**Card Grid Syndrome warning:** The Kanban board naturally uses cards. Mitigated by keeping cards minimal and using compact summary bars per column.

**Feature Dump warning:** A/B testing tools, email templates, reporting suite kept behind secondary nav — not on pipeline screen.

## Developer Handoff

**Component hierarchy:**
```
PipelinePage
├── StageColumn (multiple)
│   ├── StageHeader (name, total value, deal count)
│   └── DealCard
│       ├── DealName
│       ├── DealValue
│       ├── DaysInStage
│       └── NextActionBadge
├── DealSlideOver
│   ├── DealFields
│   ├── ActivityTimeline
│   └── NotesSection
└── ActivityFeed (optional side panel)
```

**Data requirements:**
- Deals: id, name, value, stage, closeDate, ownerId, contacts[], notes[]
- Activities: id, type, timestamp, dealId, userId, description
- Stages: id, name, order, probability

**State management:** Optimistic updates for stage changes. Undo within 5s. Polling for team activity feed.
