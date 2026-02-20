"""Page layout templates"""

from fasthtml.common import *
from components import NavBar, Footer
from config import BG_VIDEO_PATH


def HeroSection(eyebrow="", title="", subtitle="", ctas=[]):
    """Full-height typographic hero"""
    top = []
    if eyebrow:
        top.append(Span(eyebrow, cls="hero-eyebrow"))
    if title:
        top.append(NotStr(f'<span class="hero-title">{title}</span>'))

    cta_links = [
        A(f"{text} →", href=href, cls="hero-cta",
          hx_get=href, hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true")
        for text, href in ctas
    ]

    bottom = Div(
        Span(subtitle, cls="hero-subtitle") if subtitle else Span(),
        Div(*cta_links, cls="hero-cta-group"),
        cls="hero-bottom",
    )

    return Div(
        Div(
            Div(
                NotStr(f'<video autoplay muted loop playsinline class="hero-video"><source src="{BG_VIDEO_PATH}" type="video/mp4"></video>'),
                Div(cls="hero-overlay"),
                Div(
                    Div(*top, cls="hero-top"),
                    Div(Hr(cls="hero-rule"), bottom),
                    cls="hero-text",
                ),
                cls="hero-video-wrap",
            ),
            cls="hero-content",
        ),
        cls="hero-section",
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
