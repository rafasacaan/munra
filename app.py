"""Main application file"""

from fasthtml.common import *
from starlette.responses import HTMLResponse

from styles import GLOBAL_STYLES, PYGMENTS_CSS
from layouts import PageLayout, HomeLayout, ContentArea, HomeContentArea
from components import PostItem, FeaturedProject
from rendering import render_post_body
from utils import get_meta_tags, get_google_analytics
from config import FONT_URL, SITE_NAME, FAVICON_PATH, HERO_EYEBROW, HERO_TITLE, HERO_CTAS
from data.posts import get_posts, get_post_by_id, get_post_content

app, rt = fast_app(
    hdrs=(
        Link(rel="icon", type="image/jpeg", href=FAVICON_PATH),
        Link(rel="stylesheet", href=FONT_URL),
        Style(GLOBAL_STYLES + PYGMENTS_CSS),
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

HERO = dict(eyebrow=HERO_EYEBROW, title=HERO_TITLE, ctas=HERO_CTAS)


@rt("/")
def get(request):
    """Home page"""
    posts = get_posts()
    featured = posts[0] if posts else None
    rest = posts[1:] if len(posts) > 1 else []

    content = []
    if featured:
        content.append(FeaturedProject(featured))
    if rest:
        content.append(Div("Experiments", cls="section-label"))
        content.extend([PostItem(p) for p in rest])
    elif not featured:
        content.append(Span("Work in progress", cls="wip-badge"))

    if request.headers.get("HX-Request"):
        return HomeContentArea(content, **HERO)
    return Title(SITE_NAME), HomeLayout("home", content, **HERO)


@rt("/blog")
def get(request):
    """Blog listing page"""
    posts = get_posts()
    content = [PostItem(p) for p in posts] or [Span("Work in progress", cls="wip-badge")]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Experiments")
    return Title(f"Experiments - {SITE_NAME}"), PageLayout("blog", content, section_name="Experiments")


@rt("/blog/{post_id}")
def get(request, post_id: str):
    """Individual blog post"""
    post = get_post_by_id(post_id)
    if not post:
        content = [P("Post not found.", cls="text-placeholder")]
        if request.headers.get("HX-Request"):
            return ContentArea(content, "Experiments")
        return Title(f"Experiments - {SITE_NAME}"), PageLayout("blog", content, section_name="Experiments")

    content = [
        A("\u2190 Back to experiments", href="/blog", cls="post-back",
          hx_get="/blog", hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true"),
        P(post['date'], cls="post-meta"),
        *render_post_body(get_post_content(post_id)),
    ]
    if request.headers.get("HX-Request"):
        return ContentArea(content, post['title'])
    return Title(f"{post['title']} - {SITE_NAME}"), PageLayout("blog", content, section_name=post['title'])


@rt("/approach")
def get(request):
    """Approach page"""
    content = [
        P("MUNRA builds tiny AI models that generate audio—drum loops, spoken word, synth pads—for experimental music production.", cls="post-body"),

        H3("How It Works", cls="post-h3"),
        P('Think of it like teaching a neural network the "language" of audio:', cls="post-body"),

        Ul(
            Li(Strong("Step 1: Learn to compress"), " — First, the model learns to compress audio efficiently. Take a 4-second drum loop (64,000 numbers) and represent it as just 50 tokens. This makes generation possible on small models."),
            Li(Strong("Step 2: Learn to generate"), ' — Train a small AI to predict what comes next, like autocomplete for audio. Feed it thousands of drum loops until it learns patterns: "kick usually lands here, snare goes there."'),
            Li(Strong("Step 3: Add control"), ' — Give it instructions via text prompts. "Boom bap" or "fast hats" guides what it generates, like describing a sound to a collaborator.'),
            cls="post-list",
        ),

        H3("The Philosophy", cls="post-h3"),
        P("Most AI audio tools aim for perfection: pristine, studio-quality output. MUNRA does the opposite.", cls="post-body"),
        P("It's trained on lo-fi recordings with tape hiss, vinyl crackle, imperfect timing—the qualities that make music feel human. The goal isn't to replace musicians, but to create unique building blocks for creative work.", cls="post-body"),

        H3("What You Get", cls="post-h3"),
        P("Short samples (4-8 seconds): drum patterns, vocal textures, synth drones. Not complete songs. Not production-ready polish. Raw material for your own creative process.", cls="post-body"),
        P("Everything is documented publicly—the successes, the failures, the iterations.", cls="post-body"),
    ]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Approach")
    return Title(f"Approach - {SITE_NAME}"), PageLayout("approach", content, section_name="Approach")


@rt("/about")
def get(request):
    """About page"""
    content = [
        P("MUNRA is a personal research project exploring generative audio models.", cls="post-body"),

        H2("What I'm Building", cls="post-h2"),
        P("Tiny neural networks (<50M parameters) that generate:", cls="post-body"),
        Ul(
            Li("Drum loops and percussion"),
            Li("Spoken word / recited voice"),
            Li("Synth pads and drones"),
            cls="post-list",
        ),
        P("Not for production use. For creative experimentation.", cls="post-body"),

        H2('Why "Tiny"?', cls="post-h2"),
        Ul(
            Li("I can train them on a single GPU in days, not weeks."),
            Li("I can understand every part of the architecture."),
            Li("I can iterate quickly."),
            cls="post-list",
        ),

        H2('Why "Imperfect"?', cls="post-h2"),
        P("The best music has character: tape hiss, timing drift, vinyl crackle. I'm training models on lo-fi, vintage, human sounds—not pristine studio recordings.", cls="post-body"),

        H2("What This Isn't", cls="post-h2"),
        Ul(
            Li("Not a product (no API, no VST plugin)"),
            Li("Not competing with Suno/MusicGen"),
            Li("Not generating complete songs"),
            cls="post-list",
        ),

        H2("What This Is", cls="post-h2"),
        Ul(
            Li("Building blocks for experimental music"),
            Li("Personal learning journey documented publicly"),
            Li("Open research (code, models, failures)"),
            cls="post-list",
        ),

        H2("Timeline", cls="post-h2"),
        Ul(
            Li(Strong("Feb 2026:"), " Starting experiments"),
            Li(Strong("Jun 2026:"), " First working models"),
            Li(Strong("Dec 2026:"), " Evaluate if this is viable"),
            cls="post-list",
        ),

        H2("Contact", cls="post-h2"),
        P("Built by Rafael Sacaan.", cls="post-body"),
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
