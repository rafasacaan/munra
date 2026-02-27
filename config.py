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
FONT_URL = "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600&family=Source+Serif+4:ital,wght@0,300;0,400;1,400&family=Space+Mono:wght@400&display=swap"

# Colors — "Clean Minimal" palette
COLOR_BG = "#FFFFFF"           # White — page canvas
COLOR_SURFACE = "#EFEFEC"      # Light Gray — cards, panels, hover states
COLOR_BORDER = "#D0CFC9"       # Warm Border — dividers, borders
COLOR_TEXT_SEC = "#6B6860"     # Warm Gray — captions, metadata
COLOR_TEXT = "#1A1714"         # Near-Black — body text
COLOR_ACCENT = "#1A1714"       # Near-Black — active states

# Paths
LOGO_PATH = "/static/imgs/logos/munra-white.png"
BG_VIDEO_PATH = "/static/videos/munra-v4-web-audio.mp4"
FAVICON_PATH = "/static/imgs/munra.jpg"
STATIC_NOTES_PATH = "static/notes"

# Hero content
HERO_EYEBROW = "Building generative audio models for creative use"
HERO_TITLE = "Training tiny models to generate drums, voice, and textures.<br>Publishing samples, models, and experiments."
HERO_CTAS = [
    ("Samples", "/samples"),
    ("Modelos", "/models"),
    ("What we're learning", "/blog"),
]

# Analytics
GOOGLE_ANALYTICS_ID = "G-5WWLZXKEX0"
