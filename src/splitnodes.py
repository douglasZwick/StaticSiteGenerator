from collections.abc import Sequence
from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: Sequence[TextNode],
    delimiter: str,
    text_type: TextType) -> Sequence[TextNode]:
  new_nodes: Sequence[TextNode] = []

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


def split_nodes_image(old_nodes: Sequence[TextNode]) -> Sequence[TextNode]:
  new_nodes: Sequence[TextNode] = []
  

  return new_nodes


def split_nodes_link(old_nodes: Sequence[TextNode]) -> Sequence[TextNode]:
  new_nodes: Sequence[TextNode] = []


  return new_nodes
