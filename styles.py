"""Global styles for the application"""

from pygments.formatters import HtmlFormatter as _HtmlFormatter
PYGMENTS_CSS = _HtmlFormatter(style='default', cssclass='post-code').get_style_defs('.post-code')

from config import (
    FONT_HEADING, FONT_BODY, FONT_MONO, NAVBAR_HEIGHT,
    COLOR_BG, COLOR_SURFACE, COLOR_SURFACE_ALT, COLOR_BORDER,
    COLOR_TEXT, COLOR_TEXT_SEC, COLOR_ACCENT, COLOR_ACCENT_SEC,
)

# Hero — light
HERO_BG = "#FFFFFF"
HERO_TEXT = "#FFFFFF"
HERO_TEXT_SEC = "rgba(255,255,255,0.65)"
HERO_BORDER = "rgba(255,255,255,0.25)"


GLOBAL_STYLES = f"""
    :root {{
        --site-margin: clamp(0.5rem, 0.25rem + 0.5vw, 0.75rem);
        --site-max-width: 1200px;
    }}

    /* Reset */
    *, *::before, *::after {{ box-sizing: border-box; }}
    html, body {{ background: {COLOR_BG}; color: {COLOR_TEXT}; margin: 0; padding: 0; font-family: {FONT_BODY}; }}

    /* Typography */
    body {{ font-size: 17px; line-height: 1.65; font-weight: 400; }}
    h1, h2, h3, h4, h5, h6 {{
        font-family: {FONT_HEADING};
        text-transform: none;
        text-align: left;
        font-weight: 600;
        letter-spacing: -0.02em;
        color: {COLOR_TEXT};
    }}
    h1 {{ font-size: 48px; line-height: 1.1; }}
    h2 {{ font-size: 36px; line-height: 1.1; }}

    /* --- Navbar --- */
    .top-nav {{
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        height: {NAVBAR_HEIGHT};
        background: {COLOR_BG};
        z-index: 1000;
        display: flex;
        align-items: center;
    }}
    .nav-inner {{
        width: 100%;
        max-width: var(--site-max-width);
        margin: 0 auto;
        padding: 0 var(--site-margin);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
    .nav-logo {{ height: 44px; display: block; }}
    .nav-links {{ display: flex; gap: 32px; }}
    .nav-links a {{
        position: relative;
        color: {COLOR_TEXT_SEC};
        font-family: {FONT_HEADING};
        font-size: 15px;
        font-weight: 400;
        text-decoration: none;
        transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: {COLOR_TEXT}; }}
    .nav-link-active {{ color: {COLOR_TEXT} !important; text-decoration: none !important; }}
    .nav-link-active::after {{
        content: '';
        position: absolute;
        bottom: -4px; left: 0;
        width: 100%; height: 2px;
        background: {COLOR_ACCENT};
    }}

    /* --- Content area --- */
    #content-area {{ padding-top: {NAVBAR_HEIGHT}; }}

    /* --- Hero (always dark, typographic) --- */
    .hero-section {{
        width: 100%;
        margin-top: -{NAVBAR_HEIGHT};
        padding-top: {NAVBAR_HEIGHT};
        background: {HERO_BG};
    }}
    .hero-content {{
        max-width: var(--site-max-width);
        width: 100%;
        margin: 0 auto;
        padding: 40px var(--site-margin);
    }}
    .hero-video-wrap {{
        position: relative;
        width: 100%;
        overflow: hidden;
    }}
    .hero-video {{
        width: 100%;
        display: block;
        aspect-ratio: 16/9;
        object-fit: cover;
    }}
    .hero-overlay {{
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.42);
    }}
    .hero-text {{
        position: absolute;
        inset: 0;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding: 48px;
        gap: 28px;
    }}
    .hero-eyebrow {{
        font-family: {FONT_MONO};
        font-size: 11px;
        font-weight: 400;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: {HERO_TEXT_SEC};
        display: block;
        margin-bottom: 20px;
    }}
    .hero-title {{
        font-family: {FONT_HEADING};
        font-size: 75px;
        font-weight: 700;
        line-height: 0.95;
        letter-spacing: -0.03em;
        color: {HERO_TEXT};
        display: block;
    }}
    .hero-rule {{
        border: none;
        border-top: 1px solid rgba(0,0,0,0.12);
        margin: 0 0 28px 0;
    }}
    .hero-bottom {{
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        gap: 40px;
    }}
    .hero-subtitle {{
        font-family: {FONT_BODY};
        font-size: 14px;
        font-weight: 400;
        color: {HERO_TEXT_SEC};
        line-height: 1.55;
        flex: 1;
        max-width: 480px;
        margin: 0;
    }}
    .hero-cta-group {{
        display: flex;
        gap: 32px;
        flex-shrink: 0;
    }}
    .hero-cta {{
        font-family: {FONT_MONO};
        font-size: 12px;
        font-weight: 400;
        color: {HERO_TEXT};
        text-decoration: none;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        transition: color 0.2s;
    }}
    .hero-cta:hover {{ color: {COLOR_ACCENT}; }}

    /* --- Section label (mono uppercase, replaces H2) --- */
    .section-label {{
        font-family: {FONT_MONO};
        font-size: 11px;
        font-weight: 400;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: {COLOR_TEXT_SEC};
        margin: 48px 0 16px 0;
        display: block;
    }}

    /* --- Featured project --- */
    .featured {{
        padding: 40px 0;
        border-top: 5px solid {COLOR_TEXT};
        border-bottom: 1px solid {COLOR_BORDER};
        margin-bottom: 40px;
    }}
    .featured-label {{
        font-family: {FONT_MONO};
        font-size: 12px;
        color: {COLOR_TEXT_SEC};
        letter-spacing: 0.05em;
        margin: 0 0 16px 0;
    }}
    .featured-title {{
        font-family: {FONT_HEADING};
        font-size: 36px;
        font-weight: 600;
        color: {COLOR_TEXT};
        margin: 0 0 8px 0;
        letter-spacing: -0.02em;
        line-height: 1.1;
    }}
    .featured-date {{
        font-family: {FONT_MONO};
        font-size: 13px;
        color: {COLOR_TEXT_SEC};
        margin: 0 0 16px 0;
    }}
    .featured-excerpt {{
        font-family: {FONT_BODY};
        font-size: 17px;
        color: {COLOR_TEXT_SEC};
        margin: 0 0 20px 0;
        line-height: 1.6;
    }}
    .featured-link {{
        font-family: {FONT_MONO};
        font-size: 13px;
        color: {COLOR_TEXT};
        text-decoration: none;
        transition: color 0.2s;
        border-bottom: 1px solid {COLOR_TEXT};
        padding-bottom: 1px;
    }}
    .featured-link:hover {{ color: {COLOR_TEXT_SEC}; border-color: {COLOR_TEXT_SEC}; }}

    /* --- Content wrapper --- */
    .content-wrapper {{
        max-width: var(--site-max-width);
        margin: 0 auto;
        padding: 40px var(--site-margin) 80px;
        background: {COLOR_BG};
        position: relative;
        z-index: 1;
    }}
    .page-header {{
        margin-bottom: 40px;
        border-left: 5px solid {COLOR_TEXT};
        padding-left: 20px;
    }}

    /* --- Post elements --- */
    .post-item {{ text-decoration: none; display: block; }}
    .post-item-inner {{ padding: 20px 0; border-bottom: 1px solid {COLOR_BORDER}; transition: background 0.15s; }}
    .post-item:hover .post-item-inner {{ padding-left: 12px; }}
    .post-title {{ font-family: {FONT_HEADING}; font-size: 20px; font-weight: 500; color: {COLOR_TEXT}; margin: 0 0 4px 0; }}
    .post-date {{ font-family: {FONT_MONO}; font-size: 13px; font-weight: 400; color: {COLOR_TEXT_SEC}; margin: 0 0 6px 0; }}
    .post-excerpt {{ font-size: 15px; font-weight: 400; color: {COLOR_TEXT_SEC}; margin: 0; }}
    .post-body {{ font-size: 17px; font-weight: 400; color: {COLOR_TEXT}; line-height: 1.65; margin-bottom: 16px; }}
    .post-back {{
        font-family: {FONT_MONO};
        color: {COLOR_TEXT};
        text-decoration: none;
        font-size: 13px;
        display: inline-block;
        margin-bottom: 24px;
        border-bottom: 1px solid {COLOR_BORDER};
        padding-bottom: 1px;
        transition: color 0.2s, border-color 0.2s;
    }}
    .post-back:hover {{ color: {COLOR_TEXT_SEC}; border-color: {COLOR_TEXT_SEC}; }}
    .post-meta {{ font-family: {FONT_MONO}; font-size: 13px; font-weight: 400; color: {COLOR_TEXT_SEC}; margin-bottom: 24px; }}

    .code-block {{
        margin: 24px 0;
        background: #F5F5F5;
        border: 1px solid {COLOR_BORDER};
        border-radius: 0;
        overflow-x: auto;
    }}
    .post-code {{
        padding: 20px 24px;
        margin: 0;
        background: #F5F5F5;
        font-size: 13px;
        line-height: 1.6;
        color: {COLOR_TEXT};
        font-family: {FONT_MONO};
        white-space: pre;
    }}
    .post-figure {{ margin: 32px 0; text-align: center; }}
    .post-img {{ max-width: 100%; border-radius: 0; border: 1px solid {COLOR_BORDER}; }}
    .post-caption {{ font-family: {FONT_MONO}; font-size: 12px; color: {COLOR_TEXT_SEC}; margin-top: 8px; }}

    /* --- Footer --- */
    .footer {{
        max-width: var(--site-max-width);
        margin: 0 auto;
        padding: 40px var(--site-margin);
        font-family: {FONT_MONO};
        font-size: 12px;
        color: {COLOR_TEXT_SEC};
        border-top: 5px solid {COLOR_TEXT};
    }}

    /* --- Placeholder text --- */
    .text-placeholder {{ font-size: 17px; font-weight: 400; color: {COLOR_TEXT}; }}

    /* --- Links --- */
    a {{ color: {COLOR_TEXT}; }}
    a:hover {{ color: {COLOR_TEXT_SEC}; }}

    /* --- Responsive: tablet --- */
    @media (max-width: 768px) {{
        html, body {{ overflow-x: hidden; }}
        h1 {{ font-size: 36px; }}
        h2 {{ font-size: 28px; }}
        .nav-logo {{ height: 48px; }}
        .nav-links {{ gap: 20px; }}
        .nav-links a {{ font-size: 14px !important; }}
        .hero-content {{ padding: 24px var(--site-margin); }}
        .hero-text {{ padding: 32px; gap: 20px; }}
        .hero-title {{ font-size: 48px !important; }}
        .post-code {{ padding: 16px; font-size: 12px; }}
    }}

    /* --- Responsive: phone --- */
    @media (max-width: 480px) {{
        h1 {{ font-size: 28px !important; }}
        h2 {{ font-size: 22px !important; }}
        .nav-logo {{ height: 36px; }}
        .nav-links {{ gap: 12px; }}
        .nav-links a {{ font-size: 12px !important; }}
        .hero-content {{ padding: 16px var(--site-margin); }}
        .hero-video {{ aspect-ratio: 4/3; }}
        .hero-text {{ padding: 20px; gap: 16px; }}
        .hero-title {{ font-size: 28px !important; line-height: 1.0 !important; }}
        .hero-bottom {{ flex-direction: column; align-items: flex-start; gap: 16px; }}
        .hero-cta-group {{ gap: 16px; }}
        .post-code {{ padding: 12px; font-size: 11px; }}
    }}
"""
