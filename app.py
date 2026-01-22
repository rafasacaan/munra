"""Main application file"""

from fasthtml.common import *
from starlette.responses import RedirectResponse

from styles import GLOBAL_STYLES
from layouts import TwoColumnLayout
from components import PostCard, MachineCard, ContentSection
from data.posts import get_posts, get_post_content, get_post_by_id
from data.machines import get_machines
from utils import get_meta_tags
from config import FONT_URL, POST_GRID_COLUMNS, MACHINE_GRID_COLUMNS, SITE_NAME

# Initialize FastHTML app
app, rt = fast_app(
    hdrs=(
        Script(src="https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.js"),
        Link(rel="stylesheet", href=FONT_URL),
        Style(GLOBAL_STYLES),
        *get_meta_tags(),
    )
)
# Routes
@rt("/")
def get():
    """Redirect to home page"""
    return RedirectResponse("/home")


@rt("/home")
def get():
    """Home page with posts grid"""
    posts = get_posts()
    post_list = [PostCard(post) for post in posts]
    
    content = [
        Div(
            H1("Que", style="margin: 0; color: black;"),
            H1("es", style="margin: 0; color: black;"),
            H1("Munra", style="margin: 0 0 40px 0; color: black;"),
            style="margin-bottom: 40px;"
        ),
        ContentSection(
            P(
                NotStr(
                    "Colección de <span class='highlight-munra'>notas</span> y "
                    "<span class='highlight-munra'>registros</span> creados por un humano que respira y transpira.<br>"
                    "Está como acto de resistencia a algo.<br>"
                    "Nosé todavía a qué.<br>"
                    "<br>"
                ),
                style="font-size: 16px; line-height: 1.6; color: black; margin-bottom: 60px;"
            )
        ),
        Div(
            *post_list if post_list else [P("No hay posts todavía.", style="color: #666;")],
            style=f"display: grid; grid-template-columns: repeat({POST_GRID_COLUMNS}, 1fr); gap: 10px; grid-auto-flow: row;",
            cls="post-grid"
        ),
    ]
    
    return TwoColumnLayout("home", content, SITE_NAME)


@rt("/notas")
def get():
    """Redirect to home page"""
    return RedirectResponse("/home")


@rt("/notas/{post_id}")
def get(post_id: str):
    """Individual post page"""
    post = get_post_by_id(post_id)
    
    if not post:
        content = [P("Post no encontrado.", style="color: #666;")]
        return TwoColumnLayout("notas", content, "Post no encontrado")
    
    post_content = get_post_content(post_id)
    
    content = [
        A("← volver", href="/notas", 
          style="color: black; text-decoration: none; display: inline-block; margin-bottom: 30px; font-size: 16px;"),
        H1(post['title'], style="margin-bottom: 10px; color: black;"),
        P(post['date'], style="color: #666; font-size: 14px; margin-bottom: 40px;"),
        ContentSection(
            P(post_content, style="line-height: 1.8; white-space: pre-wrap; color: black;")
        ),
    ]
    
    return TwoColumnLayout("notas", content, f"{post['title']} - munra.cl")


@rt("/maquinas")
def get():
    """Machines page"""
    machines = get_machines()
    machine_cards = [MachineCard(m) for m in machines]
    
    content = [
        H1("Maquinas", style="margin-bottom: 40px; color: black;"),
        ContentSection(
            P(
                "Herramientas físicas que respiran. Cada una con su carácter, sus imperfecciones, su manera de hablar. "
                "Resistencia a la perfección digital. Lo análogo como acto político.",
                style="font-size: 16px; line-height: 1.6; color: black; margin-bottom: 60px;"
            )
        ),
        Div(
            *machine_cards,
            style=f"display: grid; grid-template-columns: repeat({MACHINE_GRID_COLUMNS}, 1fr); gap: 0;"
        ),
    ]
    
    return TwoColumnLayout("máquinas", content, "Máquinas - munra.cl")


@rt("/contact")
def get():
    """Contact page"""
    content = [
        H1("Contacto", style="margin-bottom: 40px; color: black;"),
        ContentSection(
            P("Hola! Puedes escribirnos a xxxxx@xxx.com", 
              style="font-size: 16px; line-height: 1.6; color: black;")
        ),
    ]
    
    return TwoColumnLayout("contact", content, SITE_NAME)


@app.exception_handler(404)
async def not_found(request, exc):
    """Custom 404 page"""
    content = [
        Div(
            H1("404", style="margin: 0 0 20px 0; color: black;"),
            H2("Página no encontrada", style="margin: 0 0 40px 0; color: black;"),
            style="margin-bottom: 40px;"
        ),
        ContentSection(
            P(
                "La página que buscas no existe. Tal vez nunca existió. O tal vez es parte del vacío digital.",
                style="font-size: 16px; line-height: 1.6; color: black; margin-bottom: 30px;"
            ),
            A("← Volver al inicio", href="/home", 
              style="color: black; text-decoration: underline; font-size: 16px;")
        ),
    ]
    
    return TwoColumnLayout("404", content, "404 - Página no encontrada")


# Start the server
serve()
