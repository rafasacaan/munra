"""Page layout templates"""

from fasthtml.common import *
from components import NavBar, Footer
from config import BG_VIDEO_PATH


def HeroSection(eyebrow="", title=""):
    """Compact hero with video background"""
    hero_inner = []
    if eyebrow:
        hero_inner.append(Span(eyebrow, cls="hero-eyebrow"))
    if title:
        hero_inner.append(NotStr(f'<span class="hero-title">{title}</span>'))

    return Div(
        NotStr(
            f'<video class="hero-video" autoplay loop muted playsinline>'
            f'<source src="{BG_VIDEO_PATH}" type="video/mp4">'
            f'</video>'
        ),
        Div(cls="hero-overlay"),
        Div(*hero_inner, cls="hero-content"),
        cls="hero-section"
    )


def ContentArea(content, section_name=""):
    """Inner content for HTMX swaps"""
    header = [H1(section_name, cls="page-header")] if section_name else []
    return (
        Div(*header, *content, cls="content-wrapper"),
        Footer(),
    )


def HomeContentArea(content, **hero_kwargs):
    """Inner content for home HTMX swaps"""
    return (
        HeroSection(**hero_kwargs),
        Div(*content, cls="content-wrapper"),
        Footer(),
    )


def PageLayout(current_page, content, section_name=""):
    """Standard page: navbar + content + footer"""
    header = [H1(section_name, cls="page-header")] if section_name else []
    return Div(
        NavBar(current_page),
        Div(
            Div(*header, *content, cls="content-wrapper"),
            Footer(),
            id="content-area",
        ),
    )


def HomeLayout(current_page, content, **hero_kwargs):
    """Home page: navbar + compact hero + content + footer"""
    return Div(
        NavBar(current_page),
        Div(
            HeroSection(**hero_kwargs),
            Div(*content, cls="content-wrapper"),
            Footer(),
            id="content-area",
        ),
    )
