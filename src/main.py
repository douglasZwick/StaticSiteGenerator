from textnode import *


def main() -> None:
  text_node = TextNode("This is some anchor text", TextType.LINK, "https://en.wikipedia.org/")
  print(text_node)


main()
