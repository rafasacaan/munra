"""Functions for managing posts/notes data"""

from pathlib import Path
from config import STATIC_NOTES_PATH


def get_posts():
    """Get all posts from the notes directory"""
    notes_dir = Path(STATIC_NOTES_PATH)
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
    """Get the content of a specific post"""
    content_file = Path(STATIC_NOTES_PATH) / post_id / "content.txt"
    if content_file.exists():
        return content_file.read_text()
    return "No content available."


def get_post_by_id(post_id):
    """Get a specific post by ID"""
    posts = get_posts()
    return next((p for p in posts if p['id'] == post_id), None)
