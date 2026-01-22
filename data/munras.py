"""Functions for managing munras (music releases)"""

from pathlib import Path
from config import STATIC_MUNRAS_PATH


def get_munra_cover(munra_name):
    """Get the cover image path for a munra"""
    for ext in ['jpg', 'jpeg', 'png', 'webp']:
        cover_path = Path(STATIC_MUNRAS_PATH) / munra_name / f"cover.{ext}"
        if cover_path.exists():
            return f"/{STATIC_MUNRAS_PATH}/{munra_name}/cover.{ext}"
    return None


def get_munras():
    """Get all munras"""
    munras_dir = Path(STATIC_MUNRAS_PATH)
    if not munras_dir.exists():
        return []
    return [d.name for d in munras_dir.iterdir() if d.is_dir()]


def get_munra_info(munra_name):
    """Get the info text for a munra"""
    info_file = Path(STATIC_MUNRAS_PATH) / munra_name / "info.txt"
    if info_file.exists():
        return info_file.read_text()
    return "No hay información disponible."


def get_munra_tracks(munra_name):
    """Get all tracks for a munra"""
    munra_dir = Path(STATIC_MUNRAS_PATH) / munra_name
    if not munra_dir.exists():
        return []
    return [f.name for f in munra_dir.glob("*.mp3")]
