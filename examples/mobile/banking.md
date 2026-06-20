# Mobile Banking Example (Mobile)

## Design Identity

```yaml
identity:
  name: Retail mobile banking
  color:
    primary: ["#1e3a5f (dark navy)", "#fff"]
    neutral: ["#fff", "#f8f9fa", "#495057", "#212529"]
    accent: none
    semantic: ["#2b8a3e (success)", "#c92a2a (error)"]
    banned: ["gradients", "bright colors", "illustration palettes", "multiple accents"]
  typography:
    families: ["SF Pro"]
    scale: [12, 14, 16, 20, 24, 32]
    weights: [400, 500, 600]
    banned: ["more than one family", "monospace for UI", "light below 14px"]
  density: spacious  # banking needs clarity, not density
  shape:
    radius: "8px"
    banned: ["0px radius on interactive elements", "circular buttons"]
  tone:
    is: ["trustworthy", "calm", "professional", "secure"]
    is_not: ["playful", "exciting", "crowded", "urgent"]
  layout:
    uses: ["list-based navigation", "card summary", "full-screen forms", "bottom sheets"]
    rejects: ["dashboards with charts", "hero sections", "gamification elements"]
  motion: subtle
  hard_constraints:
    - "We never use gradient backgrounds"
    - "We never use illustrations of people"
    - "We never show charts on the home screen"
    - "We never use urgency messaging ('act now', 'limited time')"
    - "We never hide the balance behind a tap"
```

## Product Understanding

Mobile banking app for retail customers. Primary user goal: check balance, pay bills, transfer money. Secondary: deposit checks, manage cards, view transaction history.

## Anti-Pattern Prevention

**Dashboard Syndrome risk:** Full-screen charts of spending patterns, investment performance, credit score, and budgeting all competing on the home screen.

**Fix:** Home screen shows exactly: account balances + recent transactions. That's what users open the app for 90% of the time. Everything else is behind navigation.

## Screen: Home

**Purpose:** See available money and recent activity at a glance

**Primary action:** Check balance

**Secondary actions:** View transaction details, initiate transfer or payment

**Components:** Account cards (account name, balance, masked number), recent transactions list (5-10 items), quick actions row (transfer, pay, deposit)

**States:**
- Loading: skeleton cards matching account card dimensions
- Error (offline): show cached balances with "Last updated X min ago" and offline indicator
- Empty (new user): "Link your first account" CTA
- Low balance: subtle yellow highlight on balance, no alarmist messaging

**Design Rationale:**
- Balance shown immediately on open — no tap required. Users check balances dozens of times daily.
- Quick actions below the fold — transfers and payments are less frequent than balance checks.
- No charts. Spending analysis belongs in a separate screen, not the home view.

## Screen: Transfer

**Purpose:** Move money between accounts or to external recipients

**Primary action:** Send money

**Components:** From account picker (default: primary checking), To field (recent recipients + search), Amount input (with number pad, not text input), date picker (scheduled transfers), memo field (optional), review step, confirm button

**States:**
- Empty (no accounts): "Add an account first"
- Insufficient funds: inline warning, amount field shows red, confirm button disabled
- Adding new recipient: slide-over form with account/routing validation
- Processing: spinner on confirm button, input fields locked
- Success: confirmation screen with receipt details and "Share receipt" option
- Error: specific message (insufficient funds, recipient account invalid, daily limit exceeded)

## Screen: Transactions

**Purpose:** Review all account activity

**Primary action:** View transaction detail

**Secondary actions:** Filter by date/category/amount, search, export

**Components:** Grouped list (by date), each row showing: merchant/description, amount (+/-), date, category icon. Pull-to-refresh.

**States:**
- Loading: skeleton rows
- Empty: no transactions message
- Error: cached list with banner
- Pending transactions: shown with pending badge (grey/italic)

## Screen: Transaction Detail

**Purpose:** See full transaction information and take action if needed

**Components:** Amount (large), merchant, date, status, category, receipt image (if available), actions: dispute, add receipt, add note, categorize

## Anti-Pattern Detection

**Confirmation Overuse risk:** Banks confirm everything. "Are you sure you want to send $50?" after the user already confirmed on the review step. Fix: one confirmation on review screen. No double confirmations.

**Empty State Neglect:** Most banking apps show nothing when there are no transactions. Fix: "No transactions this period" with a link to adjust filters or date range.

## Design Rationale

**Decision:** Show balances immediately on home screen without authentication on open (with masking toggle).

**Reason:** Checking balance is the most frequent task. Requiring authentication adds friction. The app supports biometric auth for transactions.

**Alternatives:** Balance hidden behind tap (rejected — adds step to most common action), balance on lock screen widget (not implemented — security concern).

**Tradeoffs:** Slightly less privacy if phone is unlocked. Mitigated by: masking option, biometric auth for all money movement.

## Developer Handoff

**Component hierarchy:**
```
App
├── HomeScreen
│   ├── AccountCardCarousel
│   │   └── AccountCard (name, balance, masked number)
│   ├── QuickActionsRow
│   │   ├── TransferButton
│   │   ├── PayButton
│   │   └── DepositButton
│   └── RecentTransactionsList
│       └── TransactionRow (merchant, amount, date, categoryIcon)
├── TransferScreen
│   ├── AccountPicker
│   ├── RecipientInput
│   ├── AmountInput
│   ├── DatePicker
│   ├── ReviewStep
│   └── ConfirmButton
├── TransactionHistoryScreen
│   ├── FilterBar
│   ├── TransactionGroup
│   └── TransactionRow
└── TransactionDetailScreen
    ├── AmountDisplay
    ├── MerchantInfo
    ├── StatusBadge
    └── ActionRow (dispute, add receipt, etc.)
```

**Data requirements:**
- Accounts: id, name, type, balance, availableBalance, currency, maskedNumber
- Transactions: id, accountId, amount, currency, merchant, description, date, status, category, receiptUrl
- Transfers: fromAccountId, toAccountId, toExternalId, amount, date, memo, status
- Recipients: id, name, accountNumber, routingNumber, accountType, bankName

**Security notes:**
- Biometric auth for all money movement
- Session timeout on background
- No sensitive data in push notification payloads
- Rate limiting on transfer attempts
- Daily transfer limits enforced client-side and server-side
