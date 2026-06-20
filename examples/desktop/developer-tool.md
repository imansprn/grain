# Developer Tool (Desktop) — Example

**Based on:** GOST Desktop — a Compose Multiplatform (JVM) GUI for managing a local GOST proxy binary.

This example covers the design decisions and anti-pattern traps specific to power-user desktop tools that manage a local daemon, process, or service.

---

## Design Identity

```yaml
identity:
  name: GOST Desktop
  color:
    base: "#040A12 (near-black navy)"
    surface: "#0C141E (dark slate)"
    input: "#162032 (deep blue-grey)"
    selection: "#0D2A3A (selected state)"
    accent_primary: "#00E5FF (cyan-bright)"
    accent_secondary: "#007AFF (blue-bright)"
    semantic:
      running: "#00E5FF (cyan)"       # process is active
      idle: "textSecondary"           # process stopped
      error: "#FF3D00 (neon red)"
      warning: "#FFD600 (amber)"
    borders: "rgba(255,255,255,0.15)"
    banned: ["warm tones", "beige", "gradients (decorative)", "illustrations", "pastel accents"]
  typography:
    families: ["JetBrains Mono (primary)", "system-ui fallback"]
    scale: [11, 12, 13, 14, 16, 20]
    weights: [400, 500, 700]
    banned: ["serif", "display fonts", "multiple families", "web fonts requiring network fetch"]
  density: compact        # maximum controls per screen, no decorative spacing
  shape:
    radius: "4px (inputs, cards)"
    sidebar_items: "4px"
    badges: "2px"
    banned: ["circular containers", "pill shapes", "heavy shadows"]
  tone:
    is: ["technical", "utilitarian", "precise", "power-user"]
    is_not: ["friendly", "consumer", "editorial", "marketing"]
  layout:
    uses: ["sidebar + main area (Workbench)", "compact list rows", "inline forms", "status badges"]
    rejects: ["hero sections", "card grids", "alternating feature rows", "modal-heavy flows"]
  motion: still           # M1 — no decorative transitions, only functional feedback
  hard_constraints:
    - "Always dark. Light scheme is not user-reachable."
    - "No confirmation dialogs for non-destructive actions (start/stop tunnel)."
    - "Status badges (RUNNING / IDLE / ERROR) are never animated."
    - "No rounded pill shapes anywhere."
    - "Sidebar never collapses to icon-only without keyboard shortcut."
  dials: "V3 M1 D9"
```

**Why this identity:** Users spend hours in this app managing proxy tunnels. Cognitive load from color variety, motion, or decorative whitespace compounds into fatigue. The dark + mono identity signals "this is a tool" immediately, sets expectations, and keeps every visual element functional.

---

## Product Understanding

GOST Desktop spawns and supervises child processes (GOST binary instances) per service. The user's primary jobs:

1. Define tunnel services (address, port, chain, auth)
2. Start / stop them
3. Read logs when something breaks
4. Configure GOST binary path and settings

This is a **management console**, not a dashboard. Users are not monitoring — they are operating. Design for action, not observation.

---

## Anti-Pattern Prevention

### Dashboard Syndrome risk
Large status numbers, charts, animated indicators, overview widgets. None of these help a user start a broken tunnel.

**Fix:** No dashboard screen. Default route is `services` — the list where the user acts. Overview data (running count) lives in the sidebar, not on its own screen.

### Card Grid risk
Power-user tools often turn service lists into card grids. Cards use 3–4× the vertical space of a compact row.

**Fix:** Compact list rows. Each service row: status dot + name + address:port + start/stop button. Full width, single height. Click to expand inline for details.

### Empty State as Landing Page
An empty state with a big illustration and "Create your first tunnel!" is a marketing pattern. Users who installed this app know what it is.

**Fix:** Empty state is minimal — a single text label and a "+ New Tunnel" button. Same visual weight as a filled row, not a full-bleed illustration.

---

## Macrostructure: Workbench (Structure 6)

