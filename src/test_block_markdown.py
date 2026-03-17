import unittest
from block_markdown import (
  BlockType,
  markdown_to_blocks,
  block_to_block_type,
  markdown_to_html_node, )


class TestMarkdownToBlocks(unittest.TestCase):
  def test_markdown_to_blocks(self) -> None:
    markdown = """
This is a simple block consisting of a bunch of text that may have some formatting, or it may not. It doesn't really matter too much. It can have multiple sentences, and it could in theory have multiple newlines, as long as there aren't two or more in a row.

We're now **finally** in a new block.
And here we're _still in the same block._

## Some blocks:

- contain lists
- `contain formatting`
- are headers
- have **feelings**

### Some lists:

1. Are ordered
2. Are unordered
3. Have only three elements

# AND NOW HERE IS A QUOTE:

> This quote
>> just keeps getting
>>> quotier and quotier
>>>> when will it end

Just one last ordinary paragraph, lest you forget these exist...!

```
This is one final block. The entire thing should be code-formatted. It may or may not contain actual code. The executability of this text is less important than that it is formatted as if it were code, regardless of whether it actually is code. So make of that what you will.
```
      """
    expected = [
      "This is a simple block consisting of a bunch of text that may have some formatting, or it may not. It doesn't really matter too much. It can have multiple sentences, and it could in theory have multiple newlines, as long as there aren't two or more in a row.",
      "We're now **finally** in a new block.\nAnd here we're _still in the same block._",
      "## Some blocks:",
      "- contain lists\n- `contain formatting`\n- are headers\n- have **feelings**",
      "### Some lists:",
      "1. Are ordered\n2. Are unordered\n3. Have only three elements",
      "# AND NOW HERE IS A QUOTE:",
      "> This quote\n>> just keeps getting\n>>> quotier and quotier\n>>>> when will it end",
      "Just one last ordinary paragraph, lest you forget these exist...!",
      "```\nThis is one final block. The entire thing should be code-formatted. It may or may not contain actual code. The executability of this text is less important than that it is formatted as if it were code, regardless of whether it actually is code. So make of that what you will.\n```",
    ]
    actual = markdown_to_blocks(markdown)
    self.assertListEqual(expected, actual)


class TestBlockToBlockType(unittest.TestCase):
  def test_block_to_block_type(self) -> None:
    blocks = [
      "This is a simple block consisting of a bunch of text that may have some formatting, or it may not. It doesn't really matter too much. It can have multiple sentences, and it could in theory have multiple newlines, as long as there aren't two or more in a row.",
      "We're now **finally** in a new block.\nAnd here we're _still in the same block._",
      "## Some blocks:",
      "- contain lists\n- `contain formatting`\n- are headers\n- have **feelings**",
      "### Some lists:",
      "1. Are ordered\n2. Are unordered\n3. Have only three elements",
      "# AND NOW HERE IS A QUOTE:",
      "> This quote\n>> just keeps getting\n>>> quotier and quotier\n>>>> when will it end",
      "Just one last ordinary paragraph, lest you forget these exist...!",
      "```\nThis is one final block. The entire thing should be code-formatted. It may or may not contain actual code. The executability of this text is less important than that it is formatted as if it were code, regardless of whether it actually is code. So make of that what you will.\n```",
    ]
    expected = [
      BlockType.P,
      BlockType.P,
      BlockType.H,
      BlockType.UL,
      BlockType.H,
      BlockType.OL,
      BlockType.H,
      BlockType.QUOTE,
      BlockType.P,
      BlockType.CODE,
    ]
    actual = list(map(block_to_block_type, blocks))
    self.assertListEqual(expected, actual)


class TestMarkdownToHtmlNode(unittest.TestCase):
  def test_paragraphs(self) -> None:
    markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""
    node = markdown_to_html_node(markdown)
    expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>" \
      "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
    actual = node.to_html()
    self.assertEqual(expected, actual)

  def test_code_block(self) -> None:
    markdown = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    node = markdown_to_html_node(markdown)
    expected = "<div><pre><code>This is text that _should_ remain\n" \
      "the **same** even with inline stuff\n</code></pre></div>"
    actual = node.to_html()
    self.assertEqual(expected, actual)


if __name__ == "main":
  unittest.main()
