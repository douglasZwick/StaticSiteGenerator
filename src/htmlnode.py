from collections.abc import Sequence, Mapping


class HTMLNode:
  PRETTY_PRINT: bool = False
  INDENT_SIZE: int = 2

  tag: str | None
  value: str | None
  children: "Sequence[HTMLNode] | None"
  props: Mapping[str, str | None] | None

  def __init__(self,
      tag: str | None = None,
      value: str | None = None,
      children: "Sequence[HTMLNode] | None" = None,
      props: Mapping[str, str | None] | None = None) -> None:
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  
  def to_html(self, level: int = 0) -> str:
    raise NotImplementedError()
  

  def open_tag_html(self) -> str:
    if self.tag is None:
      raise ValueError("Tried to get open tag HTML for node with no tag")
    
    open_tag = self.tag
    if self.props is not None and len(self.props) > 0:
      open_tag += f' {self.props_to_html()}'
    
    return f'<{open_tag}>'
  

  def close_tag_html(self) -> str:
    if self.tag is None:
      raise ValueError("Tried to get close tag HTML for node with no tag")

    return f'</{self.tag}>'
  

  def props_to_html(self) -> str:
    if self.props is None or len(self.props) == 0:
      return ""
    
    mapper = lambda pair: pair[0] if pair[1] is None else HTMLNode._prop_to_str(pair[0], pair[1])
    items = self.props.items()
    prop_map = map(mapper, items)
    return " ".join(prop_map)
  

  def __repr__(self) -> str:
    return f'HTMLNode({self.tag}, \'{self.value}\', {self.children}, {self.props})'
  
  
  @staticmethod
  def _prop_to_str(key: str, value: str) -> str:
    return f'{key}="{value}"'
