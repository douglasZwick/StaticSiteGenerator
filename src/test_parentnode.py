import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
  def test_to_html_with_children(self) -> None:
    child = LeafNode("span", "child")
    parent = ParentNode("div", [child])
    expected = "<div><span>child</span></div>"
    actual = parent.to_html()
    self.assertEqual(expected, actual)

  def test_to_html_with_grandchildren(self) -> None:
    grandchild = LeafNode("b", "grandchild")
    child = ParentNode("span", [grandchild])
    parent = ParentNode("div", [child])
    expected = "<div><span><b>grandchild</b></span></div>"
    actual = parent.to_html()
    self.assertEqual(expected, actual)

  def test_to_html_with_ref_copied_children(self) -> None:
    child = LeafNode("a", "Click here", {"href": "www.example.com"})
    parent = ParentNode("body", [child, child, child, child, child])
    child_str = '<a href="www.example.com">Click here</a>'
    expected = f"<body>{child_str * 5}</body>"
    actual = parent.to_html()
    self.assertEqual(expected, actual)

  def test_to_html_with_empty_children_list(self) -> None:
    parent = ParentNode("div", [])
    with self.assertRaises(ValueError):
      parent.to_html()

  def test_to_html_with_none_children(self) -> None:
    parent = ParentNode("div", [])
    parent.children = None
    with self.assertRaises(ValueError):
      parent.to_html()


if __name__ == "main":
  unittest.main()
