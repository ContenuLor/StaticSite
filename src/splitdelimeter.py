from platform import node

from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images
from extract_markdown import extract_markdown_links


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text)%2 == 0:
                raise Exception("Delimiter is not balanced")

            for i in range(len(split_text)):
                if split_text[i] == "":
                    continue
                if i%2 == 0:
                    new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_text[i], text_type))

    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            image = extract_markdown_images(node.text)
            remaining_text = node.text

            for alt_text, url in image:
                image_markdown = f"![{alt_text}]({url})"
                section = remaining_text.split(image_markdown, 1)

                if section[0] != "":
                    new_nodes.append(TextNode(section[0], TextType.TEXT))

                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                remaining_text = section[1]

            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            remaining_text = node.text

            for link_text, url in links:
                link_markdown = f"[{link_text}]({url})"
                section = remaining_text.split(link_markdown, 1)

                if section[0] != "":
                    new_nodes.append(TextNode(section[0], TextType.TEXT))

                new_nodes.append(TextNode(link_text, TextType.LINK, url))
                remaining_text = section[1]

            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text): 
    text_nodes = []

    #Create TextNode for all text
    text_nodes.append(TextNode(text, TextType.TEXT))

    #Use split_nodes_delimiter to split BOLD (**)
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    #Use split_nodes_delimiter to split italic (_)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    #Use split_nodes_delimiter to split code (')
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    #Use split_nodes_image
    text_nodes = split_nodes_image(text_nodes)
    #Use split_nodes_link
    text_nodes = split_nodes_link(text_nodes)

    return text_nodes 