import unittest
from markdown_to_html_node import markdown_to_html_node

class MarkdownToHTMLTests(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
    ```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_wholemixedtest(self):
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
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is header</h3>"
            "<p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<blockquote>This is a quote that spans two lines</blockquote>"
            "<pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n"
            "</code></pre>"
            "<ul><li>unordered list</li><li>block</li></ul>"
            "<p>- broken unordered list block</p>"
            "<ol><li>ordered list</li><li>block</li></ol>"
            "<p>1. broken ordered list 3. block</p>"
            "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p>"
            "</div>",
        )