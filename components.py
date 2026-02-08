"""Reusable UI components"""

from fasthtml.common import *
from config import NAVBAR_WIDTH, LOGO_PATH, COPYRIGHT_TEXT, COLOR_GRAY


def NavBar(current_page="home"):
    """Vertical navigation bar component"""
    def nav_link(text, href, page_name):
        is_active = current_page == page_name
        style = "color: white; font-size: 18px; font-weight: 200; text-decoration: none; display: block; margin-bottom: 15px; position: relative; text-transform: uppercase;"
        cls = "nav-link-active" if is_active else ""
        return A(text, href=href, style=style, cls=cls,
                 hx_get=href, hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true")

    return Nav(
        Div(
            A(
                Img(src=LOGO_PATH, alt="Munra Logo",
                    style="width: 100%; max-width: 260px; display: block;"),
                href="/"),
            style="margin-bottom: 50px;"
        ),
        Div(
            nav_link("grabaciones", "/grabaciones", "grabaciones"),
            nav_link("notas", "/notas", "notas"),
            nav_link("máquinas", "/maquinas", "máquinas"),
            nav_link("contacto", "/contact", "contact"),
            cls="nav-links",
            style="margin-left: 35px;"
        ),
        style=f"padding: 30px; width: {NAVBAR_WIDTH}; display: flex; flex-direction: column;",
        cls="vertical-nav"
    )


def Footer():
    """Footer component with copyright"""
    return Div(
        P(COPYRIGHT_TEXT, style=f"margin: 0; color: {COLOR_GRAY};"),
        style="font-size: 12px;",
        cls="footer"
    )
