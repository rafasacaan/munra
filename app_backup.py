from pathlib import Path
from fasthtml.common import *
from starlette.responses import RedirectResponse

app, rt = fast_app(
    hdrs=(
        Script(src="https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.js"),
        Link(rel="stylesheet", href="https://fonts.cdnfonts.com/css/pp-neue-montreal"),
        Style("""
            * {
                font-family: 'PP Neue Montreal', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            }
            html, body {
                background-color: white;
                margin: 0;
                padding: 0;
            }
            h1, h2, h3, h4, h5, h6 {
                font-family: 'PP Neue Montreal', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                text-transform: uppercase;
                text-align: left;
                font-weight: 900;
                letter-spacing: -0.08em;
            }
            h1 {
                font-size: 64px;
                line-height: 0.75;
            }
            h2 {
                font-size: 48px;
                line-height: 0.75;
            }
            .highlight-munra {
                background: linear-gradient(to right, 
                    rgba(255, 110, 199, 0.7) 0%, 
                    rgba(255, 110, 199, 0.85) 30%,
                    rgba(255, 110, 199, 0.75) 60%, 
                    rgba(255, 110, 199, 0.7) 100%);
                padding: 2px 4px;
                border-radius: 45% 12% 38% 18% / 25% 42% 15% 35%;
                display: inline-block;
                transform: rotate(-1.2deg) skewX(-0.8deg);
                box-shadow: 0 1px 3px rgba(255, 110, 199, 0.4);
                font-style: italic;
            }
            .munra-card {
                padding: 20px;
                background-color: white;
                margin: 10px;
                width: 300px;
                text-align: center;
                position: relative;
                transform: rotate(-0.6deg);
            }
            .munra-card-border {
                position: absolute;
                top: -5px;
                left: -5px;
                width: calc(100% + 10px);
                height: calc(100% + 10px);
                pointer-events: none;
            }
        """),
    )
)

######################################################################################
### Helpers
######################################################################################
def get_munra_cover(munra_name):
    # Try different image extensions
    for ext in ['jpg', 'jpeg', 'png', 'webp']:
        cover_path = Path(f"static/munras/{munra_name}/cover.{ext}")
        if cover_path.exists():
            return f"/static/munras/{munra_name}/cover.{ext}"
    return None  # No cover found

def get_munras():
    munras_dir = Path("static/munras")
    if not munras_dir.exists():
        return []
    return [d.name for d in munras_dir.iterdir() if d.is_dir()]

def get_munra_info(munra_name):
    info_file = Path(f"static/munras/{munra_name}/info.txt")
    if info_file.exists():
        return info_file.read_text()
    return "No hay información disponible."

def get_munra_tracks(munra_name):
    munra_dir = Path(f"static/munras/{munra_name}")
    if not munra_dir.exists():
        return []
    return [f.name for f in munra_dir.glob("*.mp3")]

def get_posts():
    notes_dir = Path("static/notes")
    if not notes_dir.exists():
        return []
    posts = []
    for post_dir in sorted(notes_dir.iterdir(), reverse=True):
        if post_dir.is_dir():
            meta_file = post_dir / "meta.txt"
            if meta_file.exists():
                lines = meta_file.read_text().strip().split('\n')
                posts.append({
                    'id': post_dir.name,
                    'title': lines[0] if len(lines) > 0 else post_dir.name,
                    'date': lines[1] if len(lines) > 1 else '',
                    'excerpt': lines[2] if len(lines) > 2 else ''
                })
    return posts

def get_post_content(post_id):
    content_file = Path(f"static/notes/{post_id}/content.txt")
    if content_file.exists():
        return content_file.read_text()
    return "No hay contenido disponible."

def NavBar(current_page="home", vertical=False):
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
                    Img(src="/static/munra.jpg", alt="Munra Logo", 
                        style="width: 100%; max-width: 260px; display: block;"),
                    href="/home"),
                style="margin-bottom: 50px;"
            ),
            Div(
                nav_link("home", "/home", "home"),
                nav_link("máquinas", "/maquinas", "máquinas"),
                nav_link("contacto", "/contact", "contact"),
            ),
            style="padding: 30px; width: 320px; display: flex; flex-direction: column;"
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

def PageFooter():
    return Div(
        P("© 2026 Munra - Made in Chile."),
        style="font-size: 12px; position: fixed; bottom: 0; left: 0; right: 0; text-align: center; padding: 20px; border-top: 1px solid #ccc; background-color: white; margin: 0 5%;"
    )

