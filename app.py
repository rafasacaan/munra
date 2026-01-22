from pathlib import Path
from fasthtml.common import *

app, rt = fast_app(
    hdrs=(
        Script(src="https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.js"),
        Style("""
            * {
                font-family: monospace;
            }
            html, body {
                background-color: white;
                margin: 0;
                padding: 0;
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

def NavBar(current_page="home"):
    def nav_link(text, href, page_name):
        is_active = current_page == page_name
        style = "color: black; font-size: 20px; text-decoration: none; margin-left: 100px; position: relative; display: inline-block;"
        cls = "nav-link-active" if is_active else ""
        return A(text, href=href, style=style, cls=cls)
    
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

    munras = get_munras()
    munra_cards = [
        Div(
            A(
                Img(src=get_munra_cover(munra), 
                    alt=munra,
                    style="width: 100%; height: 250px; object-fit: cover; margin-bottom: 10px;") 
                    if get_munra_cover(munra) else Div(style="height: 250px; background-color: #ddd; margin-bottom: 10px;"),
                P(munra, style="margin: 0; color: black;"),
                href=f"/munras/{munra}", 
                style="text-decoration: none;"
            ),
            cls="munra-card"
        )
        for munra in munras
    ]
    
    grid = Div(
        *munra_cards,
        style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px;"
    )
    
    return Title("munra.cl"), NavBar("munras"), Page(
        P(
            NotStr(
                "Aquí encontrarás todos los <span class='highlight-munra'>munras</span>. <br>"
                "Cada <span class='highlight-munra'>munra</span> es un extracto mínimo de contenido.<br>"
            ),
            style="font-size: 16px; margin-bottom: 30px; color: #333;"
        ),
        grid,
        Script("""
            document.addEventListener('DOMContentLoaded', function() {
                // Draw card borders
                const cards = document.querySelectorAll('.munra-card');
                cards.forEach(card => {
                    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
                    svg.classList.add('munra-card-border');
                    card.appendChild(svg);
                    
                    const rc = rough.svg(svg);
                    const width = card.offsetWidth + 10;
                    const height = card.offsetHeight + 10;
                    svg.setAttribute('width', width);
                    svg.setAttribute('height', height);
                    
                    const rect = rc.rectangle(5, 5, width - 10, height - 10, {
                        stroke: '#999',
                        strokeWidth: 0.8,
                        roughness: 1.8,
                        bowing: 1.2,
                        fill: 'none',
                        disableMultiStroke: false,
                        seed: Math.random() * 1000
                    });
                    svg.appendChild(rect);
                });
                
                // Draw nav underlines
                const activeLinks = document.querySelectorAll('.nav-link-active');
                activeLinks.forEach(link => {
                    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
                    svg.style.position = 'absolute';
                    svg.style.bottom = '-5px';
                    svg.style.left = '0';
                    svg.style.width = '100%';
                    svg.style.height = '10px';
                    svg.style.pointerEvents = 'none';
                    link.appendChild(svg);
                    
                    const rc = rough.svg(svg);
                    const width = link.offsetWidth;
                    svg.setAttribute('width', width);
                    svg.setAttribute('height', 10);
                    
                    const line = rc.line(0, 3, width, 3, {
                        stroke: '#000',
                        strokeWidth: 1,
                        roughness: 1.5,
                        bowing: 0.5,
                        seed: Math.random() * 1000
                    });
                    svg.appendChild(line);
                });
            });
        """),
        PageFooter()
    )


@rt("/que-es")
def get():
    return Title("munra.cl"), NavBar("que-es"), Page(
        P(
            NotStr(
            "<b>¿Qué es Munra?</b> <br>"
            "<br>"
            "Un <span class='highlight-munra'>munra</span> es un registro.<br>"
            "Cada <span class='highlight-munra'>munra</span> es análogo: cinta, cassette, errores incluidos.<br>"
            "<br>"
            "Importa el proceso más que el resultado.<br>"
            "Sin prisa, sin filtros.<br>"
            "<br>"
            "Cada <span class='highlight-munra'>munra</span> se hace una vez y nunca es exactamente igual.<br>"
            "Made with love from Chile.<br>"
            ),
        style="font-size: 16px; line-height: 1.6; color: black;"
        ),
        Script("""
            document.addEventListener('DOMContentLoaded', function() {
                const activeLinks = document.querySelectorAll('.nav-link-active');
                activeLinks.forEach(link => {
                    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
                    svg.style.position = 'absolute';
                    svg.style.bottom = '-5px';
                    svg.style.left = '0';
                    svg.style.width = '100%';
                    svg.style.height = '10px';
                    svg.style.pointerEvents = 'none';
                    link.appendChild(svg);
                    
                    const rc = rough.svg(svg);
                    const width = link.offsetWidth;
                    svg.setAttribute('width', width);
                    svg.setAttribute('height', 10);
                    
                    const line = rc.line(0, 3, width, 3, {
                        stroke: '#000',
                        strokeWidth: 1,
                        roughness: 1.5,
                        bowing: 0.5,
                        seed: Math.random() * 1000
                    });
                    svg.appendChild(line);
                });
            });
        """),
        PageFooter(),
    )

@rt("/notes")
def get():
    posts = get_posts()
    
    post_list = [
        Div(
            A(
                H2(post['title'], style="margin: 0 0 10px 0; color: black;"),
                P(post['date'], style="font-size: 14px; color: #666; margin: 0 0 10px 0;"),
                P(post['excerpt'], style="margin: 0; color: #333;"),
                href=f"/notes/{post['id']}",
                style="text-decoration: none;"
            ),
            style="padding: 20px; margin-bottom: 20px; background-color: white; cursor: pointer;"
        )
        for post in posts
    ]
    
    return Title("munra.cl"), NavBar("notes"), Page(
        Div(*post_list) if post_list else P("No hay posts todavía."),
        PageFooter()
    )

@rt("/notes/{post_id}")
def get(post_id: str):
    posts = get_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    
    if not post:
        return Title("Post no encontrado"), NavBar("notes"), Page(
            P("Post no encontrado."),
            PageFooter()
        )
    
    content = get_post_content(post_id)
    
    return Title(f"{post['title']} - munra.cl"), NavBar("notes"), Page(
        A("← volver a notes", href="/notes", style="color: black; text-decoration: none; display: inline-block; margin-bottom: 20px;"),
        H1(post['title']),
        P(post['date'], style="color: #666; font-size: 14px; margin-bottom: 30px;"),
        P(content, style="line-height: 1.8; white-space: pre-wrap;"),
        PageFooter()
    )

@rt("/contact")
def get():
    return Title("munra.cl"), NavBar("contact"), Page(
        P("Escríbenos a rafasacaan@gmail.com", style="font-size: 16px; line-height: 1.6; color: black;"),
        Script("""
            document.addEventListener('DOMContentLoaded', function() {
                const activeLinks = document.querySelectorAll('.nav-link-active');
                activeLinks.forEach(link => {
                    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
                    svg.style.position = 'absolute';
                    svg.style.bottom = '-5px';
                    svg.style.left = '0';
                    svg.style.width = '100%';
                    svg.style.height = '10px';
                    svg.style.pointerEvents = 'none';
                    link.appendChild(svg);
                    
                    const rc = rough.svg(svg);
                    const width = link.offsetWidth;
                    svg.setAttribute('width', width);
                    svg.setAttribute('height', 10);
                    
                    const line = rc.line(0, 3, width, 3, {
                        stroke: '#000',
                        strokeWidth: 1,
                        roughness: 1.5,
                        bowing: 0.5,
                        seed: Math.random() * 1000
                    });
                    svg.appendChild(line);
                });
            });
        """),        PageFooter()
    )

@rt("/munras/{munra_name}")
def get(munra_name: str):
    info = get_munra_info(munra_name)
    tracks = get_munra_tracks(munra_name)
    
    # Left side - Munra info
    left_section = Div(
        H1(munra_name),
        P(info, style="line-height: 1.6; white-space: pre-wrap;"),
        style="padding: 20px; flex: 1;"
    )
    
    # Right side - Track list
    track_list = [
        Div(
            P(track, style="margin-bottom: 5px; font-size: 14px; color: black;"),
            Audio(
                Source(src=f"/static/munras/{munra_name}/{track}", type="audio/mpeg"),
                controls=True,
                style="width: 100%; height: 30px;"
            ),
            style="margin-bottom: 20px; padding: 15px; background-color: white;"
        )
        for track in tracks
    ]
    
    right_section = Div(
        H2("tracks"),
        *track_list,
        style="padding: 20px; flex: 1; position: relative;",
        cls="munra-separator"
    )
    
    # Two column layout
    content = Div(
        left_section,
        right_section,
        style="display: flex; gap: 20px;"
    )
    
    return Title(f"{munra_name} - munra.cl"), NavBar("munras"), Page(
        content,
        Script("""
            document.addEventListener('DOMContentLoaded', function() {
                const separator = document.querySelector('.munra-separator');
                if (separator) {
                    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
                    svg.style.position = 'absolute';
                    svg.style.left = '0';
                    svg.style.top = '0';
                    svg.style.height = '100%';
                    svg.style.width = '20px';
                    svg.style.pointerEvents = 'none';
                    separator.appendChild(svg);
                    
                    const rc = rough.svg(svg);
                    svg.setAttribute('width', 20);
                    svg.setAttribute('height', separator.offsetHeight);
                    
                    const line = rc.line(5, 0, 5, separator.offsetHeight, {
                        stroke: '#999',
                        strokeWidth: 0.8,
                        roughness: 1.8,
                        bowing: 1.2,
                        seed: Math.random() * 1000
                    });
                    svg.appendChild(line);
                }
            });
        """),
        PageFooter()
    )


serve()