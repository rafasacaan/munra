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
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
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
        content.append(
            Div(
                Div(
                    P(Span("MUNRA", cls="highlighter"), " started in February 2026 as a way to learn audio ML by doing it. Instead of just reading papers, I'm training tiny models from scratch—recording samples, building codecs, documenting every step.", cls="post-body"),
                    P("The goal: create generative tools for my own experimental music, and share the entire process openly. Samples, models, failures, and insights—all public.", cls="post-body"),
                    cls="home-intro-text",
                ),
                Div(
                    Div(Span("Samples recorded", cls="stat-label"), Span("120", cls="stat-value"), cls="stat-badge"),
                    Div(Span("Models trained", cls="stat-label"), Span("0", cls="stat-value"), cls="stat-badge"),
                    Div(Span("Experiments", cls="stat-label"), Span("0", cls="stat-value"), cls="stat-badge"),
                    cls="stat-grid",
                ),
                cls="home-intro",
            )
        )

    if request.headers.get("HX-Request"):
        return HomeContentArea(content, **HERO)
    return Title(SITE_NAME), HomeLayout("home", content, **HERO)


@rt("/blog")
def get(request):
    """Blog listing page"""
    content = [
        P("Documenting the complete process of building generative audio models from scratch. Every experiment, success, and failure.", cls="post-body"),

        Div(
            Div(
                P("Experiment #001", cls="produce-card-title"),
                P("Audio Compression — Building a neural audio codec to represent sound as discrete tokens.", cls="produce-card-desc"),
                P("Active — 40% complete", cls="produce-card-status"),
            cls="produce-card"),
            Div(
                P("Experiment #002", cls="produce-card-title"),
                P("Perceptual Loss Functions — Exploring loss functions that optimize for human perception.", cls="produce-card-desc"),
                P("Planned", cls="produce-card-status"),
            cls="produce-card"),
            Div(
                P("Experiment #003", cls="produce-card-title"),
                P("Vector Quantization — Discrete representation of audio for generative modeling.", cls="produce-card-desc"),
                P("Planned", cls="produce-card-status"),
            cls="produce-card"),
            Div(
                P("Experiment #004", cls="produce-card-title"),
                P("Hierarchical Representation — Multi-scale audio encoding for richer generation.", cls="produce-card-desc"),
                P("Planned", cls="produce-card-status"),
            cls="produce-card"),
            cls="produce-grid",
        ),
    ]
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


@rt("/samples")
def get(request):
    """Samples page"""
    content = [
        P(Span("MUNRA", cls="highlighter"), " builds a library of unique audio samples recorded specifically for training generative models. All samples are also available for direct use in music production.", cls="post-body"),

        Div(
            *[Div(Img(src=f"/static/imgs/machines/{name}", alt=name.replace("machines-", "").replace(".jpg", ""), loading="lazy"), cls="machines-grid-item")
              for name in [
                "machines-pedals.jpg", "machines-tascam-digi.jpg", "machines-808.jpg",
                "machines-tascam-4track.jpg", "machines-walkmans.jpg", "machines-sony-1track.jpg",
                "machines-cassettes.jpg", "machines-jhs.jpg", "machines-synths.jpg",
                "machines-mics.jpg", "machines-keys.jpg",
              ]],
            cls="machines-grid",
        ),

        Div(
            Div(
                H2("Recording Philosophy", cls="post-h2"),
                P('Unlike commercial sample libraries that aim for "perfection," these samples embrace imperfection: room tone, analog character, timing inconsistencies.', cls="post-body"),
                P("Every sample is:", cls="post-body"),
                Ul(
                    Li("Recorded by hand"),
                    Li("Documented with metadata"),
                    Li("Used to train our models"),
                    Li("Free to use with attribution"),
                    cls="post-list",
                ),

                H2("Download", cls="post-h2"),
                P("Coming Soon — First pack releasing March 2026", cls="post-body"),

            ),
            Div(
                H2("Current Library", cls="post-h2"),
                P(Strong("Status:"), " In progress (target: 2,000+)", cls="post-body"),
                P(Strong("License:"), " CC-BY 4.0", cls="post-body"),
                P(Strong("Format:"), " WAV, 48kHz, 24-bit", cls="post-body"),

                H3("Categories", cls="post-h3"),
                P(Strong("Drums"), " (coming soon)", cls="post-body"),
                P(Strong("Voice"), " (coming soon)", cls="post-body"),
                P(Strong("Synths"), " (coming soon)", cls="post-body"),
            ),
            cls="home-intro",
        ),
    ]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Samples")
    return Title(f"Samples - {SITE_NAME}"), PageLayout("samples", content, section_name="Samples")


