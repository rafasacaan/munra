"""Main application file"""

from fasthtml.common import *
from starlette.responses import HTMLResponse

from styles import GLOBAL_STYLES
from layouts import PageLayout, HomeLayout, ContentArea, HomeContentArea
from components import PostItem
from rendering import render_post_body
from utils import get_meta_tags, get_google_analytics
from config import (
    FONT_URL, SITE_NAME, FAVICON_PATH,
    HERO_EYEBROW, HERO_TITLE, HERO_SUBTITLE, HERO_CTA_TEXT, HERO_CTA_HREF,
)
from data.posts import get_posts, get_post_by_id, get_post_content

app, rt = fast_app(
    hdrs=(
        Link(rel="icon", type="image/jpeg", href=FAVICON_PATH),
        Link(rel="stylesheet", href=FONT_URL),
        Style(GLOBAL_STYLES),
        *get_meta_tags(),
        *get_google_analytics(),
        Script("""
            document.addEventListener('click', function(e) {
                var link = e.target.closest('.nav-links a');
                if (link) {
                    document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('nav-link-active'));
                    link.classList.add('nav-link-active');
                }
            });
        """),
    )
)

HERO = dict(
    eyebrow=HERO_EYEBROW,
    title=HERO_TITLE,
    subtitle=HERO_SUBTITLE,
    cta_text=HERO_CTA_TEXT,
    cta_href=HERO_CTA_HREF,
)


@rt("/")
def get(request):
    """Home page"""
    posts = get_posts()
    content = [
        H2("Latest posts", style="font-size: 28px; font-weight: 300; color: white; margin: 0 0 20px 0; letter-spacing: normal;"),
        *[PostItem(p) for p in posts],
    ]
    if request.headers.get("HX-Request"):
        return HomeContentArea(content, **HERO)
    return Title(SITE_NAME), HomeLayout("home", content, **HERO)


@rt("/blog")
def get(request):
    """Blog listing page"""
    posts = get_posts()
    content = [PostItem(p) for p in posts] or [P("No posts yet.", cls="text-placeholder")]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Blog")
    return Title(f"Blog - {SITE_NAME}"), PageLayout("blog", content, section_name="Blog")


@rt("/blog/{post_id}")
def get(request, post_id: str):
    """Individual blog post"""
    post = get_post_by_id(post_id)
    if not post:
        content = [P("Post not found.", cls="text-placeholder")]
        if request.headers.get("HX-Request"):
            return ContentArea(content, "Blog")
        return Title(f"Blog - {SITE_NAME}"), PageLayout("blog", content, section_name="Blog")

    content = [
        A("\u2190 Back to blog", href="/blog", cls="post-back",
          hx_get="/blog", hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true"),
        P(post['date'], cls="post-meta"),
        *render_post_body(get_post_content(post_id)),
    ]
    if request.headers.get("HX-Request"):
        return ContentArea(content, post['title'])
    return Title(f"{post['title']} - {SITE_NAME}"), PageLayout("blog", content, section_name=post['title'])


@rt("/models")
def get(request):
    """Models page"""
    content = [P("Coming soon...", cls="text-placeholder")]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Models")
    return Title(f"Models - {SITE_NAME}"), PageLayout("models", content, section_name="Models")


@rt("/recordings")
def get(request):
    """Recordings page"""
    content = [P("Coming soon...", cls="text-placeholder")]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Recordings")
    return Title(f"Recordings - {SITE_NAME}"), PageLayout("recordings", content, section_name="Recordings")


@rt("/about")
def get(request):
    """About page"""
    content = [
        P("AI-driven audio research lab exploring the intersection of generative models and sound.",
          cls="text-placeholder"),
    ]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "About")
    return Title(f"About - {SITE_NAME}"), PageLayout("about", content, section_name="About")


@app.exception_handler(404)
async def not_found(request, exc):
    """Custom 404 page"""
    content = [
        P("The page you're looking for doesn't exist.", cls="text-placeholder",
          style="margin-bottom: 30px;"),
        A("\u2190 Back to home", href="/",
          style="color: white; text-decoration: underline; font-size: 16px;"),
    ]
    page = (Title("404 - Page not found"), PageLayout("404", content, section_name="404"))
    return HTMLResponse(to_xml(page), status_code=404)


serve()
