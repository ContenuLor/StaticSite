import sys

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from copystatic import copy_and_clean_public
from generate_pages_recursive import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    copy_and_clean_public()

    template_path = "template.html"
    dir_path_content = "content"
    dest_dir_path = "docs"

    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)


main()