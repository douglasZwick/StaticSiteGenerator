from collections.abc import Mapping
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
  def __init__(self,
      tag: str | None,
      value: str,
      props: Mapping[str, str | None] | None = None) -> None:
    super().__init__(tag, value, None, props)

  
  def to_html(self, level: int = 0) -> str:
    if self.value is None:
      raise ValueError("Every leaf node must have a value")
    if self.tag is None:
      return self.value
    
    indent = " " * level * HTMLNode.INDENT_SIZE
    open_tag = self.open_tag_html()
    close_tag = self.close_tag_html()
    line_ending = "\n" if HTMLNode.PRETTY_PRINT and level > 0 else ""
    
    return f'{indent}{open_tag}{self.value}{close_tag}{line_ending}'


  def __repr__(self) -> str:
    return f'LeafNode({self.tag}, \'{self.value}\', {self.props})'
