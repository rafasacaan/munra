"""Page layout templates"""

from fasthtml.common import *
from components import NavBar, Footer
from config import BG_VIDEO_PATH

SVG_FILTERS = NotStr('''<svg width="0" height="0" style="position:absolute;overflow:hidden" aria-hidden="true">
  <defs>
    <filter id="rough-highlight" x="-8%" y="-40%" width="116%" height="180%">
      <feTurbulence type="turbulence" baseFrequency="0.03 0.09" numOctaves="4" seed="7" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="5" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </defs>
</svg>''')


def HeroSection(eyebrow="", title="", ctas=[]):
    """Full-height typographic hero"""
    top = []
    if eyebrow:
        top.append(Span(eyebrow, cls="hero-eyebrow"))
    if title:
        top.append(NotStr(f'<span class="hero-title">{title}</span>'))

    cta_links = []
    for text, href in ctas:
        if href.startswith("http"):
            cta_links.append(A(f"{text} →", href=href, cls="hero-cta", target="_blank", rel="noopener noreferrer"))
        else:
            cta_links.append(A(f"{text} →", href=href, cls="hero-cta",
                               hx_get=href, hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true"))

    bottom = Div(
        Div(*cta_links, cls="hero-cta-group"),
        cls="hero-bottom",
    )

    update = A(
        "● March 2026 / Just dropped: 87 kicks, snares & hi-hats from an 808 drum machine — listen on Bandcamp",
        href="https://munra.bandcamp.com",
        cls="hero-update",
        target="_blank",
        rel="noopener noreferrer",
    )

    return Div(
        Div(
            Div(
                NotStr(f'<video autoplay muted loop playsinline class="hero-video"><source src="{BG_VIDEO_PATH}" type="video/mp4"></video>'),
                Div(cls="hero-overlay"),
                Div(
                    Div(
                        Div(*top, cls="hero-top"),
                        update,
                        Div(Hr(cls="hero-rule"), bottom),
                        cls="hero-text-inner",
                    ),
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
        SVG_FILTERS,
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
        SVG_FILTERS,
        NavBar(current_page),
        Div(
            HeroSection(**hero_kwargs),
            Div(*content, cls="content-wrapper"),
            Footer(),
            id="content-area",
        ),
    )