def Page(*content):
    return Div(*content, style="margin: 2% 6%;")


######################################################################################
### Routes
######################################################################################

@rt("/")
def get():
    return RedirectResponse("/home")


@rt("/home")
def get():
    posts = get_posts()
    left_nav = NavBar("home", vertical=True)
    
    post_list = [
        A(
            Div(
                Div(
                    P(post['title'], style="margin: 0; font-size: 14px; color: white;"),
                    style="background-color: black; padding: 4px 8px; display: inline-block;"
                ),
                style=f"aspect-ratio: 1; cursor: pointer; display: flex; align-items: center; justify-content: center; background-image: url('https://picsum.photos/seed/{hash(post['id'])}/400/400'); background-size: cover; background-position: center;"
            ),
            href=f"/notas/{post['id']}",
            style="text-decoration: none; display: block;"
        )
        for post in posts
    ]
    
    right_content = Div(
        Div(
            H1("Que", style="margin: 0; color: black;"),
            H1("es", style="margin: 0; color: black;"),
            H1("Munra", style="margin: 0 0 40px 0; color: black;"),
            style="margin-bottom: 40px;"
        ),
        Div(
            P(
                NotStr(
                "Colección de <span class='highlight-munra'>notas</span> y <span class='highlight-munra'>registros</span> creados por un humano que respira y transpira.<br>"
                "Está como acto de resistencia a algo.<br>"
                "Nosé todavía a qué.<br>"
                "<br>"
                ),
            style="font-size: 16px; line-height: 1.6; color: black; margin-bottom: 60px;"
            ),
            style="margin-left: 100px;"
        ),
        Div(
            *post_list if post_list else [P("No hay posts todavía.", style="color: #666;")],
            style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; grid-auto-flow: row;"
        ),
        Div(
            P("munra.cl © 2025", style="margin: 0; color: #999;"),
            style="margin-top: 80px; text-align: center; font-size: 12px;"
        ),
        style="flex: 1; padding: 40px; padding-right: 80px; overflow-y: auto; max-width: 1000px;"
    )
    
    layout = Div(
        left_nav,
        right_content,
        style="display: flex; height: 100vh;"
    )
    
    return Title("munra.cl"), layout

@rt("/notas")
def get():
    return RedirectResponse("/home")

@rt("/notas/{post_id}")
def get(post_id: str):
    posts = get_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    
    left_nav = NavBar("notas", vertical=True)
    
    if not post:
        right_content = Div(
            P("Post no encontrado.", style="color: #666;"),
            style="flex: 1; padding: 40px; overflow-y: auto;"
        )
        layout = Div(left_nav, right_content, style="display: flex; height: 100vh;")
        return Title("Post no encontrado"), layout
    
    content = get_post_content(post_id)
    
    right_content = Div(
        A("← volver", href="/notas", style="color: black; text-decoration: none; display: inline-block; margin-bottom: 30px; font-size: 16px;"),
        H1(post['title'], style="margin-bottom: 10px; color: black;"),
        P(post['date'], style="color: #666; font-size: 14px; margin-bottom: 40px;"),
        Div(
            P(content, style="line-height: 1.8; white-space: pre-wrap; color: black;"),
            style="margin-left: 100px;"
        ),
        Div(
            P("munra.cl © 2025", style="margin: 0; color: #999;"),
            style="margin-top: 80px; text-align: center; font-size: 12px;"
        ),
        style="flex: 1; padding: 40px; padding-right: 80px; overflow-y: auto; max-width: 1000px;"
    )
    
    layout = Div(
        left_nav,
        right_content,
        style="display: flex; height: 100vh;"
    )
    
    return Title(f"{post['title']} - munra.cl"), layout