```
┌─────────────────────────────────────────────────────┐
│  Sidebar (N3)    │  Main content area               │
│  ─────────────   │  ──────────────────────────────  │
│  Tunnels (1)     │  [Search bar]  [+ New Tunnel]    │
│  Chains (2)      │  ─────────────────────────────   │
│  Authers (3)     │  ● SERVICE_A   0.0.0.0:8080  ▶  │
│  Advanced (4)    │  ● SERVICE_B   :1080         ■  │
│  Logs (5)        │  ○ SERVICE_C   :7070         ▶  │
│  Config (6)      │                                  │
│  ─────────────   │                                  │
│  Settings        │                                  │
└─────────────────────────────────────────────────────┘
```

Sidebar selection replaces the main area (REPLACE, not PUSH). Wizard forms push onto the stack (PUSH). Escape pops.

---

## Screen: Services (Tunnels) — Primary

**Purpose:** View all configured tunnel services, start/stop them, create new ones.

**Primary action:** Start or stop a service

**Secondary actions:** Create new service, search/filter, open logs for a service, edit service config

**Components:**
- Compact list rows: status indicator (color dot) + service name (monospace) + address + start/stop button
- Search bar (Cmd+F focuses it)
- "+ New Tunnel" button (Cmd+N)
- Inline error expansion: when status is ERROR, row expands to show last error line from log

**States:**

| State | Treatment |
|-------|-----------|
| Empty (no services) | One-line empty message + "+ New Tunnel" text button. No illustration. |
| Loading (initializing) | Skeleton rows matching the row height. No full-page spinner. |
| Service RUNNING | Cyan status dot. Stop button visible. |
| Service IDLE | Muted status dot. Start button visible. |
| Service ERROR | Red status dot. Row expands inline with last error line. Start button remains. |
| Search active, no results | Inline "No match for '{query}'" below search bar. Clear button. |
| Network/binary missing | Banner at top: "GOST binary not found — go to Settings." Start buttons disabled. |

**Design Rationale:**
- Status dot is the primary visual signal — users scan for it, not for the service name
- Start/stop is in the row, not behind a detail view — reduces interaction cost from 2 clicks to 1
- Error expansion is inline because opening a modal for a one-line error is overhead

---

## Screen: Service Form (Wizard) — New / Edit

**Purpose:** Define a tunnel service (name, listener address, forwarder target, chain, auth).

**Primary action:** Save service

**Route behavior:** PUSH onto stack from services. Escape pops back without saving. Cmd+S saves.

**Components:**
- Form fields: Name (validated `^[a-zA-Z0-9_-]+$`), Listener type, Address/port, Forwarder target, Chain (dropdown from ChainRegistry), Auth (dropdown from AutherRegistry)
- Live validation: inline errors after field blur, not on submit
- Save button (Cmd+S), Cancel link (Escape)
- "Preview config" toggle: shows the generated GOST JSON without leaving the form

**States:**

| State | Treatment |
|-------|-----------|
| New (empty form) | All fields empty. Name field has keyboard focus. |
| Editing existing | Fields pre-filled. Title bar shows "Edit SERVICE_NAME". |
| Invalid name | Inline error: "Name must match [a-zA-Z0-9_-]". Field outline turns red. |
| Duplicate name | Inline error: "A service with this name already exists." |
| Saving | Save button shows "Saving…" and is disabled. Spinner inside button only. |
| Save success | Pop back to services list. Row for new service appears with IDLE status. |
| Save error | Inline banner below form: error message. No modal. |

**Design Rationale:**
- Name validation is critical because GOST config filenames use the name — invalid characters cause file system errors that surface as opaque errors later
- "Preview config" is a power-user feature; it lets advanced users verify the generated JSON without leaving the workflow

---

## Screen: Logs

**Purpose:** Tail stdout/stderr for all running services. Debug tunnel failures.

**Primary action:** Read log output. Filter by service.

