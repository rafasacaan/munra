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

# Colors — "Clean Minimal" palette
COLOR_BG = "#FFFFFF"           # White — page canvas
COLOR_SURFACE = "#EFEFEC"      # Light Gray — cards, panels, hover states
COLOR_SURFACE_ALT = "#E5E4E0"  # Warm Light — alternative surfaces
COLOR_BORDER = "#D0CFC9"       # Warm Border — dividers, borders
COLOR_TEXT_SEC = "#6B6860"     # Warm Gray — captions, metadata
COLOR_TEXT = "#1A1714"         # Near-Black — body text
COLOR_ACCENT = "#1A1714"       # Near-Black — active states
COLOR_ACCENT_SEC = "#0A0908"   # Deep Black — hover

# Paths
LOGO_PATH = "/static/imgs/munra-white.png"
BG_VIDEO_PATH = "/static/videos/munra-v2-web.mp4"
FAVICON_PATH = "/static/imgs/munra.jpg"
STATIC_NOTES_PATH = "static/notes"
STATIC_MODELS_PATH = "static/models"

# Hero content
HERO_EYEBROW = "AI Sound and Research Lab"
HERO_TITLE = "Tiny audio models trained<br>on character and true sound"
HERO_SUBTITLE = "The best recordings have tape hiss. The best beats have timing drift. We're building models that learn from what makes sound feel alive."
HERO_CTAS = [
    ("What we're learning", "/blog"),
    ("Browse models", "/models"),
]

# Analytics
GOOGLE_ANALYTICS_ID = "G-5WWLZXKEX0"
