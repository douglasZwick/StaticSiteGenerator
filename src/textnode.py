from enum import Enum
from htmlnode import HTMLNode
from leafnode import LeafNode


class TextType(Enum):
  TEXT = "text"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"


class TextNode:
  BOLD_DELIMITER: str = "**"
  ITALIC_DELIMITER: str = "_"
  CODE_DELIMITER: str = "`"

  text: str
  text_type: TextType
  url: str | None

  def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
    self.text = text
    self.text_type = text_type
    self.url = url


  def __eq__(self, value: object) -> bool:
    for key, value in vars(value).items():
      if getattr(self, key) != value:
        return False
    return True
      

  def __repr__(self) -> str:
    url_block = "" if self.url is None else f', "{self.url}"'
    return f'TextNode("{self.text}", TextType.{self.text_type.name}{url_block})'


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
  value = text_node.text

  match text_node.text_type:
    case TextType.TEXT:
      return LeafNode(None, text_node.text)
    case TextType.BOLD:
      return LeafNode("b", value)
    case TextType.ITALIC:
      return LeafNode("i", value)
    case TextType.CODE:
      return LeafNode("code", value)
    case TextType.LINK:
      return LeafNode("a", value, {"href": text_node.url})
    case TextType.IMAGE:
      return LeafNode("img", "", {"src": text_node.url, "alt": value})
    case _:
      raise ValueError("Unsupported TextType for TextNode")
