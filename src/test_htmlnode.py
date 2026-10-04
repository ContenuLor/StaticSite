import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)   

    def test_URLNone(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_testtype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)        

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
            node = LeafNode("b", "Hello, world!")
            self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_props(self):
            node = LeafNode("p", "Hello, world!", {"href": "https://www.boot.dev"})
            self.assertEqual(node.to_html(), '<p href="https://www.boot.dev">Hello, world!</p>')





if __name__ == "__main__":
    unittest.main()