import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
  def test_eq0(self) -> None:
    node_a = TextNode("This is a text node", TextType.BOLD)
    node_b = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node_a, node_b)

  def test_eq1(self) -> None:
    node_a = TextNode("This is a text node", TextType.BOLD)
    node_b = TextNode("This is a text node", TextType.BOLD, None)
    self.assertEqual(node_a, node_b)

  def test_ne0(self) -> None:
    node_a = TextNode("This is a text node", TextType.BOLD)
    node_b = TextNode("This is a text node", TextType.ITALIC)
    self.assertNotEqual(node_a, node_b)

  def test_ne1(self) -> None:
    node_a = TextNode("This is a text node", TextType.BOLD)
    node_b = TextNode("This is a text node", TextType.BOLD, "en.wikipedia.org")
    self.assertNotEqual(node_a, node_b)


class TestTextNodeToHTMLNode(unittest.TestCase):
  def test_text_node_to_html_node_with_text(self) -> None:
    text_node = TextNode("Hello world", TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    expected = "Hello world"
    actual = html_node.to_html()
    self.assertEqual(expected, actual)

  def test_text_node_to_html_node_with_bold(self) -> None:
    text_node = TextNode("Hello world", TextType.BOLD)
    html_node = text_node_to_html_node(text_node)
    expected = "<b>Hello world</b>"
    actual = html_node.to_html()
    self.assertEqual(expected, actual)

  def test_text_node_to_html_node_with_italic(self) -> None:
    text_node = TextNode("Hello world", TextType.ITALIC)
    html_node = text_node_to_html_node(text_node)
    expected = "<i>Hello world</i>"
    actual = html_node.to_html()
    self.assertEqual(expected, actual)

  def test_text_node_to_html_node_with_code(self) -> None:
    text_node = TextNode("Hello world", TextType.CODE)
    html_node = text_node_to_html_node(text_node)
    expected = "<code>Hello world</code>"
    actual = html_node.to_html()
    self.assertEqual(expected, actual)

  def test_text_node_to_html_node_with_link(self) -> None:
    text_node = TextNode("Hello world", TextType.LINK, "https://example.com/")
    html_node = text_node_to_html_node(text_node)
    expected = '<a href="https://example.com/">Hello world</a>'
    actual = html_node.to_html()
    self.assertEqual(expected, actual)

  def test_text_node_to_html_node_with_image(self) -> None:
    text_node = TextNode("Hello world", TextType.IMAGE, "https://example.com/example.png")
    html_node = text_node_to_html_node(text_node)
    expected = '<img src="https://example.com/example.png" alt="Hello world"></img>'
    actual = html_node.to_html()
    self.assertEqual(expected, actual)

  def test_text_node_to_html_node_with_invalid_type(self) -> None:
    text_node = TextNode("Invalid", None) # type: ignore
    with self.assertRaises(ValueError):
      text_node_to_html_node(text_node)  


if __name__ == "main":
  unittest.main()
