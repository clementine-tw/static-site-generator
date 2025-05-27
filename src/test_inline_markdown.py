import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextType, TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_1_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "`", TextType.CODE),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_2_code_block(self):
        node = TextNode("This is text with `code 1` and `code 2` block", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "`", TextType.CODE),
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("code 1", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("code 2", TextType.CODE),
                TextNode(" block", TextType.TEXT),
            ],
        )

    def test_1_bold_block(self):
        node = TextNode("This is text with **bold text**", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
            ],
        )
