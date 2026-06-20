#!/usr/bin/env python3
"""Deterministic anti-slop linter for product-ui-architect.

Usage:
    python3 lint.py <path>                    # scan file or directory (text output)
    python3 lint.py <path> --format json      # JSON output (machine-readable)
    python3 lint.py <path> --format json --exit-code  # JSON + non-zero exit on findings

Exit codes:
    0 — no findings
    1 — Critical/High findings
    2 — Medium findings only
"""

import json
import os
import re
import sys
from pathlib import Path

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}

RULES = [
    {
        "id": "magic_color_literal",
        "name": "Inline Color Value Outside Theme",
        "severity": "high",
        "category": "visual",
        "patterns": [
            r"Color\(0x[0-9A-Fa-f]{6,10}\)",
        ],
        "exclude_paths": [r"/theme/", r"Colors\.kt$", r"Palette\."],
        "message": "Inline color value outside theme file. Must reference project token system.",
    },
    {
        "id": "commented_out_code",
        "name": "Commented-Out Code Block",
        "severity": "medium",
        "category": "maintainability",
        "patterns": [
            r"(//|#|<!--)\s*(var|val|fun|def|function|class|struct|enum|import|const|let|private|public|override)\s",
            r"(//|#)\s*\{/[*!].{50,}\}",
        ],
        "message": "Commented-out code found. Remove dead code — version control preserves history.",
    },
    {
        "id": "hardcoded_sample_name",
        "name": "Hardcoded Sample Data Name",
        "severity": "medium",
        "category": "content",
        "patterns": [
            r"\b(Name|name)[:\s]+\"(Alice|Bob|Charlie|David|Emma|Frank|Grace|Henry)\"",
            r"\"(John|Jane)\s+(Doe|Smith|Brown)\"",
        ],
        "message": "Hardcoded sample name detected. Replace with real data or an honest placeholder.",
    },
    {
        "id": "gradient_unmotivated",
        "name": "Unmotivated Gradient",
        "severity": "high",
        "category": "visual",
        "patterns": [
            r"linear-gradient\s*\(",
            r"radial-gradient\s*\(",
        ],
        "message": "Gradient found. Must reference identity — if unmotivated by brand, remove.",
        "exclude_patterns": [r"\.dark\s", r"data-theme\s*=\s*[\"']dark[\"']"],
        "exclude_paths": [r"node_modules/", r"/dist/", r"/\.next/", r"/build/", r"/out/"],
    },
    {
        "id": "template_hero",
        "name": "Template Hero (dual CTA)",
        "severity": "high",
        "category": "layout",
        "patterns": [
            r"(Get Started|Learn More|Sign Up Free|Try Free|Watch Demo).{0,100}(Get Started|Learn More|Sign Up Free|Try Free|Watch Demo)",
        ],
        "message": "Two CTA buttons found near each other. Template hero pattern — consider a single primary CTA.",
    },
    {
        "id": "fabricated_metrics",
        "name": "Fabricated Metrics",
        "severity": "critical",
        "category": "content",
        "patterns": [
            # Only match prose/copy contexts: percent + marketing word (not bare CSS percentages)
            r"\b\d{2,3}\s*%\s+(faster|better|more efficient|increase|growth|conversion|efficiency)\b",
            r"(trusted by|used by|loved by)\s+\d{2,}(K|k|\+|,)\s*(\+|more\s+than)?\s*(users?|teams?|companies?|customers?)\b",
            r"\d[\d,]*\s*\+?\s*(countries|cities|locations)\s+around\b",
            r"\d+(\.\d)?\s*/\s*5\s+(stars?|rating|score)\b",
            r"\b\d{2},\d{3}\s*\+\s*(users?|reviews?|downloads?)\b",
        ],
        "message": "Fabricated metric detected — user did not supply this data. Remove or mark as placeholder.",
        "exclude_patterns": [r"(placeholder|TODO|FIXME|demo|sample)"],
        "exclude_paths": [r"node_modules/", r"/dist/", r"/\.next/", r"/build/", r"/out/"],
    },
    {
        "id": "three_step_process",
        "name": "Three-Step How-It-Works",
        "severity": "high",
        "category": "layout",
        "patterns": [
            # Must have a "How it Works" heading near numbered steps — avoids wizard/checkout false positives
            r"(How It Works|How it works|how.it.works).{0,300}(Step\s+1|step.?1|First,\s+|Step one)",
        ],
        "message": "Three-step 'How It Works' section detected. Most products don't need this — show the product working instead.",
        "exclude_paths": [r"node_modules/", r"/dist/", r"/\.next/", r"/build/", r"/out/"],
    },
    {
        "id": "alternating_sections",
        "name": "Alternating Image-Text Sections",
        "severity": "high",
        "category": "layout",
        "patterns": [
            # Match structural class names that encode alternating layout, not prose mentions of "image" or "text"
            r"(section|row|feature).{0,30}(image-left|image-right|text-left|text-right).{0,200}(section|row|feature).{0,30}(image-left|image-right|text-left|text-right)",
            r"(flex-row-reverse|flex-row).{0,300}(flex-row-reverse|flex-row).{0,300}(flex-row-reverse|flex-row)",
        ],
        "message": "Repeating alternating image-text layout detected. Vary section structures — not every section needs an image.",
        "exclude_patterns": [r"gallery|portfolio|grid"],
        "exclude_paths": [r"node_modules/", r"/dist/", r"/\.next/", r"/build/", r"/out/"],
    },
    {
        "id": "four_column_footer",
        "name": "Four-Column Footer Dump",
        "severity": "medium",
        "category": "layout",
        "patterns": [
            r"(Product|Company|Resources|Support|Legal).{0,30}(Product|Company|Resources|Support|Legal).{0,30}(Product|Company|Resources|Support|Legal)",
        ],
        "message": "4-column footer with generic link groups detected. Show 5 links users actually click.",
    },
    {
        "id": "card_inception",
        "name": "Card Inception (card inside card)",
        "severity": "high",
        "category": "layout",
        "patterns": [
            # Look for actual nesting indicators: a card class on an element inside another card element
            r"<[a-zA-Z]+[^>]*class=[\"'][^\"']*\bcard\b[^\"']*[\"'][^>]*>(?:[^<]|<(?!/[a-zA-Z]))*<[a-zA-Z]+[^>]*class=[\"'][^\"']*\bcard\b[^\"']*[\"']",
            # JSX/TSX: <Card ... > containing another <Card
            r"<Card[^>]*>(?:.|\n){0,500}<Card\b",
        ],
        "message": "Cards nested inside cards detected. Flat hierarchy — use lists inside outer cards, not nested cards.",
        "exclude_patterns": [r"trello|kanban|board"],
        "exclude_paths": [r"node_modules/", r"/dist/", r"/\.next/", r"/build/", r"/out/"],
    },
    {
        "id": "three_pricing_cards",
        "name": "Three Pricing Cards",
        "severity": "medium",
        "category": "layout",
        "patterns": [
            r"(Free|Starter|Basic).{0,100}(Pro|Premium|Professional).{0,100}(Enterprise|Team|Business)",
            r"(Most Popular|Popular|Best Value)",
        ],
        "message": "3-column pricing table detected. Consider if 2 tiers suffice — or if pricing belongs in a table, not cards.",
    },
    {
        "id": "testimonial_grid",
        "name": "Testimonial Card Grid",
        "severity": "medium",
        "category": "layout",
        "patterns": [
            r"testimonial.{0,30}(name|Name|name\s*:).{0,30}(title|Title|role|Role)",
            r"(testimonial|quote|review).{0,100}(portrait|avatar|photo|headshot)",
        ],
        "message": "Testimonial cards with portrait photos detected. Consider single scrolling quote instead of grid.",
    },
    {
        "id": "circular_icon_background",
        "name": "Circular Icon in Colored Background",
        "severity": "high",
        "category": "visual",
        "patterns": [
            r"border-radius\s*:\s*50%\s*[;}]",
        ],
        "message": "Circular icon with colored background found. Hard constraint — use flat icons without circular backgrounds.",
    },
    {
        "id": "system_font_default",
        "name": "System Font Stack as Identity",
        "severity": "medium",
        "category": "typography",
        "patterns": [
            r"font-family\s*:\s*(system-ui|-apple-system|BlinkMacSystemFont|Segoe UI)",
        ],
        "message": "System font stack used. Define a named typeface — system fonts signal no identity choice was made. Note: Tailwind base CSS injects this; flag is expected in Tailwind reset files.",
        "exclude_patterns": [r"monospace", r"code"],
        # Tailwind/framework resets legitimately set system fonts — skip those files
        "exclude_paths": [
            r"node_modules/",
            r"/dist/",
            r"/\.next/",
            r"/build/",
            r"/out/",
            r"tailwind\.css$",
            r"reset\.css$",
            r"base\.css$",
            r"preflight",
        ],
    },
    {
        "id": "lorem_ipsum",
        "name": "Lorem Ipsum Placeholder",
        "severity": "low",
        "category": "content",
        "patterns": [
            r"lorem\s*ipsum",
        ],
        "message": "Lorem ipsum detected. Replace with real content or honest placeholder.",
        "exclude_patterns": [r"(example|demo|sample)"],
    },
    {
        "id": "italic_header",
        "name": "Italic Header / Display Type",
        "severity": "low",
        "category": "typography",
        "patterns": [
            r"(h[1-6]|[Hh]eadline|[Hh]ero-title|[Dd]isplay).{0,80}font-style\s*:\s*italic",
        ],
        "message": "Italic heading detected. Use weight, accent color, or underline instead.",
    },
    {
        "id": "dummy_testimonials",
        "name": "Dummy Testimonials",
        "severity": "high",
        "category": "content",
        "patterns": [
            r"(John|Jane|Sarah|Mike|David|Emily|Alex|Chris)\s(D\.|Smith|Johnson|Brown|Williams|Jones|Garcia|Miller|Davis)",
        ],
        "message": "Fabricated testimonial name detected. Remove unless user provided real quotes.",
    },
    {
        "id": "pure_black_white",
        "name": "Pure Black on Pure White",
        "severity": "low",
        "category": "visual",
        "patterns": [
            # Match exact pure-black or pure-white CSS property values only
            r"background(-color)?\s*:\s*(#ffffff|#fff)\s*[;}]",
            r"background(-color)?\s*:\s*(#000000|#000)\s*[;}]",
            r"(?<!-)color\s*:\s*(#000000|#000)\s*[;}]",
            r"(?<!-)color\s*:\s*(#ffffff|#fff)\s*[;}]",
        ],
        "message": "Pure black (#000) or pure white (#fff) CSS value detected. Use off-blacks and off-whites for readability.",
        "exclude_paths": [r"node_modules/", r"/dist/", r"/\.next/", r"/build/", r"/out/", r"reset\.css$", r"base\.css$", r"preflight"],
    },
    {
        "id": "inter_default",
        "name": "Inter Font Without Identity Choice",
        "severity": "low",
        "category": "typography",
        "patterns": [
            r"Inter.{0,30}(Inter\s*;|Inter\s*\),)",
        ],
        "message": "Inter is the default AI font. Define a distinctive typeface unless specifically chosen for the identity.",
    },
    {
        "id": "em_dash_content",
        "name": "Em-Dash in Content",
        "severity": "high",
        "category": "content",
        "patterns": [
            # Unicode em-dash (U+2014) and en-dash (U+2013) used as separator
            r"—",
            r"–",
            # HTML entity forms
            r"&mdash;",
            r"&ndash;",
            r"&#8212;",
            r"&#8211;",
        ],
        "message": "Em-dash or en-dash detected. The em-dash is the #1 AI copy tell. Use a period, comma, hyphen, or restructure the sentence.",
        "exclude_paths": [r"node_modules/", r"/dist/", r"/\.next/", r"/build/", r"/out/"],
        "skip_comment_lines": True,
    },
    {
        "id": "fraunces_instrument_serif",
        "name": "Banned AI-Default Serif Font",
        "severity": "high",
        "category": "typography",
        "patterns": [
            r"Fraunces",
            r"Instrument[_\s]Serif",
        ],
        "message": "Fraunces / Instrument Serif are the two most overused AI-generated display serifs. Pick a different typeface unless the brand explicitly requires it.",
        "exclude_paths": [r"node_modules/", r"/dist/", r"/\.next/"],
    },
    {
        "id": "eyebrow_density",
        "name": "Eyebrow Overuse (Uppercase Tracking Label)",
        "severity": "medium",
        "category": "layout",
        "patterns": [
            # 4+ occurrences of small uppercase tracking labels above section headings (inline check is approximate)
            # Pattern matches the repeated use of uppercase + tracking in the same file
            r"(uppercase\s+tracking|tracking.{0,20}uppercase).{0,500}(uppercase\s+tracking|tracking.{0,20}uppercase).{0,500}(uppercase\s+tracking|tracking.{0,20}uppercase).{0,500}(uppercase\s+tracking|tracking.{0,20}uppercase)",
        ],
        "message": "4+ eyebrow labels (uppercase tracking) detected in one file. Max 1 per 3 sections. Remove redundant section labels — position on the page categorizes content.",
        "exclude_paths": [r"node_modules/", r"/dist/", r"/\.next/", r"/build/", r"/out/"],
    },
]


