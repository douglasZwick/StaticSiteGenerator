import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
  def test_to_html(self) -> None:
    node = HTMLNode()
    with self.assertRaises(NotImplementedError):
      node.to_html()

  def test_props_to_html0(self) -> None:
    tag = "a"
    value = "Should not be seen"
    children = None
    props = {
      "href": "en.wikipedia.org",
      "target": "_blank",
      "onclick": "console.log('Hello world')",
    }

    node = HTMLNode(tag, value, children, props)
    expected = 'href="en.wikipedia.org" target="_blank" onclick="console.log(\'Hello world\')"'
    actual = node.props_to_html()
    self.assertEqual(expected, actual)

  def test_props_to_html1(self) -> None:
    node = HTMLNode()
    expected = ""
    actual = node.props_to_html()
    self.assertEqual(expected, actual)

  def test_props_to_html_with_unary_property(self) -> None:
    tag = "script"
    value = ""
    children = None
    props = {
      "type": "text/javascript",
      "src": "https://abc.xyz/script.js",
      "crossorigin": None,
      "async": None,
      "defer": None,
    }

    node = HTMLNode(tag, value, children, props)
    expected = 'type="text/javascript" src="https://abc.xyz/script.js" crossorigin async defer'
    actual = node.props_to_html()
    self.assertEqual(expected, actual)

  def test_repr(self) -> None:
    tag = "a"
    value = "Should not be seen"
    children = None
    props = {
      "href": "en.wikipedia.org",
      "target": "_blank",
      "onclick": "console.log('Hello world')",
    }

    node = HTMLNode(tag, value, children, props)
    expected = 'HTMLNode(a, \'Should not be seen\', None, {\'href\': \'en.wikipedia.org\', \'target\': \'_blank\', \'onclick\': "console.log(\'Hello world\')"})'
    actual = f"{node}"
    self.assertEqual(expected, actual)


if __name__ == "main":
  unittest.main()
