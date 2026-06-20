# Analytics Dashboard Example (Web)

## Design Identity

```yaml
identity:
  name: B2B analytics platform
  color:
    primary: ["#6366f1 (indigo-500)", "#4f46e5 (indigo-600)"]
    neutral: ["#fff", "#f8fafc", "#94a3b8", "#1e293b"]
    accent: "#06b6d4 (cyan-500) for data highlights"
    semantic: ["#22c55e", "#ef4444", "#f59e0b"]
    banned: ["gradients on charts", "rainbow chart colors", "illustration colors"]
  typography:
    families: ["Inter"]
    scale: [11, 13, 15, 18, 22, 28]
    weights: [400, 500, 600]
    banned: ["rounded fonts", "serif", "monospace for UI"]
  density: compact  # data dashboards are dense by nature
  shape:
    radius: "4px"
    banned: ["pill shapes", "rounded card containers (12px+)"]
  tone:
    is: ["analytical", "precise", "data-first"]
    is_not: ["decorative", "playful", "salesy", "news-like"]
  layout:
    uses: ["fixed-width charts", "side-by-side panels", "dense table lists", "compact filters"]
    rejects: ["hero sections", "alternating image-text", "card grids of equal cards", "illustrations"]
  motion: subtle
  hard_constraints:
    - "We never show a chart that doesn't have a labeled axis"
    - "We never use 3D chart effects"
    - "We never use pie charts with more than 5 segments"
    - "We never show metrics without context (comparison period, target)"
    - "We never use stock illustrations"
```

## Product Understanding

Analytics platform for product managers at B2B SaaS companies. Primary goal: understand user behavior trends. Secondary: share reports with stakeholders.

**Identity check:** Analytics dashboards are the #1 dashboard syndrome victim. Our identity bans decorative charts, requires labeled axes, and forces compact density. This prevents the "pretty but useless" dashboard pattern.

## Anti-Pattern Prevention

**Dashboard Syndrome risk:** 12 widgets showing total users, new signups, MRR, churn rate, NPS score, feature usage, page views, session duration — all unrelated, all competing.

**Fix:** One question per page. "How is user growth trending?" → growth-focused page with cohort table, retention curve, signup source breakdown. "What features are used most?" → separate page with heatmap and usage tables. Never mix unrelated metrics.

## Screen: Growth Dashboard

**Purpose:** Answer "how is user acquisition and retention trending?"

**Primary action:** Filter by date range and segment

**Secondary actions:** Export chart as image, share report link

**Components:** Date range picker, segment filter (dropdown), retention curve chart (line), cohort retention table, signup sources bar chart (stacked), metric cards (4 max: new users, active users, retention rate, conversion rate)

**States:**
- Loading: skeleton chart areas with pulsing lines (not full-page spinner)
- Empty (no data for filter): "No data for this date range" with reset filter button
- Error: chart-specific error banner with retry
- Edge: partial data — show available data with data freshness indicator

**Design Rationale:**
- One question per page forces focus. A growth page answers growth questions. A feature usage page answers feature questions.
- Metric cards show only 4 numbers — enough to scan, few enough to remember
- Charts have labeled axes and tooltips — never decorative

## Screen: Feature Usage Heatmap

**Purpose:** See which features are adopted and where users drop off

**Primary action:** Click a cell to see user list for that feature/segment

**Components:** Heatmap grid (features × user segments), adoption rate % per cell, color intensity from identity palette, detail panel (slide-over)

**States:**
- Loading: skeleton heatmap grid
- Empty: no feature events recorded — "Integrate tracking to see feature usage"
- Error: inline error with retry per feature row

## Screen: Report Builder

**Purpose:** Create and share a report combining multiple charts

**Primary action:** Add chart to report

**Components:** Chart picker (available metrics), date range, layout grid (drag-to-arrange), title/description fields, share button

**States:**
- Empty: "Add your first chart to build a report"
- Saved: confirmation with link
- Error on save: inline error

## Anti-Pattern Detection

**Dashboard Syndrome:** Mitigated by one-question-per-page design. The "Growth Dashboard" answers only growth questions. No unrelated widgets.

**Card Grid Syndrome:** Charts are full-width or side-by-side, never in equal-sized card grid. Tables are dense, not wrapped in cards.

## Developer Handoff

**Component hierarchy:**
```
GrowthPage
├── PageHeader
│   ├── DateRangePicker
│   └── SegmentFilter
├── MetricCardsRow
│   └── MetricCard (label, value, trend, sparkline)
├── RetentionCurveChart
├── CohortTable
└── SignupSourcesChart

FeatureHeatmapPage
├── FilterBar
├── HeatmapGrid
│   └── HeatmapCell (feature, segment, adoption %)
└── DetailSlideOver

ReportBuilder
├── ChartPicker
├── ReportGrid
│   └── ReportBlock (chart, title, description)
└── SharePanel
```

**Data requirements:**
- Metrics: id, name, value, previousValue, change%, trend[]
- Cohorts: date, usersAdded, retentionDay1/7/30
- Feature heatmap: featureId, segmentId, adoptionRate, userCount
- Reports: id, title, description, blocks[], sharedWith[], createdAt

**Technical notes:**
- Charts render server-side or with WebGL (not SVG for large datasets)
- CSV export for all tabular data
- Report links are permission-gated, not public
- Date ranges are pre-computed for common periods (7d, 30d, 90d, custom)
