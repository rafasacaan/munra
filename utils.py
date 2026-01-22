"""Utilities for SEO and meta tags"""

from fasthtml.common import *
from config import SITE_NAME, SITE_DESCRIPTION, SITE_URL


def get_meta_tags(title=None, description=None, image=None, url=None):
    """Generate SEO meta tags for better social sharing and search visibility"""
    page_title = f"{title} - {SITE_NAME}" if title and title != SITE_NAME else SITE_NAME
    page_description = description or SITE_DESCRIPTION
    page_url = f"{SITE_URL}{url}" if url else SITE_URL
    page_image = image or f"{SITE_URL}/static/munra.jpg"
    
    return [
        # Basic meta tags
        Meta(charset="utf-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0, maximum-scale=5.0"),
        Meta(name="description", content=page_description),
        Meta(name="keywords", content="munra, notas, registros, análogo, música, máquinas"),
        Meta(name="author", content="munra.cl"),
        Meta(name="theme-color", content="#ffffff"),
        
        # Open Graph / Facebook
        Meta(property="og:type", content="website"),
        Meta(property="og:site_name", content=SITE_NAME),
        Meta(property="og:title", content=page_title),
        Meta(property="og:description", content=page_description),
        Meta(property="og:image", content=page_image),
        Meta(property="og:image:width", content="1200"),
        Meta(property="og:image:height", content="630"),
        Meta(property="og:url", content=page_url),
        Meta(property="og:locale", content="es_ES"),
        
        # Twitter Card
        Meta(name="twitter:card", content="summary_large_image"),
        Meta(name="twitter:title", content=page_title),
        Meta(name="twitter:description", content=page_description),
        Meta(name="twitter:image", content=page_image),
    ]
