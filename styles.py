"""Global styles for the application"""

from config import (
    FONT_HEADING, FONT_BODY, FONT_MONO, NAVBAR_HEIGHT,
    COLOR_BG, COLOR_SURFACE, COLOR_SURFACE_ALT, COLOR_BORDER,
    COLOR_TEXT, COLOR_TEXT_SEC, COLOR_ACCENT, COLOR_ACCENT_SEC,
)

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
        background: #181818;
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

    /* --- Hero --- */
    .hero-section {{
        position: relative;
        width: 100%; height: 40vh;
        min-height: 280px;
        margin-top: -{NAVBAR_HEIGHT};
        padding-top: {NAVBAR_HEIGHT};
        overflow: hidden;
        display: flex;
        align-items: flex-end;
        background: {COLOR_BG};
    }}
    .hero-video {{
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        object-fit: cover;
        z-index: 0;
    }}
    .hero-overlay {{
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(
            to bottom,
            {COLOR_BG} 0%, rgba(26,23,20,0.6) 20%,
            transparent 40%,
            rgba(26,23,20,0.6) 60%, {COLOR_BG} 100%
        );
        z-index: 1;
    }}
    .hero-content {{
        position: relative;
        z-index: 2;
        width: 100%;
        max-width: var(--site-max-width);
        margin: 0 auto;
        padding: 60px var(--site-margin);
    }}
    .hero-eyebrow {{
        font-family: {FONT_MONO};
        font-size: 13px;
        font-weight: 400;
        letter-spacing: 0.05em;
        color: {COLOR_TEXT_SEC};
        display: block;
        margin-bottom: 20px;
    }}
    .hero-title {{
        font-family: {FONT_HEADING};
        font-size: 72px;
        font-weight: 600;
        line-height: 1.0;
        letter-spacing: -0.02em;
        color: {COLOR_TEXT};
        display: inline-block;
    }}
    .hero-subtitle {{
        font-family: {FONT_BODY};
        font-size: 18px;
        font-weight: 400;
        color: {COLOR_TEXT_SEC};
        margin: 24px 0 0;
        line-height: 1.6;
    }}
    .hero-ctas {{
        display: flex;
        gap: 16px;
        margin-top: 30px;
        flex-wrap: wrap;
    }}
    .hero-cta {{
        display: inline-block;
        font-family: {FONT_HEADING};
        padding: 12px 32px;
        font-size: 14px;
        font-weight: 500;
        color: {COLOR_TEXT};
        text-decoration: none;
        letter-spacing: 0.05em;
        border: 1px solid {COLOR_BORDER};
        transition: border-color 0.3s, background 0.3s, color 0.3s;
    }}
    .hero-cta:hover {{
        border-color: {COLOR_ACCENT};
        color: {COLOR_ACCENT};
        background: rgba(22,228,145,0.08);
    }}
    .scroll-indicator {{
        position: absolute;
        bottom: 30px; left: 50%;
        transform: translateX(-50%);
        z-index: 2;
    }}
    .scroll-indicator span {{
        display: block;
        width: 20px; height: 20px;
        border-right: 2px solid {COLOR_BORDER};
        border-bottom: 2px solid {COLOR_BORDER};
        transform: rotate(45deg);
        animation: scroll-bounce 2s infinite;
    }}
    @keyframes scroll-bounce {{
        0%, 100% {{ opacity: 0.3; transform: rotate(45deg) translateY(0); }}
        50%      {{ opacity: 1;   transform: rotate(45deg) translateY(8px); }}
    }}

    /* --- Home header --- */
    .home-header {{
        padding: 60px 0 40px;
        border-bottom: 1px solid {COLOR_BORDER};
        margin-bottom: 40px;
    }}
    .home-name {{
        font-family: {FONT_HEADING};
        font-size: 32px;
        font-weight: 600;
        color: {COLOR_TEXT};
        margin: 0 0 8px 0;
        letter-spacing: -0.02em;
    }}
    .home-descriptor {{
        font-family: {FONT_MONO};
        font-size: 13px;
        color: {COLOR_TEXT_SEC};
        margin: 0;
    }}

    /* --- Featured project --- */
    .featured {{
        padding: 40px 0;
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
        color: {COLOR_ACCENT};
        text-decoration: none;
        transition: color 0.2s;
    }}
    .featured-link:hover {{ color: {COLOR_ACCENT_SEC}; }}

    /* --- Content wrapper --- */
    .content-wrapper {{
        max-width: var(--site-max-width);
        margin: 0 auto;
        padding: 40px var(--site-margin) 80px;
        background: {COLOR_BG};
        position: relative;
        z-index: 1;
    }}
    .page-header {{ margin-bottom: 40px; }}

    /* --- Post elements --- */
    .post-item {{ text-decoration: none; display: block; }}
    .post-item-inner {{ padding: 20px 0; border-bottom: 1px solid {COLOR_BORDER}; }}
    .post-item:hover .post-item-inner {{ background: {COLOR_SURFACE}; }}
    .post-title {{ font-family: {FONT_HEADING}; font-size: 20px; font-weight: 500; color: {COLOR_TEXT}; margin: 0 0 4px 0; }}
    .post-date {{ font-family: {FONT_MONO}; font-size: 13px; font-weight: 400; color: {COLOR_TEXT_SEC}; margin: 0 0 6px 0; }}
    .post-excerpt {{ font-size: 15px; font-weight: 400; color: {COLOR_TEXT_SEC}; margin: 0; }}
    .post-body {{ font-size: 17px; font-weight: 400; color: {COLOR_TEXT}; line-height: 1.65; margin-bottom: 16px; }}
    .post-back {{
        font-family: {FONT_MONO};
        color: {COLOR_ACCENT};
        text-decoration: none;
        font-size: 13px;
        display: inline-block;
        margin-bottom: 24px;
        transition: color 0.2s;
    }}
    .post-back:hover {{ color: {COLOR_ACCENT_SEC}; }}
    .post-meta {{ font-family: {FONT_MONO}; font-size: 13px; font-weight: 400; color: {COLOR_TEXT_SEC}; margin-bottom: 24px; }}

    .code-block {{
        margin: 24px 0;
        background: {COLOR_SURFACE};
        border: 1px solid {COLOR_BORDER};
        border-radius: 4px;
        overflow-x: auto;
    }}
    .post-code {{
        padding: 20px 24px;
        margin: 0;
        font-size: 13px;
        line-height: 1.6;
        color: {COLOR_TEXT};
        font-family: {FONT_MONO};
        white-space: pre;
    }}
    .post-figure {{ margin: 32px 0; text-align: center; }}
    .post-img {{ max-width: 100%; border-radius: 4px; border: 1px solid {COLOR_BORDER}; }}
    .post-caption {{ font-family: {FONT_MONO}; font-size: 12px; color: {COLOR_TEXT_SEC}; margin-top: 8px; }}

    /* --- Footer --- */
    .footer {{
        max-width: var(--site-max-width);
        margin: 0 auto;
        padding: 40px var(--site-margin);
        font-family: {FONT_MONO};
        font-size: 12px;
        color: {COLOR_TEXT_SEC};
        border-top: 1px solid {COLOR_BORDER};
    }}

    /* --- Placeholder text --- */
    .text-placeholder {{ font-size: 17px; font-weight: 400; color: {COLOR_TEXT}; }}

    /* --- Links --- */
    a {{ color: {COLOR_ACCENT}; }}
    a:hover {{ color: {COLOR_ACCENT_SEC}; }}

    /* --- Responsive: tablet --- */
    @media (max-width: 768px) {{
        html, body {{ overflow-x: hidden; }}
        h1 {{ font-size: 36px; }}
        h2 {{ font-size: 28px; }}
        .nav-logo {{ height: 48px; }}
        .nav-links {{ gap: 20px; }}
        .nav-links a {{ font-size: 14px !important; }}
        .hero-eyebrow {{ font-size: 12px !important; }}
        .hero-title {{ font-size: 48px !important; }}
        .hero-subtitle {{ font-size: 16px; }}
        .post-code {{ padding: 16px; font-size: 12px; }}
    }}

    /* --- Responsive: phone --- */
    @media (max-width: 480px) {{
        h1 {{ font-size: 28px !important; }}
        h2 {{ font-size: 22px !important; }}
        .nav-logo {{ height: 36px; }}
        .nav-links {{ gap: 12px; }}
        .nav-links a {{ font-size: 12px !important; }}
        .hero-eyebrow {{ font-size: 11px !important; margin-bottom: 12px !important; }}
        .hero-title {{ font-size: 32px !important; }}
        .hero-subtitle {{ font-size: 14px; margin-top: 14px; }}
        .hero-cta {{ padding: 10px 24px; font-size: 12px; }}
        .post-code {{ padding: 12px; font-size: 11px; }}
    }}
"""
