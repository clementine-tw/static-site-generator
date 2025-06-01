import unittest
from htmlpage import extract_title


class TestExtracTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Hello

## Heading 2
"""
        self.assertEqual(
            extract_title(md),
            "Hello",
        )
