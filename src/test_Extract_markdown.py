import unittest
from Extract_Markdown import *


def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a [link](https://www.google.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("link", "https://www.google.com")], matches)


if __name__ == "__main__":
    unittest.main()