"""
Markdown to HTML Converter - Python console application

Converts a subset of Markdown syntax to HTML. Written from scratch
(no external markdown library) to demonstrate line-by-line text parsing.

Supported syntax:
  # Heading 1 .. ###### Heading 6
  **bold**  and  *italic*
  `inline code`
  ```
  code blocks
  ```
  - bullet lists  (also * and +)
  1. numbered lists
  > blockquotes
  [link text](https://example.com)
  ![alt text](image.png)
  --- or ***  horizontal rules
  Blank line = paragraph break
"""

import re
import os


def convert_inline(text):
    """Handles inline formatting: bold, italic, code, links, images."""

    # Images: ![alt](url)  -- must be checked before links since syntax overlaps
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', text)

    # Links: [text](url)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

    # Bold: **text** or __text__
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)

    # Italic: *text* or _text_ (applied after bold so ** isn't caught here)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)

    # Inline code: `code`
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)

    return text


def convert_markdown(md_text):
    lines = md_text.split("\n")
    html_lines = []

    in_code_block = False
    in_list = None  # None, "ul", or "ol"
    paragraph_buffer = []

    def flush_paragraph():
        if paragraph_buffer:
            joined = " ".join(paragraph_buffer)
            html_lines.append(f"<p>{convert_inline(joined)}</p>")
            paragraph_buffer.clear()

    def close_list():
        nonlocal in_list
        if in_list == "ul":
            html_lines.append("</ul>")
        elif in_list == "ol":
            html_lines.append("</ol>")
        in_list = None

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code block fences ```
        if stripped.startswith("```"):
            flush_paragraph()
            close_list()
            if not in_code_block:
                html_lines.append("<pre><code>")
                in_code_block = True
            else:
                html_lines.append("</code></pre>")
                in_code_block = False
            i += 1
            continue

        if in_code_block:
            # Escape HTML special characters inside code blocks
            escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            html_lines.append(escaped)
            i += 1
            continue

        # Blank line -> paragraph/list break
        if stripped == "":
            flush_paragraph()
            close_list()
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^(-{3,}|\*{3,}|_{3,})$', stripped):
            flush_paragraph()
            close_list()
            html_lines.append("<hr>")
            i += 1
            continue

        # Headings
        heading_match = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if heading_match:
            flush_paragraph()
            close_list()
            level = len(heading_match.group(1))
            content = convert_inline(heading_match.group(2))
            html_lines.append(f"<h{level}>{content}</h{level}>")
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            flush_paragraph()
            close_list()
            quote_content = convert_inline(stripped.lstrip(">").strip())
            html_lines.append(f"<blockquote>{quote_content}</blockquote>")
            i += 1
            continue

        # Unordered list item
        ul_match = re.match(r'^[-*+]\s+(.*)', stripped)
        if ul_match:
            flush_paragraph()
            if in_list != "ul":
                close_list()
                html_lines.append("<ul>")
                in_list = "ul"
            html_lines.append(f"<li>{convert_inline(ul_match.group(1))}</li>")
            i += 1
            continue

        # Ordered list item
        ol_match = re.match(r'^\d+\.\s+(.*)', stripped)
        if ol_match:
            flush_paragraph()
            if in_list != "ol":
                close_list()
                html_lines.append("<ol>")
                in_list = "ol"
            html_lines.append(f"<li>{convert_inline(ol_match.group(1))}</li>")
            i += 1
            continue

        # Regular text -> part of a paragraph
        close_list()
        paragraph_buffer.append(stripped)
        i += 1

    flush_paragraph()
    close_list()
    if in_code_block:
        html_lines.append("</code></pre>")  # close unterminated code block defensively

    return "\n".join(html_lines)


def wrap_html_document(body, title="Converted Document"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
</head>
<body>
{body}
</body>
</html>
"""


def main():
    print("===== Markdown to HTML Converter =====\n")

    input_path = input("Enter path to .md file: ").strip()
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    body_html = convert_markdown(md_text)

    wrap = input("Wrap in a full HTML document (with <html>/<head>/<body>)? (y/n): ").strip().lower()
    if wrap == "y":
        title = os.path.splitext(os.path.basename(input_path))[0]
        final_html = wrap_html_document(body_html, title=title)
    else:
        final_html = body_html

    default_output = os.path.splitext(input_path)[0] + ".html"
    output_path = input(f"Output file path [{default_output}]: ").strip() or default_output

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"\nConverted successfully: {output_path}")


if __name__ == "__main__":
    main()
