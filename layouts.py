"""Page layout templates"""

from fasthtml.common import *
from components import NavBar, Footer
from config import CONTENT_MAX_WIDTH, SITE_NAME


def TwoColumnLayout(current_page, content, title=SITE_NAME):
    """Standard two-column layout with vertical navbar and content area"""
    left_nav = NavBar(current_page, vertical=True)
    
    right_content = Div(
        *content,
        Footer(),
        style=f"flex: 1; padding: 40px; padding-right: 80px; overflow-y: auto; max-width: {CONTENT_MAX_WIDTH};",
        cls="content-area"
    )
    
    layout = Div(
        left_nav,
        right_content,
        style="display: flex; height: 100vh;",
        cls="main-layout"
    )
    
    return Title(title), layout
