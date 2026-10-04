from enum import Enum
import re

class BlockType (Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block) -> BlockType:

    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    heading_pattern = r"^#{1,6} "

    if re.match(heading_pattern, block):
        return BlockType.HEADING

    # Multiline Code blocks must start with 3 backticks and a newline, then end with 3 backticks.
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    # Every line in a quote block must start with a "greater-than" character: > followed by the quote text. 
    # A space after > is allowed but not required.
    lines = block.split("\n")

        #Check if all lines are QUOTE lines
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE


    # Every line in an unordered list block must start with a - character, followed by a space.
    lines = block.split("\n")
    
        #Check if all lines are UNORDERED LIST lines
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Every line in an ordered list block must start with a number followed by a . character and a space. 
    # The number must start at 1 and increment by 1 for each line.

    lines = block.split("\n")
    #Check if all lines are ORDERED LIST lines
    i = 1
    is_ordered = True
    for line in lines:
        if not line.startswith(f'{i}. '):
            is_ordered = False
            break
        i += 1

    if is_ordered == True:
        return BlockType.ORDERED_LIST
                               

    # If none of the above conditions are met, the block is a normal paragraph.

    return BlockType.PARAGRAPH

if __name__ == "__main__":
    test_cases = [
        "# Heading 1",
        "### Heading 3",
        "```\nprint('hello')\n```",
        """>many lines
>block""",
        """>partion quote
block""",
        """- unordered list
- block""",
        """- broken unordered list
block""",
        """1. ordered list
2. block""",
        """1. broken ordered list
3. block""",
        "Just a normal paragraph.",
    ]

    for block in test_cases:
        result = block_to_block_type(block)
        print(f"Input:\n{block}\nResult: {result}\n{'-'*20}")