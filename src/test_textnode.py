import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from splitdelimeter import split_nodes_delimiter, text_to_textnodes


class TestTextNode(unittest.TestCase):
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

    def test_text_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_text_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev/image.png", "alt": "This is a text node"})

    def test_delimeter_split_bold(self):
        nodes = [TextNode("This is a **bold** text node", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(" text node", TextType.TEXT))

    def test_delimeter_split_italic(self):
        nodes = [TextNode("This is a *italic* text node", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("italic", TextType.ITALIC))
        self.assertEqual(new_nodes[2], TextNode(" text node", TextType.TEXT))

    def test_delimeter_split_code(self):
        nodes = [TextNode("This is a `code` text node", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" text node", TextType.TEXT))

    def test_delimeter_split_unbalanced(self):
        nodes = [TextNode("This is a **bold text node", TextType.TEXT)]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertTrue("Delimiter is not balanced" in str(context.exception))

    def test_delimeter_split_empty(self):
        nodes = [TextNode("This is a **** text node", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("This is a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode(" text node", TextType.TEXT))

    def test_text_to_node_1(self):
        #bold+italic
        text = "This is a **bold** text node and _italic_ text node"
        text_nodes = text_to_textnodes(text)
        self.assertEqual(len(text_nodes), 5)
        self.assertEqual(text_nodes[0], TextNode("This is a ", TextType.TEXT))
        self.assertEqual(text_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(text_nodes[2], TextNode(" text node and ", TextType.TEXT))
        self.assertEqual(text_nodes[3], TextNode("italic", TextType.ITALIC))
        self.assertEqual(text_nodes[4], TextNode(" text node", TextType.TEXT))

    def test_text_to_node_2(self):
        #plain text string
        text = "This is a just a text"
        text_nodes = text_to_textnodes(text)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(text_nodes[0], TextNode("This is a just a text", TextType.TEXT))


    def test_text_to_node_mix(self):
        #bold+italic+image+url
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        self.assertEqual(len(text_nodes), 10)
        self.assertEqual(text_nodes[0], TextNode("This is ", TextType.TEXT))
        self.assertEqual(text_nodes[1], TextNode("text", TextType.BOLD))
        self.assertEqual(text_nodes[2], TextNode(" with an ", TextType.TEXT))
        self.assertEqual(text_nodes[3], TextNode("italic", TextType.ITALIC))
        self.assertEqual(text_nodes[4], TextNode(" word and a ", TextType.TEXT))
        self.assertEqual(text_nodes[5], TextNode("code block", TextType.CODE))
        self.assertEqual(text_nodes[6], TextNode(" and an ", TextType.TEXT))
        self.assertEqual(text_nodes[7], TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"))
        self.assertEqual(text_nodes[8], TextNode(" and a ", TextType.TEXT))
        self.assertEqual(text_nodes[9], TextNode("link", TextType.LINK, "https://boot.dev"))

    


if __name__ == "__main__":
    unittest.main()