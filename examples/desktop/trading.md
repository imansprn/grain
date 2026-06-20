# Trading Platform Example (Desktop)

## Design Identity

```yaml
identity:
  name: Active trading platform
  color:
    primary: ["#059669 (emerald-600)", "#047857 (emerald-700)"]
    neutral: ["#fafafa (neutral-50)", "#1a1a2e (dark navy)", "#e2e8f0 (slate-200)"]
    accent: "#f97316 (orange-500) for warnings"
    semantic: ["#22c55e (buy)", "#ef4444 (sell)"]
    banned: ["gradients", "decorative colors", "illustration palettes"]
  typography:
    families: ["JetBrains Mono"]
    scale: [10, 12, 14, 16, 20]
    weights: [400, 500, 700]
    banned: ["serif", "display fonts", "multiple families"]
  density: compact  # maximum data per screen
  shape:
    radius: "0px"
    banned: ["rounded corners", "circular elements"]
  tone:
    is: ["technical", "precise", "cold"]
    is_not: ["friendly", "decorative", "consumer app"]
  layout:
    uses: ["dense tables", "fixed panels", "side-by-side layouts", "compact order entry"]
    rejects: ["hero sections", "card grids", "alternating rows", "illustrations"]
  motion: still
  hard_constraints:
    - "We never use rounded corners"
    - "We never use illustrations or icons"
    - "We never use gradients"
    - "We never use confirmation dialogs for order submission"
    - "We never use full-page loading"
```

## Product Understanding

Browser-based platform for active retail traders executing 10-100+ trades daily. Primary user goal: execute trades fast with minimal errors.

## Anti-Pattern Prevention

**Dashboard Syndrome risk:** Portfolio value charts, market overviews, news feeds, and watchlists all competing for attention.

**Fix:** Default view is the order entry screen. Everything else is a side panel. A trader's primary job is entering orders, not watching charts.

## Screen: Order Entry (Primary)

**Purpose:** Execute trades. Speed is safety — fast execution means less slippage.

**Primary action:** Submit buy/sell order

**Secondary actions:** Switch order type (market/limit/stop), set quantity, set price, view position

**Components:** Instrument selector (search + top picks), order type tabs, quantity input (with preset % options), price input (with bid/ask price buttons), buy/sell buttons (green/red, large), position summary, order book depth (compact)

**States:**
- Loading: instrument data skeleton
- Market closed: greyed buy/sell, shows next session open time
- Insufficient funds/positions: inline warning, quantity auto-adjusts
- Order submitted: confirmation toast with order ID, option to cancel (if cancellable)
- Order rejected: specific reason (insufficient funds, market closed, invalid price)
- Network disconnected: prominent banner, cached data shown, queued orders held

**Design Rationale:**
- Buy/sell buttons are the largest elements — they are the primary action
- Price inputs show bid/ask as clickable buttons (saves typing, prevents fat-finger)
- Quantity presets (25%, 50%, 75%, 100%) reduce typing and cognitive load during fast markets
- Order book depth is compact (best 5 bids/asks) — full depth is a separate screen

## Screen: Positions & Orders

**Purpose:** Monitor open positions and active/queued orders

**Primary action:** Close position or cancel order

**Components:** Two tabs: Open Positions (instrument, side, qty, entry price, current price, P&L, close button), Open Orders (instrument, side, type, price, qty, filled, cancel button)

**States:**
- No positions: empty state shows "Your positions will appear here"
- Position in profit/loss: green/red P&L, no flashing or animations
- Order partially filled: show filled vs total quantity

## Screen: Trade History

**Purpose:** Review past trades for analysis and tax reporting

**Primary action:** Filter by date range or instrument

**Components:** Scrollable table (date, instrument, side, qty, price, total, P&L), export button, search/filter

## Anti-Pattern Detection

**Card Grid Syndrome risk:** Trading platforms put everything in cards. Fix: dense tables. Traders scan vertically, not in grid patterns.

**Confirmation Overuse risk:** "Are you sure?" on every order is dangerous in fast markets. Fix: no confirmation for market/limit orders. One-click trade execution. Confirmation only for order cancellation if position is significant.

## Design Rationale

**Decision:** No confirmation dialog on order submission.

**Reason:** In active trading, 500ms delay can cost money. Accidental trades are prevented by the two-button design (select instrument + click buy/sell).

**Alternatives:** Confirmation dialog (rejected — causes slippage), click-and-confirm (rejected — two-step adds no safety over buy/sell buttons).

**Tradeoffs:** Slightly higher risk of fat-finger trades. Mitigated by: undo window (3s cancel), position limits configurable per account.

## Developer Handoff

**Component hierarchy:**
```
TradePage
├── InstrumentSelector
├── OrderPanel
│   ├── OrderTypeTabs (Market | Limit | Stop)
│   ├── QuantityInput
│   │   └── QuantityPresets (25%, 50%, 75%, 100%)
│   ├── PriceInput
│   │   └── BidAskButtons
│   └── BuySellButtons
├── PositionSummary (compact)
├── OrderBookDepth (best 5)
├── ActivityPanel (tabs)
│   ├── PositionsTab
│   ├── OrdersTab
│   └── HistoryTab
└── ConnectionStatus
```

**Data requirements:**
- Instruments: symbol, name, lastPrice, bid, ask, volume, sessionStatus
- Orders: id, instrument, side, type, price, quantity, filledQuantity, status, timestamp
- Positions: id, instrument, side, quantity, entryPrice, currentPrice, P&L
- Trade history: date, instrument, side, quantity, price, total, fees, P&L

**State management:**
- WebSocket connection for real-time prices (reconnect with exponential backoff)
- Local queue for orders during network interruption
- Optimistic position updates (reconcile on confirmation)
- Undo window: 3s after order fill to submit cancel
- Connection status: indicator in header, never blocking
