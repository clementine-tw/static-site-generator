import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    BlockType,
)


class TestMarkdownToBlocks(unittest.TestCase):
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


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# 123"
        self.assertEqual(
            BlockType.HEADING,
            block_to_block_type(block),
        )

    def test_heading_6(self):
        block = "###### 666"
        self.assertEqual(
            BlockType.HEADING,
            block_to_block_type(block),
        )

    def test_break_heading(self):
        block = "####### 7+#"
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_to_block_type(block),
        )

    def test_code(self):
        block = "```\nThis is code\ncode2\ncode3\n```"
        self.assertEqual(
            BlockType.CODE,
            block_to_block_type(block),
        )

    def test_quote(self):
        block = "> aaa\n> bbb\n> ccc"
        self.assertEqual(
            BlockType.QUOTE,
            block_to_block_type(block),
        )

    def test_unordered_list(self):
        block = "- ul 1\n- ul 2"
        self.assertEqual(
            BlockType.UNORDERED_LIST,
            block_to_block_type(block),
        )

    def test_ordered_list(self):
        block = "1. ol 1\n2. ol 2\n3. ol 3"
        self.assertEqual(
            BlockType.ORDERED_LIST,
            block_to_block_type(block),
        )


class TestMarkdownToHTMLNode(unittest.TestCase):
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
