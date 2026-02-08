"""Page layout templates"""

from fasthtml.common import *
from components import NavBar, Footer
from config import SITE_NAME, BG_VIDEO_PATH


def SectionTitle(section_name):
    """Fixed section title at bottom right"""
    return Div(
        P(section_name,
          style="font-size: 64px; font-weight: 200; line-height: 1.1; color: white; margin: 0; text-transform: uppercase; letter-spacing: -0.08em;"),
        style="position: absolute; bottom: 40px; right: 80px; text-align: right;"
    )


def ContentArea(content, section_name=""):
    """Inner content for partial HTMX swaps"""
    return (
        Div(*content, style="flex: 1; margin-top: 25px;"),
        SectionTitle(section_name),
        Footer(),
    )


def TwoColumnLayout(current_page, content, section_name="", title=SITE_NAME):
    """Standard two-column layout with vertical navbar and content area"""
    left_nav = NavBar(current_page)

    right_content = Div(
        Div(*content, style="flex: 1; margin-top: 25px;"),
        SectionTitle(section_name),
        Footer(),
        style="flex: 1; padding: 40px; padding-right: 80px; padding-bottom: 120px; overflow-y: auto; display: flex; flex-direction: column; position: relative;",
        cls="content-area",
        id="content-area"
    )

    bg_video = NotStr(
        '<video autoplay loop muted playsinline '
        f'style="position:fixed;top:0;left:0;width:100%;height:100%;object-fit:cover;z-index:-1;">'
        f'<source src="{BG_VIDEO_PATH}" type="video/mp4">'
        '</video>'
    )

    layout = Div(
        bg_video,
        left_nav,
        right_content,
        style="display: flex; height: 100vh; position: relative;",
        cls="main-layout"
    )

    return layout
