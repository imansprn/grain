# Fitness Tracking Example (Mobile)

## Design Identity

```yaml
identity:
  name: Mobile fitness tracker
  color:
    primary: ["#7c3aed (violet-600)", "#6d28d9 (violet-700)"]
    neutral: ["#fff", "#faf5ff", "#374151", "#111827"]
    accent: "#f97316 (orange-500) for streak/progress highlights"
    semantic: ["#22c55e (goal met)", "#f59e0b (almost there)", "#ef4444 (missed)"]
    banned: ["medical greens and blues", "dark themes", "corporate flat grays"]
  typography:
    families: ["Inter"]
    scale: [12, 14, 16, 20, 28, 40]
    weights: [400, 500, 700]
    banned: ["monospace", "more than one family", "thin weights"]
  density: moderate  # comfortable touch targets, not cramped
  shape:
    radius: "12px"
    banned: ["sharp 0px corners on interactive elements", "pill buttons"]
  tone:
    is: ["motivational", "energetic", "personal", "human"]
    is_not: ["corporate", "medical", "clinical", "competitive"]
  layout:
    uses: ["full-bleed hero numbers", "horizontal scrolling metrics", "list feeds", "modal sheets"]
    rejects: ["data tables", "desktop-style dashboards", "calendar grids"]
  motion: expressive
  hard_constraints:
    - "We never show calories in red (associates food with punishment)"
    - "We never show leaderboards (competitive fitness increases anxiety)"
    - "We never use medical terminology (METs, VO2 max without explanation)"
    - "We never show numbers without context ('5,000 steps' → '5,000 / 10,000 goal')"
    - "We never hide the main metric behind a tap"
```

## Product Understanding

Mobile fitness tracker for casual to intermediate users (not athletes). Primary goal: maintain daily activity habit. Secondary: see progress over time.

**Identity check:** Fitness apps default to medical-green clinical or leaderboard-competitive. Our identity bans both — the violet/orange palette, motivational tone, and expressive motion create a personal coach feel, not a medical device.

## Screen: Today (Home)

**Purpose:** See today's activity and take one action

**Primary action:** Log an activity

**Secondary actions:** View step count, view heart rate, start a workout

**Components:** Large ring progress (steps toward goal), highlighted stat (steps / active minutes / distance), recent activity feed (auto-logged and manual), quick-start workout button (prominent, bottom position for thumb zone)

**States:**
- Loading: skeleton ring and stat placeholders (no full-screen spinner)
- Empty (new user): "Start your first walk to see activity here" with CTA
- Error (no sensor data): "Enable health permissions in Settings" with deep-link
- Goal reached: ring shows completion animation (violet pulse, 1s, not blocking)
- Late day / below goal: subtle orange accent on progress, no guilt messaging

**Design Rationale:**
- Ring chart is universally understood for goal progress — no labels needed
- Primary metric is always visible without scrolling (identity constraint)
- Workout button at bottom for thumb reach (mobile-specific)
- No leaderboards or social comparison (hard constraint)

## Screen: Activity Log

**Purpose:** Review and edit past activities

**Primary action:** Tap an activity to edit or delete

**Components:** Grouped list (by day), each row: activity type icon + name, duration, calories, time. Pull-to-refresh.

**States:**
- Loading: skeleton rows
- Empty: "Log your first activity" with suggestion cards (walk, run, yoga)
- Error: cached list with stale data indicator
- Pending sync (watch data): grey badge with "Syncing..."

## Screen: Trends

**Purpose:** See progress over days and weeks

**Primary action:** Change view period (week / month / 3 months)

**Components:** Segmented control (period), bar chart (daily steps), line overlay (7-day avg), summary metrics below (avg steps, streak count, best day), share button (export as image)

**States:**
- Loading: skeleton chart area
- Insufficient data: "More data needed — keep logging to see trends" with preview
- Error: inline error with retry

## Screen: Workout Detail

**Purpose:** Log or review a specific workout

**Primary action:** Start workout (pre-workout) / Save (post-workout)

**Components:** Activity type picker (scrollable icon grid), duration picker (wheel), intensity slider, notes field, start button (full width, filled)

**States:**
- Pre-workout (logging manually): form state
- Recording: live timer, pause/end buttons, heart rate display
- Post-workout: summary with map (if GPS), save/discard options

## Anti-Pattern Detection

**Dashboard Syndrome:** Only one metric shown on home — step progress toward goal. No multi-widget layout.

**Form Hell:** Activity logging reduced to activity type + duration + intensity. Optional notes. 3 fields, not 10.

**Card Grid Syndrome:** Feed uses list rows, not cards. Chart is full-width, not in a card.

## Developer Handoff

**Component hierarchy:**
```
App
├── TodayScreen
│   ├── ProgressRing (goal %, animated)
│   ├── MetricHighlight (steps / active min / distance)
│   ├── ActivityFeed
│   │   └── ActivityRow (icon, name, duration, time)
│   └── StartWorkoutButton (prominent, bottom)

├── ActivityLogScreen
│   ├── CalendarScrubber (optional)
│   ├── ActivityGroup (day header + rows)
│   └── SyncStatusIndicator

├── TrendsScreen
│   ├── PeriodSelector
│   ├── StepsChart
│   ├── TrendSummary
│   └── ShareButton

└── WorkoutDetailScreen
    ├── ActivityTypePicker
    ├── DurationPicker
    ├── IntensitySlider
    ├── NotesInput
    └── PrimaryButton
```

**Data requirements:**
- Daily activity: date, steps, activeMinutes, distance, heartRate[], workouts[]
- Workouts: id, type, startTime, duration, calories, heartRate[], route[] (GPS)
- Goals: type, target, period (daily/weekly), current
- Trends: period aggregates (avg steps, totals, streaks)

**Native features:**
- HealthKit / Google Fit integration for passive data
- Workout session with live timer (keep phone awake)
- GPS route tracking (background updates)
- Watch companion app for wrist-based workout start
- Live activities / notifications for goal milestones

**Motion notes:**
- Expressive motion (identity setting)
- Ring completion: violet pulse + haptic feedback
- Chart transitions: spring-based (not linear)
- Screen transitions: slide-up sheets (not push)