SKIP_DIRS = {"node_modules", ".next", "dist", "build", "out", ".git", ".turbo", ".cache", "__pycache__", ".svelte-kit"}

def find_target_files(path):
    """Walk directory or single file, returning matching file paths."""
    extensions = {".html", ".css", ".jsx", ".tsx", ".vue", ".svelte", ".astro", ".php", ".kt", ".swift", ".dart", ".ts", ".js", ".py"}
    path = Path(path)
    if path.is_file():
        return [path] if path.suffix in extensions else []

    files = []
    for root, dirs, filenames in os.walk(path):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in filenames:
            fp = Path(root) / f
            if fp.suffix in extensions:
                files.append(fp)
    return files


def lint_file(filepath, rules):
    """Run all rules against a single file."""
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    findings = []
    fired_rules = set()
    for rule in rules:
        if rule["id"] in fired_rules:
            continue

        # Check content-based exclusions
        excluded = False
        for ex in rule.get("exclude_patterns", []):
            if re.search(ex, content, re.IGNORECASE):
                excluded = True
                break
        if excluded:
            continue

        # Check path-based exclusions
        for ex in rule.get("exclude_paths", []):
            if re.search(ex, str(filepath), re.IGNORECASE):
                excluded = True
                break
        if excluded:
            continue

        # For rules that must skip comment lines, check line by line
        if rule.get("skip_comment_lines"):
            comment_prefixes = ("//", "#", "*", "/*", "<!--", "--", "/**")
            lines = content.splitlines()
            found = False
            for i, line in enumerate(lines):
                stripped = line.strip()
                if any(stripped.startswith(p) for p in comment_prefixes):
                    continue
                for pattern in rule["patterns"]:
                    if re.search(pattern, line, re.IGNORECASE):
                        findings.append({
                            "rule": rule["id"],
                            "name": rule["name"],
                            "severity": rule["severity"],
                            "category": rule["category"],
                            "file": str(filepath),
                            "line": i + 1,
                            "message": rule["message"],
                        })
                        fired_rules.add(rule["id"])
                        found = True
                        break
                if found:
                    break
            continue

        for pattern in rule["patterns"]:
            match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
            if match:
                line_num = content[: match.start()].count("\n") + 1
                findings.append({
                    "rule": rule["id"],
                    "name": rule["name"],
                    "severity": rule["severity"],
                    "category": rule["category"],
                    "file": str(filepath),
                    "line": line_num,
                    "message": rule["message"],
                })
                fired_rules.add(rule["id"])
                break
    return findings