**Components:**
- Service filter tabs (All / per service)
- Monospace log output (auto-scroll when at bottom, pauses on scroll up)
- Search/highlight field (Cmd+F)
- "Scroll to bottom" button (appears when paused)
- Clear button (clears in-memory buffer)

**States:**

| State | Treatment |
|-------|-----------|
| No services running | "No running services. Start a tunnel to see logs." Center-aligned one-liner. |
| Log output | Auto-scrolling monospace terminal. Timestamps muted, log text primary. |
| Paused (user scrolled up) | Auto-scroll paused. "↓ Live" button appears fixed at bottom. |
| Search active | Matching lines highlighted with amber background. Non-matching lines dimmed. |

---

## Screen: Connection (First-Run / Binary Missing)

**Purpose:** Prompt user to set the GOST binary path. Shown when `isRuntimeValid == false`.

**Primary action:** Set binary path (file picker or manual entry)

**Notes:** This is a gate, not an onboarding flow. Users who installed this app are technical — they don't need a tutorial. They need a file picker.

**Design Rationale:**
- No illustration, no step counter, no "Welcome to GOST Desktop!" heading
- One instruction, one input, one button
- If the binary is found and valid, navigate immediately to services without a success state

---

## Identity Coherence Check

Risks for this identity:

| Risk | Check |
|------|-------|
| Warm accent creeping in | All accents must be cyan (`#00E5FF`) or blue (`#007AFF`). Amber only for warnings. |
| Card-style service items | Rows must stay rows. No `elevation`, no card background, no rounded card containers. |
| Decorative motion | Any `animate*` call needs a functional reason. No entrance animations. |
| Light mode bleed | `darkTheme = true` in `App.kt`. Never read `isSystemInDarkTheme()` for the dark/light decision. |
| Rounded pill badges | Status badges use `4px` radius, never `.clip(CircleShape)` or `RoundedCornerShape(50%)`. |

---

## Developer Handoff

**Component hierarchy:**
```
App
├── ConnectionScreen          (shown if isRuntimeValid == false)
└── MainAppContent
    ├── Sidebar (N3)
    │   ├── SidebarItem × 6   (nav + Cmd+1-6)
    │   └── SettingsItem       (Cmd+,)
    └── ScreenHost (stack-driven)
        ├── ServicesScreen
        │   ├── SearchBar
        │   ├── ServiceList
        │   │   └── ServiceRow × n
        │   │       ├── StatusDot
        │   │       ├── ServiceName + Address
        │   │       ├── StartStopButton
        │   │       └── InlineErrorExpansion (conditional)
        │   └── EmptyState (conditional)
        ├── ServiceFormScreen
        │   ├── NameField
        │   ├── ListenerTypeSelector
        │   ├── AddressField
        │   ├── ForwarderField
        │   ├── ChainSelector
        │   ├── AuthSelector
        │   ├── ConfigPreviewToggle
        │   └── SaveButton + CancelLink
        ├── LogsScreen
        │   ├── ServiceFilterTabs
        │   ├── LogOutput (auto-scroll)
        │   ├── SearchField
        │   └── ScrollToBottomButton (conditional)
        └── SettingsScreen
```

**Token usage:**
```kotlin
// Correct — always via GostSemantics
val colors = GostSemantics.colors
Surface(color = colors.surfacePanel) { ... }
Text(text = name, color = colors.textPrimary, style = GostTextStyles.bodyMono)

// Wrong — hardcoded or raw MaterialTheme
Surface(color = Color(0xFF0C141E)) { ... }
Text(color = MaterialTheme.colorScheme.onSurface) { ... }
```

**State management:**
- `ServicesScreenModel` collects `ServiceRegistry.services: StateFlow<List<ServiceEntity>>`
- Start/stop calls `ProcessManager` directly from ScreenModel — no intermediate event bus
- Log output collects `ProcessManager.logs: SharedFlow<LogEvent>` in `LogsScreenModel`
- Singleton access: always via `Foo.default()` — never construct singletons directly in composables
