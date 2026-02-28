"""Reusable UI components"""

from fasthtml.common import *
from config import LOGO_PATH, COPYRIGHT_TEXT, COLOR_TEXT_SEC, COLOR_BORDER


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
                nav_link("Samples", "/samples", "samples"),
                nav_link("Models", "/models", "models"),
                nav_link("Experiments", "/blog", "blog"),
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
        P(COPYRIGHT_TEXT, style=f"margin: 0; color: {COLOR_TEXT_SEC};"),
        Div(
            A("Bandcamp", href="https://munra.bandcamp.com", target="_blank", rel="noopener noreferrer",
              style=f"color: {COLOR_TEXT_SEC}; text-decoration: none;"),
            Span("·", style=f"color: {COLOR_BORDER}; margin: 0 0.5rem;"),
            A("GitHub", href="https://github.com/rafasacaan/munra-dev", target="_blank", rel="noopener noreferrer",
              style=f"color: {COLOR_TEXT_SEC}; text-decoration: none;"),
            style="margin-top: 0.25rem;",
        ),
        cls="footer"
    )


def FeaturedProject(post):
    """Featured latest project on the homepage"""
    return Div(
        P("Latest", cls="featured-label"),
        P(post['title'], cls="featured-title"),
        P(post['date'], cls="featured-date"),
        P(post['excerpt'], cls="featured-excerpt"),
        A("Read more \u2192", href=f"/blog/{post['id']}", cls="featured-link",
          hx_get=f"/blog/{post['id']}", hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true"),
        cls="featured",
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
