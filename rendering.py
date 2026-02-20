"""Post content rendering — parses markdown-like syntax into FastHTML elements"""

import re
from fasthtml.common import *
from pygments import highlight as _highlight
from pygments.lexers import get_lexer_by_name
from pygments.lexers.special import TextLexer
from pygments.formatters import HtmlFormatter

_formatter = HtmlFormatter(nowrap=True, style='default')


def _highlight_code(code, lang):
    try:
        lexer = get_lexer_by_name(lang, stripall=True)
    except Exception:
        lexer = TextLexer()
    return _highlight(code, lexer, _formatter)


def render_post_body(body):
    """Parse post body supporting ```lang code blocks and ![alt](src) images"""
    elements = []
    parts = re.split(r'(```\w*\n.*?```)', body, flags=re.DOTALL)

    for part in parts:
        code_match = re.match(r'```(\w*)\n(.*?)```', part, flags=re.DOTALL)
        if code_match:
            lang = code_match.group(1) or "text"
            code = code_match.group(2).rstrip()
            elements.append(
                Div(Pre(NotStr(_highlight_code(code, lang)), cls="post-code"), cls="code-block", data_lang=lang)
            )
        else:
            for block in part.split('\n\n'):
                block = block.strip()
                if not block:
                    continue
                img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', block)
                if img_match:
                    alt, src = img_match.group(1), img_match.group(2)
                    elements.append(
                        Div(
                            Img(src=src, alt=alt, cls="post-img"),
                            P(alt, cls="post-caption") if alt else "",
                            cls="post-figure",
                        )
                    )
                else:
                    elements.append(P(block, cls="post-body"))

    return elements
