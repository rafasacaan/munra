"""Page layout templates"""

from fasthtml.common import *
from components import NavBar, Footer
from config import BG_VIDEO_PATH


def HeroSection(eyebrow="", title="", subtitle="", cta_text="", cta_href=""):
    """Full-viewport hero with video background"""
    hero_inner = []
    if eyebrow:
        hero_inner.append(Span(eyebrow, cls="hero-eyebrow"))
    if title:
        hero_inner.append(NotStr(f'<span class="hero-title">{title}</span>'))
    if subtitle:
        hero_inner.append(P(subtitle, cls="hero-subtitle"))
    if cta_text:
        hero_inner.append(
            A(cta_text, href=cta_href, cls="hero-cta",
              hx_get=cta_href, hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true"))

    return Div(
        NotStr(
            f'<video class="hero-video" autoplay loop muted playsinline>'
            f'<source src="{BG_VIDEO_PATH}" type="video/mp4">'
            f'</video>'
        ),
        Div(cls="hero-overlay"),
        Div(*hero_inner, cls="hero-content"),
        NotStr('<div class="scroll-indicator"><span></span></div>'),
        cls="hero-section"
    )


def ContentArea(content, section_name=""):
    """Inner content for non-home HTMX swaps"""
    return (
        Div(H1(section_name, cls="page-header"), *content, cls="content-wrapper"),
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
    """Standard page: navbar + H1 + content + footer"""
    return Div(
        NavBar(current_page),
        Div(
            Div(H1(section_name, cls="page-header"), *content, cls="content-wrapper"),
            Footer(),
            id="content-area",
        ),
    )


def HomeLayout(current_page, content, **hero_kwargs):
    """Home page: navbar + hero + content + footer"""
    return Div(
        NavBar(current_page),
        Div(
            HeroSection(**hero_kwargs),
            Div(*content, cls="content-wrapper"),
            Footer(),
            id="content-area",
        ),
    )
