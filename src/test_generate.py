from markdown_to_html_node import markdown_to_html_node

with open("content/index.md") as f:
    text = f.read()

node = markdown_to_html_node(text)
print(node.to_html())