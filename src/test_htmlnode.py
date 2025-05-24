import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode("p", "this is p")
        self.assertEqual(node.tag, "p")

    def test_value(self):
        node = HTMLNode("p", "this is p")
        self.assertEqual(node.value, "this is p")

    def test_props_to_html_none(self):
        node = HTMLNode("p", "this is p")
        want = ""
        got = node.props_to_html()
        self.assertEqual(got, want)

    def test_props_to_html_1_attr(self):
        node = HTMLNode("p", "this is p", props = {"color": "white"})
        want = ' "color"="white"'
        got = node.props_to_html()
        self.assertEqual(got, want)

    def test_props_to_html_2_attr(self):
        node = HTMLNode("a", "this is link", None,
                        {"href": "https://google.com", "target": "_blank"})
        want = ' "href"="https://google.com" "target"="_blank"'
        got = node.props_to_html()
        self.assertEqual(got, want)

    def test_repr(self):
        node = HTMLNode("a", "this is link", None, {"href": "http"})
        want = "tag: a\nvalue: this is link\nprops: {'href': 'http'}\nchildren: None\n"
        got = repr(node)
        self.assertEqual(got, want)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        want = '<a "href"="https://www.google.com">Click me!</a>'
        got = node.to_html()
        self.assertEqual(got, want)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "raw text")
        want = "raw text"
        got = node.to_html()
        self.assertEqual(got, want)

if __name__ == "__main__":
    unittest.main()
