import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from parentnode import ParentNode
from inline_markdown import (
  split_nodes_delimiter,
  split_nodes_image,
  split_nodes_link,
  text_to_text_nodes)


class TestSplitNodesDelimiter(unittest.TestCase):
  def test_basic_bold(self) -> None:
    nodes = [
      TextNode("Hello world", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)
    expected_count = 1
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    expected_value = "Hello world"
    actual_value = output[0].text
    self.assertEqual(expected_value, actual_value)

  def test_basic_type_mismatch_bold(self) -> None:
    nodes = [
      TextNode("Hello world", TextType.BOLD)
    ]

    output = split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)
    expected_count = 1
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    expected_value = "Hello world"
    actual_value = output[0].text
    self.assertEqual(expected_value, actual_value)

  def test_front_bold_1(self) -> None:
    nodes = [
      TextNode("**Hello** world", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)
    expected_count = 2
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span><b>Hello</b> world</span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_back_bold_1(self) -> None:
    nodes = [
      TextNode("Hello **world**", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)
    expected_count = 2
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span>Hello <b>world</b></span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_middle_bold_1(self) -> None:
    nodes = [
      TextNode("Hello **beautiful** world", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)
    expected_count = 3
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span>Hello <b>beautiful</b> world</span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_all_bold_3(self) -> None:
    nodes = [
      TextNode("**Hello** **beautiful** **world**", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)
    expected_count = 5
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span><b>Hello</b> <b>beautiful</b> <b>world</b></span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_double_bold(self) -> None:
    nodes = [
      TextNode("**Hello****world**", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)
    expected_count = 2
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span><b>Hello</b><b>world</b></span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_extra_bold(self) -> None:
    nodes = [
      TextNode("****WOW!!****", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)
    expected_count = 1
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span>WOW!!</span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_multi_node_bold(self) -> None:
    nodes = [
      TextNode("Lorem **ipsum** dolor **sit** amet, ", TextType.TEXT),
      TextNode("Consectetur **adipisicing** elit, **elit**, elit ", TextType.TEXT),
      TextNode("Ut **enim** ad **minim**, minim **veniam** ", TextType.TEXT),
      TextNode("**Quis** nostrud **excer** excercitacion", TextType.TEXT),
    ]

    output = split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)
    expected_count = 21
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("p", children)
    expected_str = \
      '<p>Lorem <b>ipsum</b> dolor <b>sit</b> amet, ' \
      'Consectetur <b>adipisicing</b> elit, <b>elit</b>, elit ' \
      'Ut <b>enim</b> ad <b>minim</b>, minim <b>veniam</b> ' \
      '<b>Quis</b> nostrud <b>excer</b> excercitacion</p>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_front_italic_1(self) -> None:
    nodes = [
      TextNode("_Hello_ world", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.ITALIC_DELIMITER, TextType.ITALIC)
    expected_count = 2
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span><i>Hello</i> world</span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_back_italic_1(self) -> None:
    nodes = [
      TextNode("Hello _world_", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.ITALIC_DELIMITER, TextType.ITALIC)
    expected_count = 2
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span>Hello <i>world</i></span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_middle_italic_1(self) -> None:
    nodes = [
      TextNode("Hello _beautiful_ world", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.ITALIC_DELIMITER, TextType.ITALIC)
    expected_count = 3
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span>Hello <i>beautiful</i> world</span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_all_italic_3(self) -> None:
    nodes = [
      TextNode("_Hello_ _beautiful_ _world_", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.ITALIC_DELIMITER, TextType.ITALIC)
    expected_count = 5
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span><i>Hello</i> <i>beautiful</i> <i>world</i></span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_double_italic(self) -> None:
    nodes = [
      TextNode("_Hello__world_", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.ITALIC_DELIMITER, TextType.ITALIC)
    expected_count = 2
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span><i>Hello</i><i>world</i></span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_extra_italic(self) -> None:
    nodes = [
      TextNode("__WOW!!__", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.ITALIC_DELIMITER, TextType.ITALIC)
    expected_count = 1
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span>WOW!!</span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_multi_node_italic(self) -> None:
    nodes = [
      TextNode("Lorem _ipsum_ dolor _sit_ amet, ", TextType.TEXT),
      TextNode("Consectetur _adipisicing_ elit, _elit_, elit ", TextType.TEXT),
      TextNode("Ut _enim_ ad _minim_, minim _veniam_ ", TextType.TEXT),
      TextNode("_Quis_ nostrud _excer_ excercitacion", TextType.TEXT),
    ]

    output = split_nodes_delimiter(nodes, TextNode.ITALIC_DELIMITER, TextType.ITALIC)
    expected_count = 21
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("p", children)
    expected_str = \
      '<p>Lorem <i>ipsum</i> dolor <i>sit</i> amet, ' \
      'Consectetur <i>adipisicing</i> elit, <i>elit</i>, elit ' \
      'Ut <i>enim</i> ad <i>minim</i>, minim <i>veniam</i> ' \
      '<i>Quis</i> nostrud <i>excer</i> excercitacion</p>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_front_code_1(self) -> None:
    nodes = [
      TextNode("`Hello` world", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.CODE_DELIMITER, TextType.CODE)
    expected_count = 2
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span><code>Hello</code> world</span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_back_code_1(self) -> None:
    nodes = [
      TextNode("Hello `world`", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.CODE_DELIMITER, TextType.CODE)
    expected_count = 2
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span>Hello <code>world</code></span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_middle_code_1(self) -> None:
    nodes = [
      TextNode("Hello `beautiful` world", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.CODE_DELIMITER, TextType.CODE)
    expected_count = 3
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span>Hello <code>beautiful</code> world</span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_all_code_3(self) -> None:
    nodes = [
      TextNode("`Hello` `beautiful` `world`", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.CODE_DELIMITER, TextType.CODE)
    expected_count = 5
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)
    
    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span><code>Hello</code> <code>beautiful</code> <code>world</code></span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_double_code(self) -> None:
    nodes = [
      TextNode("`Hello``world`", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.CODE_DELIMITER, TextType.CODE)
    expected_count = 2
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span><code>Hello</code><code>world</code></span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_extra_code(self) -> None:
    nodes = [
      TextNode("``WOW!!``", TextType.TEXT)
    ]

    output = split_nodes_delimiter(nodes, TextNode.CODE_DELIMITER, TextType.CODE)
    expected_count = 1
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("span", children)
    expected_str = '<span>WOW!!</span>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_multi_node_code(self) -> None:
    nodes = [
      TextNode("Lorem `ipsum` dolor `sit` amet, ", TextType.TEXT),
      TextNode("Consectetur `adipisicing` elit, `elit`, elit ", TextType.TEXT),
      TextNode("Ut `enim` ad `minim`, minim `veniam` ", TextType.TEXT),
      TextNode("`Quis` nostrud `excer` excercitacion", TextType.TEXT),
    ]

    output = split_nodes_delimiter(nodes, TextNode.CODE_DELIMITER, TextType.CODE)
    expected_count = 21
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("p", children)
    expected_str = \
      '<p>Lorem <code>ipsum</code> dolor <code>sit</code> amet, ' \
      'Consectetur <code>adipisicing</code> elit, <code>elit</code>, elit ' \
      'Ut <code>enim</code> ad <code>minim</code>, minim <code>veniam</code> ' \
      '<code>Quis</code> nostrud <code>excer</code> excercitacion</p>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_multi_node_mixed(self) -> None:
    nodes = [
      TextNode("`Lorem ipsum` dolor _sit_ amet, ", TextType.TEXT),
      TextNode("Consectetur **adipisicing** elit, **elit**, _elit_ ", TextType.TEXT),
      TextNode("Ut _enim ad minim_, `minim veniam` ", TextType.TEXT),
      TextNode("`Quis` nostrud **excer** excercitacion", TextType.TEXT),
    ]

    output = split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)
    expected_count = 10
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("p", children)
    expected_str = \
      '<p>`Lorem ipsum` dolor _sit_ amet, ' \
      'Consectetur <b>adipisicing</b> elit, <b>elit</b>, _elit_ ' \
      'Ut _enim ad minim_, `minim veniam` ' \
      '`Quis` nostrud <b>excer</b> excercitacion</p>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

    output = split_nodes_delimiter(output, TextNode.ITALIC_DELIMITER, TextType.ITALIC)
    expected_count = 16
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("p", children)
    expected_str = \
      '<p>`Lorem ipsum` dolor <i>sit</i> amet, ' \
      'Consectetur <b>adipisicing</b> elit, <b>elit</b>, <i>elit</i> ' \
      'Ut <i>enim ad minim</i>, `minim veniam` ' \
      '`Quis` nostrud <b>excer</b> excercitacion</p>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

    output = split_nodes_delimiter(output, TextNode.CODE_DELIMITER, TextType.CODE)
    expected_count = 20
    actual_count = len(output)
    self.assertEqual(expected_count, actual_count)

    children = list(map(text_node_to_html_node, output))
    parent = ParentNode("p", children)
    expected_str = \
      '<p><code>Lorem ipsum</code> dolor <i>sit</i> amet, ' \
      'Consectetur <b>adipisicing</b> elit, <b>elit</b>, <i>elit</i> ' \
      'Ut <i>enim ad minim</i>, <code>minim veniam</code> ' \
      '<code>Quis</code> nostrud <b>excer</b> excercitacion</p>'
    actual_str = parent.to_html()
    self.assertEqual(expected_str, actual_str)

  def test_unmatched_bold_raise_1(self) -> None:
    nodes = [
      TextNode("**Hello gorgeous beautiful fucked-up world", TextType.TEXT)
    ]

    with self.assertRaises(ValueError):
      split_nodes_delimiter(nodes, TextNode.BOLD_DELIMITER, TextType.BOLD)

  def test_unmatched_italic_raise_3(self) -> None:
    nodes = [
      TextNode("_Hello_ gorgeous _beautiful fucked-up world", TextType.TEXT)
    ]

    with self.assertRaises(ValueError):
      split_nodes_delimiter(nodes, TextNode.ITALIC_DELIMITER, TextType.ITALIC)

  def test_unmatched_code_raise_5(self) -> None:
    nodes = [
      TextNode("`Hello` gorgeous `beautiful` fucked-up `world", TextType.TEXT)
    ]

    with self.assertRaises(ValueError):
      split_nodes_delimiter(nodes, TextNode.CODE_DELIMITER, TextType.CODE)


class TestSplitNodesImage(unittest.TestCase):
  def test_basic(self) -> None:
    nodes = [
      TextNode("Text before image ![abc](xyz.com/a.png) text after image", TextType.TEXT),
    ]

    expected = [
      TextNode("Text before image ", TextType.TEXT),
      TextNode("abc", TextType.IMAGE, "xyz.com/a.png"),
      TextNode(" text after image", TextType.TEXT),
    ]
    actual = split_nodes_image(nodes)
    self.assertListEqual(expected, actual)

  def test_empty_before(self) -> None:
    nodes = [
      TextNode("![abc](xyz.com/a.png) text after image", TextType.TEXT),
    ]

    expected = [
      TextNode("abc", TextType.IMAGE, "xyz.com/a.png"),
      TextNode(" text after image", TextType.TEXT),
    ]
    actual = split_nodes_image(nodes)
    self.assertListEqual(expected, actual)

  def test_empty_after(self) -> None:
    nodes = [
      TextNode("Text before image ![abc](xyz.com/a.png)", TextType.TEXT),
    ]

    expected = [
      TextNode("Text before image ", TextType.TEXT),
      TextNode("abc", TextType.IMAGE, "xyz.com/a.png"),
    ]
    actual = split_nodes_image(nodes)
    self.assertListEqual(expected, actual)

  def test_two_images(self) -> None:
    nodes = [
      TextNode("![abc](qrs.com/a.png) between ![def](tuv.com/b.jpg)", TextType.TEXT),
    ]

    expected = [
      TextNode("abc", TextType.IMAGE, "qrs.com/a.png"),
      TextNode(" between ", TextType.TEXT),
      TextNode("def", TextType.IMAGE, "tuv.com/b.jpg"),
    ]
    actual = split_nodes_image(nodes)
    self.assertListEqual(expected, actual)

  def test_image_and_link_same_node(self) -> None:
    nodes = [
      TextNode("![abc](qrs.com/a.png) between [link anchor](tuv.com)", TextType.TEXT),
    ]

    expected = [
      TextNode("abc", TextType.IMAGE, "qrs.com/a.png"),
      TextNode(" between [link anchor](tuv.com)", TextType.TEXT),
    ]
    actual = split_nodes_image(nodes)
    self.assertListEqual(expected, actual)

  def test_image_and_link_separate_nodes(self) -> None:
    nodes = [
      TextNode("Text before image ![abc](qrs.com/a.png) text after image", TextType.TEXT),
      TextNode("Text before link [link anchor](tuv.com) text after link", TextType.TEXT),
    ]

    expected = [
      TextNode("Text before image ", TextType.TEXT),
      TextNode("abc", TextType.IMAGE, "qrs.com/a.png"),
      TextNode(" text after image", TextType.TEXT),
      TextNode("Text before link [link anchor](tuv.com) text after link", TextType.TEXT),
    ]
    actual = split_nodes_image(nodes)
    self.assertListEqual(expected, actual)


class TestSplitNodesLink(unittest.TestCase):
  def test_basic(self) -> None:
    nodes = [
      TextNode("Text before link [link anchor](tuv.com) text after link", TextType.TEXT),
    ]

    expected = [
      TextNode("Text before link ", TextType.TEXT),
      TextNode("link anchor", TextType.LINK, "tuv.com"),
      TextNode(" text after link", TextType.TEXT),
    ]
    actual = split_nodes_link(nodes)
    self.assertListEqual(expected, actual)

  def test_empty_before(self) -> None:
    nodes = [
      TextNode("[link anchor](tuv.com) text after link", TextType.TEXT),
    ]

    expected = [
      TextNode("link anchor", TextType.LINK, "tuv.com"),
      TextNode(" text after link", TextType.TEXT),
    ]
    actual = split_nodes_link(nodes)
    self.assertListEqual(expected, actual)

  def test_empty_after(self) -> None:
    nodes = [
      TextNode("Text before link [link anchor](tuv.com)", TextType.TEXT),
    ]

    expected = [
      TextNode("Text before link ", TextType.TEXT),
      TextNode("link anchor", TextType.LINK, "tuv.com"),
    ]
    actual = split_nodes_link(nodes)
    self.assertListEqual(expected, actual)

  def test_two_links(self) -> None:
    nodes = [
      TextNode("[link anchor a](abc.com) between [link anchor b](xyz.com)", TextType.TEXT),
    ]

    expected = [
      TextNode("link anchor a", TextType.LINK, "abc.com"),
      TextNode(" between ", TextType.TEXT),
      TextNode("link anchor b", TextType.LINK, "xyz.com"),
    ]
    actual = split_nodes_link(nodes)
    self.assertListEqual(expected, actual)

  def test_image_and_link_same_node(self) -> None:
    nodes = [
      TextNode("![abc](qrs.com/a.png) between [link anchor](tuv.com)", TextType.TEXT),
    ]

    expected = [
      TextNode("![abc](qrs.com/a.png) between ", TextType.TEXT),
      TextNode("link anchor", TextType.LINK, "tuv.com"),
    ]
    actual = split_nodes_link(nodes)
    self.assertListEqual(expected, actual)

  def test_image_and_link_separate_nodes(self) -> None:
    nodes = [
      TextNode("Text before image ![abc](qrs.com/a.png) text after image", TextType.TEXT),
      TextNode("Text before link [link anchor](tuv.com) text after link", TextType.TEXT),
    ]

    expected = [
      TextNode("Text before image ![abc](qrs.com/a.png) text after image", TextType.TEXT),
      TextNode("Text before link ", TextType.TEXT),
      TextNode("link anchor", TextType.LINK, "tuv.com"),
      TextNode(" text after link", TextType.TEXT),
    ]
    actual = split_nodes_link(nodes)
    self.assertListEqual(expected, actual)


class TestTextToTextNodes(unittest.TestCase):
  def test_with_boot_dev_example(self) -> None:
    text = \
      "This is **text** with an _italic_ word and a `code block` and an " \
      "![Obi-Wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev/)"
    
    expected = [
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.BOLD),
      TextNode(" with an ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" word and a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" and an ", TextType.TEXT),
      TextNode("Obi-Wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
      TextNode(" and a ", TextType.TEXT),
      TextNode("link", TextType.LINK, "https://boot.dev/"),
    ]
    actual = text_to_text_nodes(text)
    self.assertListEqual(expected, actual)


if __name__ == "main":
  unittest.main()
