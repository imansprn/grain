# E-commerce Example (Web)

## Design Identity

```yaml
identity:
  name: Premium e-commerce store
  color:
    primary: ["#1a1a1a (near-black)", "#fff"]
    neutral: ["#fff", "#f5f5f5", "#737373", "#171717"]
    accent: "#eab308 (yellow-500)"
    banned: ["gradients", "rainbow accents", "bright primary colors"]
  typography:
    families: ["Inter"]
    scale: [12, 14, 16, 20, 24, 36]
    weights: [400, 500, 600]
    banned: ["more than one family", "rounded fonts"]
  density: spacious  # products need room to breathe
  shape:
    radius: "0px"
    banned: ["rounded product cards", "pill-shaped buttons"]
  tone:
    is: ["premium", "minimal", "editorial"]
    is_not: ["playful", "cheerful", "crowded", "discount-store"]
  layout:
    uses: ["full-width imagery", "asymmetric grids", "generous whitespace", "single-column mobile"]
    rejects: ["card grids with equal cards", "hero + subtitle + mockup", "rounded price tags"]
  motion: subtle
  hard_constraints:
    - "We never use stock photography"
    - "We never use rounded containers"
    - "We never use gradients"
    - "We never use popup newsletter signups"
    - "We never use 'limited time offer' urgency patterns"
```

## Product Understanding

E-commerce store selling physical goods. Primary user goal: find and purchase a product in minimum time.

## Anti-Pattern Prevention

**Feature Dump Syndrome risk:** Showing filters, categories, recommendations, reviews, promotions, and product details all at once.

**Fix:** Progressive disclosure. Search/category → product list → product detail → cart → checkout. Each screen shows only what's needed for that step.

## Screen: Product List

**Purpose:** Browse and narrow down to a specific product

**Primary action:** Select a product

**Secondary actions:** Filter, sort, add to cart (inline)

**Components:** Grid of product thumbnails, filter sidebar (collapsible), sort dropdown, pagination or infinite scroll

**States:**
- Loading: skeleton grid matching product aspect ratios
- Empty (no results): "No products found" with suggestions (broader category, remove filters)
- Error: retry with cached results if available
- Edge: 0 results after filter — show "Clear filters" prominently

**Design Rationale:** Grid chosen over list because products are visual. Filter sidebar is collapsible on desktop, slide-over on mobile. Sort defaults to relevance (not price) because most users browse, not compare.

## Screen: Product Detail

**Purpose:** Provide enough information to decide and buy

**Primary action:** Add to cart

**Secondary actions:** Select variant (size/color), view gallery, read reviews, share

**Components:** Image gallery (with zoom), variant selector, price + stock indicator, add-to-cart button (always visible), description, reviews section

**States:**
- Loading: skeleton with image placeholder, text lines
- Out of stock: greyed button with "Notify me" option
- Error on add-to-cart: inline error, item stays in local cart
- Unavailable variant: dimmed, showing "Currently unavailable"

## Screen: Cart

**Purpose:** Review and modify selections before purchase

**Primary action:** Proceed to checkout

**Secondary actions:** Update quantity, remove item, apply promo code, save for later

**Components:** Line items (image, name, variant, quantity, price), order summary (subtotal, shipping, tax, total), promo code field, checkout button

**States:**
- Empty: "Your cart is empty" with continue shopping link and personalized recommendations
- Saved for later: section below cart items

## Screen: Checkout

**Purpose:** Complete purchase

**Primary action:** Place order

**Components:** Multi-step form (shipping → payment → review), progress indicator, order summary sidebar

**States:**
- Validation: inline field errors, never full-page error
- Processing: button shows spinner, all fields disabled
- Success: order confirmation with order number and email preview
- Error: preserve entered data, show specific error (card declined → try another, address invalid → highlight field)

## Anti-Pattern Detection

**Form Hell warning:** Checkout forms typically ask for 12+ fields. Mitigated by: address autocomplete, saved payment methods, guest checkout option, smart defaults (same as shipping).

## Developer Handoff

**Component hierarchy:**
```
ProductListPage
├── FilterSidebar
│   ├── CategoryFilter
│   ├── PriceRangeFilter
│   └── RatingFilter
├── ProductGrid
│   └── ProductCard
│       ├── ProductImage
│       ├── ProductName
│       ├── ProductPrice
│       └── AddToCartButton
└── SortDropdown

ProductDetailPage
├── ImageGallery
├── VariantSelector
├── PriceDisplay
├── AddToCartButton (sticky bottom on mobile)
├── ProductDescription
└── ReviewSection
```

**Data requirements:**
- Products: id, name, description, images[], variants[], price, categoryId, rating, reviewCount, inStock
- Cart: items[], promoCode, subtotal
- Checkout: shipping fields, payment token, orderId

**Technical notes:**
- Cart persistence: localStorage for guest, API for logged-in
- Image optimization: responsive srcset, WebP, lazy loading
- Checkout: iframe or redirect for PCI-compliant payment processing
