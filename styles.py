"""Global styles for the application"""

from config import FONT_FAMILY, COLOR_WHITE, NAVBAR_HEIGHT

GLOBAL_STYLES = f"""
    :root {{
        --site-margin: clamp(0.5rem, 0.25rem + 0.5vw, 0.75rem);
        --site-max-width: 1200px;
    }}

    /* Reset */
    *, *::before, *::after {{ box-sizing: border-box; }}
    * {{ font-family: {FONT_FAMILY}; }}
    html, body {{ background: #000; color: {COLOR_WHITE}; margin: 0; padding: 0; }}

    /* Typography */
    h1, h2, h3, h4, h5, h6 {{
        font-family: {FONT_FAMILY};
        text-transform: none;
        text-align: left;
        font-weight: 200;
        letter-spacing: -0.08em;
    }}
    h1 {{ font-size: 64px; line-height: 0.75; }}
    h2 {{ font-size: 48px; line-height: 0.75; }}

    /* --- Navbar --- */
    .top-nav {{
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        height: {NAVBAR_HEIGHT};
        background: #000;
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
    .nav-logo {{ height: 60px; display: block; }}
    .nav-links {{ display: flex; gap: 32px; }}
    .nav-links a {{
        position: relative;
        color: white;
        font-size: 16px;
        font-weight: 300;
        text-decoration: none;
    }}
    .nav-link-active {{ text-decoration: none !important; }}
    .nav-link-active::after {{
        content: '';
        position: absolute;
        bottom: -4px; left: 0;
        width: 100%; height: 2px;
        background: white;
    }}

    /* --- Content area --- */
    #content-area {{ padding-top: {NAVBAR_HEIGHT}; }}

    /* --- Hero --- */
    .hero-section {{
        position: relative;
        width: 100%; height: 100vh;
        margin-top: -{NAVBAR_HEIGHT};
        padding-top: {NAVBAR_HEIGHT};
        overflow: hidden;
        display: flex;
        align-items: flex-end;
        background: #000;
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
            #000 0%, rgba(0,0,0,0.6) 20%,
            transparent 40%,
            rgba(0,0,0,0.6) 60%, #000 100%
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
        font-size: 22px;
        font-weight: 600;
        letter-spacing: 0.1em;
        color: white;
        display: block;
        margin-bottom: 20px;
    }}
    .hero-title {{
        font-size: 96px;
        font-weight: 300;
        line-height: 0.9;
        display: inline-block;
    }}
    .hero-subtitle {{
        font-size: 18px;
        font-weight: 300;
        color: white;
        margin: 20px 0 0;
        letter-spacing: 0.02em;
    }}
    .hero-cta {{
        display: inline-block;
        margin-top: 30px;
        padding: 12px 32px;
        font-size: 14px;
        font-weight: 400;
        color: white;
        text-decoration: none;
        letter-spacing: 0.1em;
        border: 1px solid rgba(255,255,255,0.4);
        transition: border-color 0.3s, background 0.3s;
    }}
    .hero-cta:hover {{
        border-color: white;
        background: rgba(255,255,255,0.1);
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
        border-right: 2px solid rgba(255,255,255,0.5);
        border-bottom: 2px solid rgba(255,255,255,0.5);
        transform: rotate(45deg);
        animation: scroll-bounce 2s infinite;
    }}
    @keyframes scroll-bounce {{
        0%, 100% {{ opacity: 0.3; transform: rotate(45deg) translateY(0); }}
        50%      {{ opacity: 1;   transform: rotate(45deg) translateY(8px); }}
    }}

    /* --- Content wrapper --- */
    .content-wrapper {{
        max-width: var(--site-max-width);
        margin: 0 auto;
        padding: 40px var(--site-margin) 80px;
        background: #000;
        position: relative;
        z-index: 1;
    }}
    .page-header {{ margin-bottom: 40px; }}

    /* --- Post elements --- */
    .post-item {{ text-decoration: none; display: block; }}
    .post-item-inner {{ padding: 20px 0; border-bottom: 1px solid #333; }}
    .post-title {{ font-size: 20px; font-weight: 400; color: white; margin: 0 0 4px 0; }}
    .post-date {{ font-size: 13px; font-weight: 300; color: #999; margin: 0 0 6px 0; }}
    .post-excerpt {{ font-size: 15px; font-weight: 300; color: #ccc; margin: 0; }}
    .post-body {{ font-size: 16px; font-weight: 300; color: #ddd; line-height: 1.7; margin-bottom: 16px; }}
    .post-back {{ color: #999; text-decoration: none; font-size: 14px; display: inline-block; margin-bottom: 24px; }}
    .post-meta {{ font-size: 13px; font-weight: 300; color: #999; margin-bottom: 24px; }}

    .code-block {{
        margin: 24px 0;
        background: #111;
        border: 1px solid #222;
        border-radius: 4px;
        overflow-x: auto;
    }}
    .post-code {{
        padding: 20px 24px;
        margin: 0;
        font-size: 14px;
        line-height: 1.6;
        color: #e6e6e6;
        font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace;
        white-space: pre;
    }}
    .post-figure {{ margin: 32px 0; text-align: center; }}
    .post-img {{ max-width: 100%; border-radius: 4px; border: 1px solid #222; }}
    .post-caption {{ font-size: 12px; color: #999; margin-top: 8px; }}

    /* --- Footer --- */
    .footer {{
        max-width: var(--site-max-width);
        margin: 0 auto;
        padding: 40px var(--site-margin);
        font-size: 12px;
    }}

    /* --- Placeholder text --- */
    .text-placeholder {{ font-size: 18px; font-weight: 300; color: white; }}

    /* --- Responsive: tablet --- */
    @media (max-width: 768px) {{
        html, body {{ overflow-x: hidden; }}
        h1 {{ font-size: 40px; }}
        h2 {{ font-size: 32px; }}
        .nav-logo {{ height: 48px; }}
        .nav-links {{ gap: 20px; }}
        .nav-links a {{ font-size: 14px !important; }}
        .hero-eyebrow {{ font-size: 16px !important; }}
        .hero-title {{ font-size: 56px !important; }}
        .hero-subtitle {{ font-size: 16px; }}
        .post-code {{ padding: 16px; font-size: 13px; }}
    }}

    /* --- Responsive: phone --- */
    @media (max-width: 480px) {{
        h1 {{ font-size: 28px !important; }}
        h2 {{ font-size: 22px !important; }}
        .nav-logo {{ height: 36px; }}
        .nav-links {{ gap: 12px; }}
        .nav-links a {{ font-size: 12px !important; }}
        .hero-eyebrow {{ font-size: 14px !important; margin-bottom: 12px !important; }}
        .hero-title {{ font-size: 36px !important; }}
        .hero-subtitle {{ font-size: 14px; margin-top: 14px; }}
        .hero-cta {{ padding: 10px 24px; font-size: 12px; margin-top: 20px; }}
        .post-code {{ padding: 12px; font-size: 12px; }}
    }}
"""