@rt("/maquinas")
def get():
    left_nav = NavBar("maquinas", vertical=True)
    
    # Sample machines data
    machines = [
        {
            "name": "Tascam Portastudio", 
            "seed": "tascam1",
            "description": "Cuatro pistas de cinta que capturan el tiempo de manera física. El hiss como textura, no como error. Cada grabación es un acto irreversible que obliga a decidir."
        },
        {
            "name": "Akai MPC 2000XL", 
            "seed": "akai2",
            "description": "Pads sensibles a la presión que responden al tacto humano. Secuenciador que piensa en loops, no en barras infinitas. La memoria limitada como restricción creativa."
        },
        {
            "name": "Roland SP-404", 
            "seed": "roland3",
            "description": "Sampler portátil que cabe en una mochila. Efectos lo-fi que abrazan la degradación. Diseñado para ser tocado en vivo, no programado en silencio."
        },
        {
            "name": "Technics SL-1200", 
            "seed": "technics4",
            "description": "Tornamesa de tracción directa construida como tanque. El vinilo como formato físico irremplazable. Scratchear es tocar un instrumento, no reproducir audio."
        },
        {
            "name": "Korg Volca Keys", 
            "seed": "korg5",
            "description": "Sintetizador análogo que cabe en la palma de la mano. Perillas físicas para cada parámetro esencial. Lo pequeño no es limitación, es enfoque."
        },
        {
            "name": "Teenage Engineering OP-1", 
            "seed": "teenage6",
            "description": "Estudio completo con batería incorporada. Limitaciones de grabación que fuerzan creatividad. Diseño que invita a explorar, no a optimizar."
        },
    ]
    
    machine_grid = [
        Div(
            Img(src=f"https://picsum.photos/seed/{m['seed']}/600/400", 
                style="width: 100%; display: block; object-fit: cover;"),
            Div(
                P(m['name'], style="margin: 0 0 10px 0; font-size: 16px; font-weight: bold; color: black;"),
                P(m['description'], style="margin: 0; font-size: 14px; line-height: 1.6; color: black;"),
                style="padding: 15px; background-color: white;"
            ),
            style="background-color: white; margin-bottom: 30px;"
        )
        for m in machines
    ]
    
    right_content = Div(
        H1("Maquinas", style="margin-bottom: 40px; color: black;"),
        Div(
            P(
                "Herramientas físicas que respiran. Cada una con su carácter, sus imperfecciones, su manera de hablar. "
                "Resistencia a la perfección digital. Lo análogo como acto político.",
                style="font-size: 16px; line-height: 1.6; color: black; margin-bottom: 60px;"
            ),
            style="margin-left: 100px;"
        ),
        Div(
            *machine_grid,
            style="display: grid; grid-template-columns: 1fr; gap: 0;"
        ),
        Div(
            P("munra.cl © 2026", style="margin: 0; color: #999;"),
            style="margin-top: 80px; text-align: center; font-size: 12px;"
        ),
        style="flex: 1; padding: 40px; padding-right: 80px; overflow-y: auto; max-width: 1000px;"
    )
    
    layout = Div(
        left_nav,
        right_content,
        style="display: flex; height: 100vh;"
    )
    
    return Title("Máquinas - munra.cl"), layout

@rt("/contact")
def get():
    left_nav = NavBar("contact", vertical=True)
    
    right_content = Div(
        H1("Contacto", style="margin-bottom: 40px; color: black;"),
        Div(
            P("Hola! Puedes escribirnos a xxxxx@xxx.com", style="font-size: 16px; line-height: 1.6; color: black;"),
            style="margin-left: 100px;"
        ),
        Div(
            P("munra.cl © 2026", style="margin: 0; color: #999;"),
            style="margin-top: 80px; text-align: center; font-size: 12px;"
        ),
        style="flex: 1; padding: 40px; padding-right: 80px; overflow-y: auto; max-width: 1000px;"
    )
    
    layout = Div(
        left_nav,
        right_content,
        style="display: flex; height: 100vh;"
    )
    
    return Title("munra.cl"), layout

@rt("/contact")
def get():
    left_nav = NavBar("contact", vertical=True)
    
    right_content = Div(
        H1("Contacto", style="margin-bottom: 40px; color: black;"),
        Div(
            P("Hola! Puedes escribirnos a xxxxx@xxx.com", style="font-size: 16px; line-height: 1.6; color: black;"),
            style="margin-left: 100px;"
        ),
        Div(
            P("munra.cl © 2026", style="margin: 0; color: #999;"),
            style="margin-top: 80px; text-align: center; font-size: 12px;"
        ),
        style="flex: 1; padding: 40px; padding-right: 80px; overflow-y: auto; max-width: 1000px;"
    )
    
    layout = Div(
        left_nav,
        right_content,
        style="display: flex; height: 100vh;"
    )
    
    return Title("munra.cl"), layout


serve()