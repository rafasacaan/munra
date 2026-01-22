"""Global styles for the application"""

from config import FONT_FAMILY, COLOR_WHITE, COLOR_BLACK

GLOBAL_STYLES = f"""
    * {{
        font-family: {FONT_FAMILY};
    }}
    html, body {{
        background-color: {COLOR_WHITE};
        margin: 0;
        padding: 0;
    }}
    @media (max-width: 768px) {{
        html, body {{
            overflow-x: hidden;
        }}
    }}
    h1, h2, h3, h4, h5, h6 {{
        font-family: {FONT_FAMILY};
        text-transform: uppercase;
        text-align: left;
        font-weight: 900;
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
    @media (max-width: 768px) {{
        h1 {{
            font-size: 40px;
        }}
        h2 {{
            font-size: 32px;
        }}
    }}
    .highlight-munra {{
        background: linear-gradient(to right, 
            rgba(255, 110, 199, 0.7) 0%, 
            rgba(255, 110, 199, 0.85) 30%,
            rgba(255, 110, 199, 0.75) 60%, 
            rgba(255, 110, 199, 0.7) 100%);
        padding: 2px 4px;
        border-radius: 45% 12% 38% 18% / 25% 42% 15% 35%;
        display: inline-block;
        transform: rotate(-1.2deg) skewX(-0.8deg);
        box-shadow: 0 1px 3px rgba(255, 110, 199, 0.4);
        font-style: italic;
    }}
    .munra-card {{
        padding: 20px;
        background-color: {COLOR_WHITE};
        margin: 10px;
        width: 300px;
        text-align: center;
        position: relative;
        transform: rotate(-0.6deg);
    }}
    .munra-card-border {{
        position: absolute;
        top: -5px;
        left: -5px;
        width: calc(100% + 10px);
        height: calc(100% + 10px);
        pointer-events: none;
    }}
    
    /* Content section with offset */
    .content-section {{
        margin-left: 100px;
    }}
    
    /* Responsive layout */
    @media (max-width: 768px) {{
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
        .content-area {{
            padding: 20px !important;
            padding-right: 20px !important;
            max-width: 100% !important;
        }}
        .content-section {{
            margin-left: 20px !important;
        }}
        .post-grid {{
            grid-template-columns: repeat(2, 1fr) !important;
            gap: 8px !important;
        }}
    }}
    
    @media (max-width: 480px) {{
        .post-grid {{
            grid-template-columns: 1fr !important;
        }}
        .content-section {{
            margin-left: 0 !important;
        }}
        h1 {{
            font-size: 32px !important;
        }}
        h2 {{
            font-size: 24px !important;
        }}
    }}
"""