@rt("/models")
def get(request):
    """Models page"""
    content = [
        P(Span("MUNRA", cls="highlighter"), " trains tiny neural networks (<50M params) to generate audio for creative music production.", cls="post-body"),

        H2("Philosophy", cls="post-h2"),
        P("Most audio AI optimizes for perfection. ", Span("MUNRA", cls="highlighter"), " optimizes for character:", cls="post-body"),
        Ul(
            Li("Lo-fi aesthetic (tape, vinyl, imperfection)"),
            Li("Tiny models (trainable on single GPU)"),
            Li("Open source (models, weights, training process)"),
            cls="post-list",
        ),

        H2("Planned Models", cls="post-h2"),

        Div(
            Div(
                P("Drummer", cls="produce-card-title"),
                P("Generates drum loops and percussion. Trained on found sounds and acoustic objects.", cls="produce-card-desc"),
                P("Work in progress — ~20M params", cls="produce-card-status"),
            cls="produce-card"),
            Div(
                P("Voice Reciter", cls="produce-card-title"),
                P("Generates spoken word and vocal textures. Trained on recitations and phonemes.", cls="produce-card-desc"),
                P("Work in progress — ~28M params", cls="produce-card-status"),
            cls="produce-card"),
            Div(
                P("Drone Generator", cls="produce-card-title"),
                P("Generates pads and evolving textures. Trained on synths and guitar feedback.", cls="produce-card-desc"),
                P("Work in progress — ~22M params", cls="produce-card-status"),
            cls="produce-card"),
            cls="produce-grid",
        ),

        H2("Follow Progress", cls="post-h2"),
        P("Each model's development is documented in experiments.", cls="post-body"),
        A("View experiments →", href="/blog", cls="featured-link",
          hx_get="/blog", hx_target="#content-area", hx_swap="innerHTML", hx_push_url="true"),
    ]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Models")
    return Title(f"Models - {SITE_NAME}"), PageLayout("models", content, section_name="Models")


@rt("/about")
def get(request):
    """About page"""
    content = [
        P(Span("MUNRA", cls="highlighter"), " is a personal audio ML research lab exploring generative models for creative music production.", cls="post-body"),

        H2("What We Produce", cls="post-h2"),

        Div(
            Div(
                P("Audio Samples & Loops", cls="produce-card-title"),
                P("A growing library of unique recordings: drums, voice, and synths. Used for training models and available for direct use.", cls="produce-card-desc"),
                P("In progress — Target: 2,000+", cls="produce-card-status"),
            cls="produce-card"),
            Div(
                P("Generative Models", cls="produce-card-title"),
                P("Tiny neural networks (<50M params) that generate drums, voice, and textures. Trained on our sample library, optimized for lo-fi aesthetic.", cls="produce-card-desc"),
                P("In development — First model: June 2026", cls="produce-card-status"),
            cls="produce-card"),
            Div(
                P("Documented Process", cls="produce-card-title"),
                P("Every experiment is documented publicly: architecture decisions, failures, breakthroughs, insights. Complete transparency.", cls="produce-card-desc"),
                P("Experiment #001 in progress", cls="produce-card-status"),
            cls="produce-card"),
            cls="produce-grid",
        ),

        H2("Why This Approach", cls="post-h2"),
        P("Most audio AI optimizes for perfection: pristine, studio-quality output. ", Span("MUNRA", cls="highlighter"), " does the opposite.", cls="post-body"),
        P("We train on imperfect, characterful audio: tape hiss, vinyl crackle, timing drift. The goal isn't to replace musicians, but to create unique building blocks for experimental music.", cls="post-body"),

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
