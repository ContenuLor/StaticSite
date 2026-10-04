import re

def extract_markdown_images(text):
# should return [("rick roll", "https://i.imgur.com/aKaOqIh.gif")
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
# should return [("rick roll", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")]
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches