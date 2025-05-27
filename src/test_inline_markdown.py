import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)
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


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_1_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://example.com/image.png)"
        )
        self.assertEqual([("image", "https://example.com/image.png")], matches)

    def test_extract_2_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://example.com/image.png) and ![image2](https://example.com/img2.png)"
        )
        self.assertEqual(
            [
                ("image", "https://example.com/image.png"),
                ("image2", "https://example.com/img2.png"),
            ],
            matches,
        )


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_1_link(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_2_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) "
            + "and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )


class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_only_image(self):
        node = TextNode("![image](https://www.google.com/xxx.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.google.com/xxx.png"),
            ],
            new_nodes,
        )


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with [google](https://www.google.com) and"
            + " [youtube](https://www.youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("google", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("youtube", TextType.LINK, "https://www.youtube.com"),
            ],
            new_nodes,
        )
