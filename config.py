"""Configuration constants for the application"""

# Site metadata
SITE_NAME = "munra"
SITE_DESCRIPTION = "AI-driven audio research lab"
SITE_URL = "https://munra.cl"

# Copyright
COPYRIGHT_YEAR = "2026"
COPYRIGHT_TEXT = f"munra \u00a9 {COPYRIGHT_YEAR}"

# Layout
NAVBAR_HEIGHT = "70px"

# Typography
FONT_HEADING = "'Space Grotesk', sans-serif"
FONT_BODY = "'Source Serif 4', Georgia, serif"
FONT_MONO = "'Space Mono', monospace"
FONT_URL = "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Source+Serif+4:ital,wght@0,300;0,400;0,500;0,600;1,400&family=Space+Mono:wght@400;700&display=swap"

# Colors — "Tape Machine Warm" palette
COLOR_BG = "#1A1714"           # Midnight Charcoal — page canvas
COLOR_SURFACE = "#252220"      # Warm Slate — cards, panels
COLOR_SURFACE_ALT = "#332E2A"  # Tobacco Gray — modals, hover states
COLOR_BORDER = "#4A433B"       # Aged Bronze — dividers, borders
COLOR_TEXT_SEC = "#9B9285"     # Warm Pewter — captions, metadata
COLOR_TEXT = "#E8E0D4"         # Parchment — body text
COLOR_ACCENT = "#16e491"       # Mint — links, active states
COLOR_ACCENT_SEC = "#B85C3A"   # Tape Reel Rust — hover, secondary

# Paths
LOGO_PATH = "/static/imgs/2-nobg-short.png"
FAVICON_PATH = "/static/imgs/munra.jpg"
BG_VIDEO_PATH = "/static/videos/munra-v2-web.mp4"
STATIC_NOTES_PATH = "static/notes"
STATIC_MODELS_PATH = "static/models"

# Hero content
HERO_EYEBROW = "AI Sound and Research Lab"
HERO_TITLE = "Tiny audio models trained<br>on character and true sound"
HERO_SUBTITLE = "The best recordings have tape hiss. The best beats have timing drift.<br>We're building models that learn from what makes sound feel alive."
HERO_CTAS = [
    ("What we're learning", "/blog"),
    ("Browse models", "/models"),
]

# Analytics
GOOGLE_ANALYTICS_ID = "G-5WWLZXKEX0"
