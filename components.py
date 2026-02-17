"""Reusable UI components"""

from fasthtml.common import *
from config import LOGO_PATH, COPYRIGHT_TEXT, COLOR_GRAY


def NavBar(current_page="home"):
    """Horizontal top navigation bar"""
    def nav_link(text, href, page_name):
        cls = "nav-link-active" if current_page == page_name else ""
        return A(text, href=href, cls=cls,
                 hx_get=href, hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true")

    return Nav(
        Div(
            A(Img(src=LOGO_PATH, alt="Munra Logo", cls="nav-logo"),
              href="/", hx_get="/", hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true"),
            Div(
                nav_link("Blog", "/blog", "blog"),
                nav_link("Models", "/models", "models"),
                nav_link("Recordings", "/recordings", "recordings"),
                nav_link("About", "/about", "about"),
                cls="nav-links",
            ),
            cls="nav-inner",
        ),
        cls="top-nav"
    )


def Footer():
    """Footer component"""
    return Div(
        P(COPYRIGHT_TEXT, style=f"margin: 0; color: {COLOR_GRAY};"),
        cls="footer"
    )


def PostItem(post):
    """Reusable post list item for blog listing and home page"""
    return A(
        Div(
            P(post['title'], cls="post-title"),
            P(post['date'], cls="post-date"),
            P(post['excerpt'], cls="post-excerpt"),
            cls="post-item-inner",
        ),
        href=f"/blog/{post['id']}",
        cls="post-item",
        hx_get=f"/blog/{post['id']}", hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true",
    )
