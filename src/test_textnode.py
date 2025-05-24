import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("this is text", TextType.TEXT)
        node2 = TextNode("this is text", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_eq_url(self):
        node1 = TextNode("link node", TextType.LINK, "https://google.com")
        node2 = TextNode("link node", TextType.LINK, "https://google.com")
        self.assertEqual(node1, node2)

    def test_noteq(self):
        node1 = TextNode("this is text", TextType.TEXT)
        node2 = TextNode("this is another text", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_noteq_url(self):
        node1 = TextNode("link node", TextType.LINK, "https://example.com")
        node2 = TextNode("link node", TextType.LINK, "https://google.com")
        self.assertNotEqual(node1, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://google.com"})

    def test_image(self):
        node = TextNode("image alt text", TextType.IMAGE, "an image url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"src": "an image url", "alt": "image alt text"}
        )


if __name__ == "__main__":
    unittest.main()
