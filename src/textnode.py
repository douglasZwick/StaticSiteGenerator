from enum import Enum


class TextType(Enum):
  PLAIN = "plain"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"


class TextNode:
  text: str
  text_type: TextType
  url: str | None

  def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
    self.text = text
    self.text_type = text_type
    self.url = url


  def __eq__(self, rhs: object) -> bool:
    for key, value in vars(rhs).items():
      if getattr(self, key) != value:
        return False
    return True
      

  def __repr__(self) -> str:
    return f"TextNode({self.text}, TextType.{self.text_type.name}, {self.url})"
