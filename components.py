"""Reusable UI components"""

from fasthtml.common import *
from config import (
    NAVBAR_WIDTH, LOGO_PATH, COLOR_BLACK, COLOR_WHITE,
    CONTENT_OFFSET, COPYRIGHT_TEXT, PICSUM_BASE_URL, COLOR_GRAY
)


def NavBar(current_page="home", vertical=False):
    """Navigation bar component"""
    def nav_link(text, href, page_name):
        is_active = current_page == page_name
        if vertical:
            style = "color: black; font-size: 18px; text-decoration: none; display: block; margin-bottom: 15px; position: relative;"
        else:
            style = "color: black; font-size: 20px; text-decoration: none; margin-left: 100px; position: relative; display: inline-block;"
        cls = "nav-link-active" if is_active else ""
        return A(text, href=href, style=style, cls=cls)
    
    if vertical:
        return Nav(
            Div(
                A(
                    Img(src=LOGO_PATH, alt="Munra Logo", 
                        style="width: 100%; max-width: 260px; display: block;"),
                    href="/home"),
                style="margin-bottom: 50px;"
            ),
            Div(
                nav_link("home", "/home", "home"),
                nav_link("máquinas", "/maquinas", "máquinas"),
                nav_link("contacto", "/contact", "contact"),
            ),
            style=f"padding: 30px; width: {NAVBAR_WIDTH}; display: flex; flex-direction: column;",
            cls="vertical-nav"
        )
    
    return Nav(
        Div(
            # Logo on the left
            A(
                Img(src="/static/munra.jpg", alt="Munra Logo", 
                    style="width: 20%; max-width: 50%; display: block;"),
                href="/"),
            
            # Links below the logo
            Div(
                A("munras", href="/", 
                style="color: black; font-size: 20px; text-decoration: none; position: relative; display: inline-block;",
                cls="nav-link-active" if current_page == 'munras' else ""),
                nav_link("qué es", "/que-es", "que-es"),
                nav_link("contacto", "/contact", "contact"),
                style="display: flex; margin-top: 20px;"),
            
            style="display: flex; flex-direction: column; padding: 20px; width: 100%;"),
        style="margin: 2% 5%;"
    )


def Footer():
    """Footer component with copyright"""
    return Div(
        P(COPYRIGHT_TEXT, style=f"margin: 0; color: {COLOR_GRAY};"),
        style="margin-top: 80px; text-align: center; font-size: 12px;"
    )


def PostCard(post):
    """Card component for displaying a post in the grid"""
    return A(
        Div(
            Div(
                P(post['title'], style=f"margin: 0; font-size: 14px; color: {COLOR_WHITE};"),
                style=f"background-color: {COLOR_BLACK}; padding: 4px 8px; display: inline-block;"
            ),
            style=f"aspect-ratio: 1; cursor: pointer; display: flex; align-items: center; justify-content: center; background-image: url('{PICSUM_BASE_URL}/seed/{hash(post['id'])}/400/400'); background-size: cover; background-position: center;"
        ),
        href=f"/notas/{post['id']}",
        style="text-decoration: none; display: block;"
    )


def MachineCard(machine):
    """Card component for displaying a machine"""
    return Div(
        Img(src=f"{PICSUM_BASE_URL}/seed/{machine['seed']}/600/400", 
            style="width: 100%; display: block; object-fit: cover;"),
        Div(
            P(machine['name'], style=f"margin: 0 0 10px 0; font-size: 16px; font-weight: bold; color: {COLOR_BLACK};"),
            P(machine['description'], style=f"margin: 0; font-size: 14px; line-height: 1.6; color: {COLOR_BLACK};"),
            style=f"padding: 15px; background-color: {COLOR_WHITE};"
        ),
        style=f"background-color: {COLOR_WHITE}; margin-bottom: 30px;"
    )


def ContentSection(*content, offset=True):
    """Wrapper for content with optional left margin offset"""
    if offset:
        return Div(*content, cls="content-section")
    return Div(*content)
