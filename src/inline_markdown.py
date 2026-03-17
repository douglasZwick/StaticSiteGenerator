from collections.abc import Sequence
from textnode import TextNode, TextType
from urlextraction import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(
    old_nodes: Sequence[TextNode],
    delimiter: str,
    text_type: TextType) -> list[TextNode]:
  new_nodes = []

  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue

    text = node.text
    
    if text.count(delimiter) % 2 != 0:
      raise ValueError(f'Unmatched delimiter {delimiter} in text node')
    
    active = True
    split_parts = node.text.split(delimiter)
    for part in split_parts:
      active = not active
      if part == "":
        continue

      new_nodes.append(TextNode(part, text_type if active else TextType.TEXT))

  return new_nodes


def split_nodes_image(old_nodes: Sequence[TextNode]) -> list[TextNode]:
  new_nodes = []

  for node in old_nodes:
    # TODO:
    #   It may be that we should not actually allow BOLD, ITALIC, or CODE text types here
    if node.text_type in (TextType.IMAGE, TextType.LINK):
      new_nodes.append(node)
      continue

    matches = extract_markdown_images(node.text)

    if len(matches) == 0:
      new_nodes.append(node)
      continue

    to_split = node.text

    for alt, url in matches:
      parts = to_split.split(f"![{alt}]({url})", 1)
      
      pre = parts[0]
      if pre != "":
        new_nodes.append(TextNode(pre, TextType.TEXT))
      new_nodes.append(TextNode(alt, TextType.IMAGE, url))
      to_split = parts[1]
    
    if to_split != "":
      new_nodes.append(TextNode(to_split, TextType.TEXT))

  return new_nodes


def split_nodes_link(old_nodes: Sequence[TextNode]) -> list[TextNode]:
  # TODO:
  #   Maaaybe be a tiny bit less grug idk

  new_nodes = []

  for node in old_nodes:
    # TODO:
    #   It may be that we should not actually allow BOLD, ITALIC, or CODE text types here
    if node.text_type in (TextType.IMAGE, TextType.LINK):
      new_nodes.append(node)
      continue
    
    matches = extract_markdown_links(node.text)

    if len(matches) == 0:
      new_nodes.append(node)
      continue

    to_split = node.text

    for anchor, url in matches:
      parts = to_split.split(f"[{anchor}]({url})")

      pre = parts[0]
      if pre != "":
        new_nodes.append(TextNode(pre, TextType.TEXT))
      new_nodes.append(TextNode(anchor, TextType.LINK, url))
      to_split = parts[1]

    if to_split != "":
      new_nodes.append(TextNode(to_split, TextType.TEXT))

  return new_nodes


def text_to_text_nodes(text: str) -> list[TextNode]:
  input = [TextNode(text, TextType.TEXT)]
  output = split_nodes_image(input)
  output = split_nodes_link(output)
  output = split_nodes_delimiter(output, TextNode.BOLD_DELIMITER, TextType.BOLD)
  output = split_nodes_delimiter(output, TextNode.ITALIC_DELIMITER, TextType.ITALIC)
  output = split_nodes_delimiter(output, TextNode.CODE_DELIMITER, TextType.CODE)
  return output
