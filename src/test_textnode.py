import unittest
from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()
