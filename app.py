"""Main application file"""

from fasthtml.common import *

from styles import GLOBAL_STYLES
from layouts import TwoColumnLayout, ContentArea
from utils import get_meta_tags, get_google_analytics
from config import FONT_URL, SITE_NAME, FAVICON_PATH, CONTACT_EMAIL

# Initialize FastHTML app
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


# Routes
@rt("/")
def get(request):
    """Home page"""
    home_title = NotStr("Estudio de creación de audio<br>análogo y experimental .")
    content = []
    if request.headers.get("HX-Request"):
        return ContentArea(content, home_title)
    return Title(SITE_NAME), TwoColumnLayout("home", content, section_name=home_title)


@rt("/grabaciones")
def get(request):
    """Grabaciones page"""
    content = [P("Próximamente...", style="font-size: 18px; font-weight: 300; color: white;")]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Grabaciones")
    return Title("Grabaciones - munra.cl"), TwoColumnLayout("grabaciones", content, section_name="Grabaciones")


@rt("/notas")
def get(request):
    """Notas page"""
    content = [P("Próximamente...", style="font-size: 18px; font-weight: 300; color: white;")]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Notas")
    return Title("Notas - munra.cl"), TwoColumnLayout("notas", content, section_name="Notas")


@rt("/maquinas")
def get(request):
    """Machines page"""
    content = [P("Próximamente...", style="font-size: 18px; font-weight: 300; color: white;")]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Máquinas")
    return Title("Máquinas - munra.cl"), TwoColumnLayout("máquinas", content, section_name="Máquinas")


@rt("/contact")
def get(request):
    """Contact page"""
    content = [
        P(f"Escríbenos a {CONTACT_EMAIL.replace('@', ' at ')}",
          style="font-size: 18px; font-weight: 300; color: white;"),
    ]
    if request.headers.get("HX-Request"):
        return ContentArea(content, "Contacto")
    return Title(SITE_NAME), TwoColumnLayout("contact", content, section_name="Contacto")


@app.exception_handler(404)
async def not_found(request, exc):
    """Custom 404 page"""
    content = [
        P("La página que buscas no existe.",
          style="font-size: 18px; font-weight: 300; color: white; margin-bottom: 30px;"),
        A("← Volver al inicio", href="/",
          style="color: white; text-decoration: underline; font-size: 16px;"),
    ]

    return Title("404 - Página no encontrada"), TwoColumnLayout("404", content, section_name="404")


# Start the server
serve()
