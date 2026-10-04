import unittest
from markdown_block import markdown_to_blocks
from blocktype import BlockType, block_to_block_type

class MarkdownBlockTests(unittest.TestCase):
    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_markdown_to_blocks_few_empty(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_markdown_to_blocks_few_empty(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_markdown_to_blocks_emptystring(self):
            md = ""

            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [],
            )

    def test_markdown_to_blocks_trails(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line   



- This is a list
- with items  
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_markdown_to_blocks_singleblock(self):
            md = "This is **bolded** paragraph, with nothing else in it"
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                ["This is **bolded** paragraph, with nothing else in it"],
            )

class MarkdownBlockToBlockTest(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code(self):
        block = "```\ncode block\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_headin3(self):
        block = "### Heading 3"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_quote(self):
        block = ">many lines\n>block"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_partialquote(self):
        block =">partial quote\nblock"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unorderedlist(self):
        block ="- unordered list\n- block"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_broken_unorderedlist(self):
        block = "- broken unordered list\nblock"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_orderedlist(self):
        block ="1. ordered list\n2. block"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_broken_orderedlist(self):
        block ="1. broken ordered list\n3. block"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_broken_paragraph(self):
        block ="Just a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)