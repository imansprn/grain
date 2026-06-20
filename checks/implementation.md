# Implementation Checklist

Stack-specific pitfalls that cause slop or breakage in production. Generic engineering practices (API error handling, CSRF, bundle size) belong in your project's engineering standards, not here.

## Universal UI Requirements

- [ ] Every displayed value has an identified data source — no placeholder text in production paths
- [ ] Loading, empty, and error states handled at component level (not page level)
- [ ] List virtualization for any list that can exceed ~50 items
- [ ] Skeleton screens per-section, not full-page spinner
- [ ] Responsive behavior defined at 375px, 768px, 1280px minimum
- [ ] Token references only — no inline hex values, hardcoded font sizes, or magic spacing numbers

---

## React / Next.js (App Router)

- [ ] `'use client'` only where state/events are needed — not applied globally
- [ ] `loading.tsx` and `error.tsx` defined for all dynamic routes
- [ ] `next/image` for all images (automatic WebP, responsive srcset)
- [ ] `next/font` for all fonts (no external font requests at runtime)
- [ ] Client state that must survive navigation is in URL search params or a store, not React state
- [ ] Suspense boundaries for any long-loading server component

## React / Next.js (Pages Router)

- [ ] `getStaticProps` / `getServerSideProps` chosen deliberately per route — not defaulting to SSR for everything
- [ ] `next/image` and `next/font` used

## Compose Multiplatform / Jetpack Compose

- [ ] Side effects (`LaunchedEffect`, `DisposableEffect`) scoped to the right key — avoid infinite recomposition
- [ ] `rememberSaveable` for state that must survive config changes; `remember` for transient state
- [ ] `ScreenModel` / `ViewModel` is the only place with `coroutineScope` — no coroutines inside composables
- [ ] `StateFlow` collected via `collectAsState()` — not `Flow.collect` in `LaunchedEffect` unless intentional
- [ ] Keyboard shortcuts registered in `DisposableEffect` (cleaned up on composition exit)
- [ ] `Modifier.fillMaxWidth()` inside lazy columns — never `fillMaxSize()` on lazy column items
- [ ] All text uses project typography tokens — no hardcoded `fontSize` values

## SwiftUI

- [ ] `@StateObject` owns the object lifetime; `@ObservedObject` for injected objects — not swapped
- [ ] Async work in `.task {}` modifier or `onAppear` — not `DispatchQueue.main.async`
- [ ] `NavigationStack` + `navigationDestination` (not deprecated `NavigationView`)
- [ ] `@AppStorage` / `@SceneStorage` for lightweight persistence — not raw `UserDefaults`

## Flutter

- [ ] `const` constructors used wherever widgets don't depend on runtime data
- [ ] `mounted` guard before using `BuildContext` after `await`
- [ ] Platform-adaptive widgets where available (`adaptive` constructors)
- [ ] Routing via `go_router` consistently — no mixing with `Navigator.push`
- [ ] `ThemeData` tokens for all colors and text styles — no hardcoded values in widget files
