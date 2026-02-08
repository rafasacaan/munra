"""Global styles for the application"""

from config import FONT_FAMILY, COLOR_WHITE

GLOBAL_STYLES = f"""
    * {{
        font-family: {FONT_FAMILY};
    }}
    html, body {{
        background-color: transparent;
        color: {COLOR_WHITE};
        margin: 0;
        padding: 0;
    }}
    .main-layout, .vertical-nav, .content-area {{
        background: transparent;
    }}
    h1, h2, h3, h4, h5, h6 {{
        font-family: {FONT_FAMILY};
        text-transform: uppercase;
        text-align: left;
        font-weight: 200;
        letter-spacing: -0.08em;
    }}
    h1 {{
        font-size: 64px;
        line-height: 0.75;
    }}
    h2 {{
        font-size: 48px;
        line-height: 0.75;
    }}
    .nav-links a {{
        position: relative;
    }}
    .nav-link-active {{
        text-decoration: none !important;
    }}
    .nav-link-active::after {{
        content: '';
        position: absolute;
        bottom: -4px;
        left: 0;
        width: 17%;
        height: 3px;
        background-color: white;
    }}

    /* Responsive layout */
    @media (max-width: 768px) {{
        html, body {{
            overflow-x: hidden;
        }}
        h1 {{
            font-size: 40px;
        }}
        h2 {{
            font-size: 32px;
        }}
        .main-layout {{
            flex-direction: column !important;
            height: auto !important;
        }}
        .vertical-nav {{
            width: 100% !important;
            padding: 20px !important;
        }}
        .vertical-nav img {{
            max-width: 180px !important;
        }}
        .nav-links {{
            display: flex !important;
            flex-direction: row !important;
            gap: 20px !important;
            justify-content: center !important;
        }}
        .nav-links a {{
            margin-bottom: 0 !important;
        }}
        .content-area {{
            padding: 20px !important;
            padding-right: 20px !important;
            max-width: 100% !important;
        }}
    }}

    @media (max-width: 480px) {{
        h1 {{
            font-size: 32px !important;
        }}
        h2 {{
            font-size: 24px !important;
        }}
    }}
"""
