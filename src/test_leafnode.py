import unittest
from leafnode import *


class TestLeafNode(unittest.TestCase):
  def test_to_html_p(self) -> None:
    tag = "p"
    value = "Hello world!"
    props = None

    node = LeafNode(tag, value, props)
    expected = "<p>Hello world!</p>"
    actual = node.to_html()
    self.assertEqual(expected, actual)

  def test_to_html_a(self) -> None:
    tag = "a"
    value = "Should not be seen"
    props = {
      "href": "en.wikipedia.org",
      "target": "_blank",
      "onclick": "console.log('Hello world')",
    }

    node = LeafNode(tag, value, props)
    expected = '<a href="en.wikipedia.org" target="_blank" onclick="console.log(\'Hello world\')">Should not be seen</a>'
    actual = node.to_html()
    self.assertEqual(expected, actual)

  def test_to_html_default(self) -> None:
    tag = None
    value = "Hello world"

    node = LeafNode(tag, value)
    expected = value
    actual = node.to_html()
    self.assertEqual(expected, actual)

  def test_to_html_raise(self) -> None:
    tag = None
    value = "Will be replaced"

    node = LeafNode(tag, value)
    node.value = None
    with self.assertRaises(ValueError):
      node.to_html()

  def test_repr(self) -> None:
    tag = "a"
    value = "Should not be seen"
    props = {
      "href": "en.wikipedia.org",
      "target": "_blank",
      "onclick": "console.log('Hello world')",
    }

    node = LeafNode(tag, value, props)
    expected = 'LeafNode(a, \'Should not be seen\', {\'href\': \'en.wikipedia.org\', \'target\': \'_blank\', \'onclick\': "console.log(\'Hello world\')"})'
    actual = f"{node}"
    self.assertEqual(expected, actual)


if __name__ == "main":
  unittest.main()