def print_text(findings):
    """Print findings in human-readable format."""
    if not findings:
        print("No anti-patterns found.")
        return

    by_severity = {"critical": [], "high": [], "medium": [], "low": []}
    for f in findings:
        by_severity[f["severity"]].append(f)

    for sev in ["critical", "high", "medium", "low"]:
        items = by_severity[sev]
        if not items:
            continue
        label = sev.upper()
        print(f"\n=== {label} ({len(items)}) ===")
        for f in items:
            print(f"  [{f['rule']}] {f['file']}:{f['line']}")
            print(f"    {f['name']}: {f['message']}")

    print(f"\nTotal: {len(findings)} findings")


def print_json(findings):
    """Print findings as JSON array."""
    print(json.dumps(findings, indent=2))


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 lint.py <path> [--format json|text] [--exit-code]", file=sys.stderr)
        sys.exit(1)

    path_arg = args[0]
    fmt = "text"
    use_exit_code = False

    if "--format" in args:
        idx = args.index("--format")
        if idx + 1 < len(args):
            fmt = args[idx + 1]

    if "--exit-code" in args or "--ci" in args:
        use_exit_code = True

    path = Path(path_arg)
    if not path.exists():
        print(f"Error: path not found: {path}", file=sys.stderr)
        sys.exit(1)

    files = find_target_files(path)
    if not files:
        print(f"No matching files found in: {path}", file=sys.stderr)
        sys.exit(0)

    all_findings = []
    for f in files:
        findings = lint_file(f, RULES)
        all_findings.extend(findings)

    if fmt == "json":
        print_json(all_findings)
    else:
        print_text(all_findings)

    if use_exit_code:
        if any(f["severity"] in ("critical", "high") for f in all_findings):
            sys.exit(1)
        if any(f["severity"] == "medium" for f in all_findings):
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
