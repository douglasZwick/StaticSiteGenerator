from collections.abc import Sequence, Mapping
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
  def __init__(self,
      tag: str,
      children: "Sequence[HTMLNode]",
      props: Mapping[str, str | None] | None = None) -> None:
    super().__init__(tag, None, children, props)

  
  def to_html(self, level: int = 0) -> str:
    if HTMLNode.PRETTY_PRINT:
      return self._to_html_pretty(level)
    
    if self.tag is None:
      raise ValueError("Every parent node must have a tag")
    if self.children is None or len(self.children) == 0:
      raise ValueError("Every parent node must have children")
    
    open_tag = self.open_tag_html()
    children_str = ""
    for child in self.children:
      children_str += child.to_html()
    close_tag = self.close_tag_html()

    return f'{open_tag}{children_str}{close_tag}'

  
  def _to_html_pretty(self, level: int) -> str:
    if self.tag is None:
      raise ValueError("Every parent node must have a tag")
    if self.children is None or len(self.children) == 0:
      raise ValueError("Every parent node must have children")
    
    indent = " " * level * HTMLNode.INDENT_SIZE
    
    open_tag = indent + self.open_tag_html() + "\n"

    children_str = ""
    for child in self.children:
      children_str += child.to_html(level + 1)

    close_tag = indent + self.close_tag_html() + "\n"
    
    return f'{open_tag}{children_str}{close_tag}'
