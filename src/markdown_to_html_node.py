from markdown_block import markdown_to_blocks
from blocktype import block_to_block_type
from blocktype import BlockType
from splitdelimeter import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode

#Converts a full markdown document into a single parent HTMLNode.
#That one parent HTMLNode should (obviously) contain many child HTMLNode objects representing the nested elements.
def markdown_to_html_node(markdown):
    # 1.Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    
    # 2.Loop over each block and collect all the text_nodes
    # per-document collection goes here
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)

        #define tag for each block:
        tag = ""
        if block_type == BlockType.PARAGRAPH:
            block_node = paragraph_to_html_node(block)
        elif block_type == BlockType.HEADING:
            block_node = header_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            block_node = quote_to_html_node(block)
        elif block_type == BlockType.CODE:
            block_node = code_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            block_node = unordered_list_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:  
            block_node = ordered_list_to_html_node(block)

        block_nodes.append(block_node)

    final_HTML_node = ParentNode("div",block_nodes)
    return final_HTML_node

def paragraph_to_html_node(block):
    block = block.replace("\n"," ")
    tag = "p"

    text_nodes = text_to_textnodes(block)

    #Loop over each text_node and collect all the LeafNodes
    children = []
        
    for text_node in text_nodes:
        leaf_node = text_node_to_html_node(text_node)
        children.append(leaf_node)
                    
    block_node = ParentNode(tag,children)
    return block_node

def header_to_html_node(block):
    h_count = 0
    for char in block:
        if char == "#":
            h_count +=1
        else:
            break
    tag = f'h{h_count}'
    block = block[h_count+1:]

    text_nodes = text_to_textnodes(block)

    #Loop over each text_node and collect all the LeafNodes
    children = []
        
    for text_node in text_nodes:
        leaf_node = text_node_to_html_node(text_node)
        children.append(leaf_node)
                    
    block_node = ParentNode(tag,children)
    return block_node

def quote_to_html_node(block):
    tag = "blockquote"

    quote_lines = block.split("\n")
    cleaned_lines = []
    for line in quote_lines:
        cleaned_line = line.lstrip(">").strip()
        cleaned_lines.append(cleaned_line)

    quote = " ".join(cleaned_lines)

    text_nodes = text_to_textnodes(quote)

    #Loop over each text_node and collect all the LeafNodes
    children = []
        
    for text_node in text_nodes:
        leaf_node = text_node_to_html_node(text_node)
        children.append(leaf_node)
                    
    block_node = ParentNode(tag,children)
    return block_node

def code_to_html_node(block):
    code = block[3:]
    code = code[:-3]
    code = code.lstrip()

    Code_TEXTNODE = TextNode(code, TextType.TEXT, url=None)
    leaf_node = text_node_to_html_node(Code_TEXTNODE)
    children = []
    children.append(leaf_node)

    Temp_node = ParentNode("code", children)
    temp_nodes = []
    temp_nodes.append(Temp_node)

    block_node = ParentNode("pre",temp_nodes)
    return block_node
    

def unordered_list_to_html_node(block):

    unordered_list_lines = block.split("\n")

    lines_clean = []
    li_nodes = []   

    for line in unordered_list_lines:
        lines_clean.append(line[2:])

    for clean_lines in lines_clean:

        #covert line into text node, then to html
        text_nodes = text_to_textnodes(clean_lines)

        #Loop over each text_node and collect all the LeafNodes
        children = []
            
        for text_node in text_nodes:
            leaf_node = text_node_to_html_node(text_node)
            children.append(leaf_node)

        line_node = ParentNode("li",children)
        li_nodes.append(line_node)

    block_node = ParentNode("ul",li_nodes)
    return block_node

def ordered_list_to_html_node(block):

    ordered_list_lines = block.split("\n")

    lines_clean = []
    li_nodes = []
    
    for line in ordered_list_lines:
        digit_count = 0
        for char in line:
            if char != ".":
                digit_count +=1
            else:
                break

        lines_clean.append(line[digit_count+2:])

    for clean_lines in lines_clean:

        #covert line into text node, then to html
        text_nodes = text_to_textnodes(clean_lines)

        #Loop over each text_node and collect all the LeafNodes
        children = []
            
        for text_node in text_nodes:
            leaf_node = text_node_to_html_node(text_node)
            children.append(leaf_node)

        line_node = ParentNode("li",children)
        li_nodes.append(line_node)

    block_node = ParentNode("ol",li_nodes)
    return block_node

if __name__ == "__main__":
    md = """
### This is header

This is **bolded** paragraph
text in a p
tag here

> This is a quote
> that spans two lines

```
This is text that _should_ remain
the **same** even with inline stuff
```

- unordered list
- block

- broken unordered list
block

1. ordered list
2. block

1. broken ordered list
3. block

This is another paragraph with _italic_ text and `code` here

"""
    result = markdown_to_html_node(md)
    print (result.to_html())