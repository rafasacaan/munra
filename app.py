from pathlib import Path
from fasthtml.common import *

app, rt = fast_app(
    hdrs=(
        Style("""
            * {
                font-family: 'Courier New', Courier, monospace;
            }
        """),
    )
)

######################################################################################
### Helpers
######################################################################################
def get_artist_cover(artist_name):
    # Try different image extensions
    for ext in ['jpg', 'jpeg', 'png', 'webp']:
        cover_path = Path(f"static/artists/{artist_name}/cover.{ext}")
        if cover_path.exists():
            return f"/static/artists/{artist_name}/cover.{ext}"
    return None  # No cover found

def get_artists():
    artists_dir = Path("static/artists")
    if not artists_dir.exists():
        return []
    return [d.name for d in artists_dir.iterdir() if d.is_dir()]

def get_artist_info(artist_name):
    info_file = Path(f"static/artists/{artist_name}/info.txt")
    if info_file.exists():
        return info_file.read_text()
    return "No hay información disponible."

def get_artist_tracks(artist_name):
    artist_dir = Path(f"static/artists/{artist_name}")
    if not artist_dir.exists():
        return []
    return [f.name for f in artist_dir.glob("*.mp3")]

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
        style = (
            "color: black; font-size: 24px; text-decoration: none; margin-left: 100px; "
            + ("text-decoration: underline;" if is_active else "")
        )
        return A(text, href=href, style=style)
    
    return Nav(
        Div(
            # Logo on the left
            A(
                Img(src="/static/munra.jpg", alt="Munra Logo", 
                    style="height: 270px; max-width: 250%; width: auto; display: block;"),
                href="/"),
            
            # Links below the logo
            Div(
                A("home", href="/", 
                style=f"color: black; font-size: 24px; text-decoration: none; {'text-decoration: underline;' if current_page == 'home' else ''}"),
                nav_link("notas", "/notes", "notes"),
                nav_link("artistas", "/artists", "artists"),
                nav_link("contacto", "/contact", "contact"),
                style="display: flex; margin-top: 20px;"),
            
            style="display: flex; flex-direction: column; padding: 20px; width: 100%;"),
        style="margin: 2% 5%;"
    )

def PageFooter():
    return Div(
        P("© 2024 Munra - Sello de música chileno"),
        style="font-size: 12px; position: fixed; bottom: 0; left: 0; right: 0; text-align: center; padding: 20px; border-top: 1px solid #ccc; background-color: white; margin: 0 5%;"
    )

def Page(*content):
    return Div(*content, style="margin: 2% 6%;")


### Routes
######################################################################################

@rt("/")
def get():
    return Title("munra.cl"), NavBar(), Page(
        P(
            NotStr(
            "<b>¿Qué es Munra?</b> <br>"
            "<br>"
            "Munra es un sello de música chileno.<br>"
            "Nos gusta enfocarnos en el proceso: <br>"
            " - más en el <i>cómo</i>, y menos en el <i>qué</i>.<br>"
            "<br>"
            "Todo parte desde algún instrumento análogo.<br>"
            "Nuestras producciones son hechas a cassette.<br>"
            "<br>"
            "Cada pieza es única, hecha con dedicación y atención.<br>"
            ),
        style="font-size: 16px; line-height: 1.6;"
        ),
        PageFooter(),
    )


@rt("/artists")
def get():

    artists = get_artists()
    artist_cards = [
        Div(
            A(
                Img(src=get_artist_cover(artist), 
                    alt=artist,
                    style="width: 100%; height: 250px; object-fit: cover; margin-bottom: 10px;") 
                    if get_artist_cover(artist) else Div(style="height: 250px; background-color: #ddd; margin-bottom: 10px;"),
                P(artist, style="margin: 0; color: black;"),
                href=f"/artists/{artist}", 
                style="text-decoration: none;"
            ),
            style=
                "border: 1px solid black; "
                "border-radius: 1px; "
                "pointer: hover; "
                "padding: 20px; "
                "background-color: white;"
                "margin: 10px; "
                "width: 300px; "
                "text-align: center; "
        )
        for artist in artists
    ]
    
    grid = Div(
        *artist_cards,
        style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px;"
    )
    
    return Title("munra.cl"), NavBar("artists"), Page(
        grid,
        PageFooter()
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
        P("Contáctanos en rafasacaan@gmail.com"),
        PageFooter()
    )

@rt("/artists/{artist_name}")
def get(artist_name: str):
    info = get_artist_info(artist_name)
    tracks = get_artist_tracks(artist_name)
    
    # Left side - Artist info
    left_section = Div(
        H1(artist_name),
        P(info, style="line-height: 1.6; white-space: pre-wrap;"),
        style="padding: 20px; flex: 1;"
    )
    
    # Right side - Track list
    track_list = [
        Div(
            P(track, style="margin-bottom: 5px; font-size: 14px; color: black;"),
            Audio(
                Source(src=f"/static/artists/{artist_name}/{track}", type="audio/mpeg"),
                controls=True,
                style="width: 100%; height: 30px;"
            ),
            style="margin-bottom: 20px; padding: 15px; background-color: white; border: 3px solid black;"
        )
        for track in tracks
    ]
    
    right_section = Div(
        H2("tracks"),
        *track_list,
        style="padding: 20px; flex: 1; border-left: 1px solid #ccc;"
    )
    
    # Two column layout
    content = Div(
        left_section,
        right_section,
        style="display: flex; gap: 20px;"
    )
    
    return Title(f"{artist_name} - munra.cl"), NavBar("artists"), Page(
        content,
        PageFooter()
    )


serve()