from parentnode import *
from leafnode import *


def main() -> None:
  node = ParentNode(
    "html",
    [
      ParentNode(
        "head",
        [
          LeafNode("script", "", {"type": "text/javascript", "async": None, "src": "https://example.code/"}),
          LeafNode("script", "", {"async": None, "src": "https://something.code/"}),
          LeafNode("meta", "", {"charset": "utf-8"}),
          LeafNode("meta", "", {"name": "viewport"}),
          LeafNode("title", "Build a Static Site Generator in Python: ParentNode | Boot.dev"),
          LeafNode("link", "", {"rel": "preconnect", "href": "https://use.typekit.net", "data-hid": "preconnect-typekit"}),
        ]
      ),
      ParentNode(
        "body",
        [
          ParentNode(
            "div",
            [
              ParentNode(
                "div",
                [
                  ParentNode(
                    "div",
                    [
                      ParentNode(
                        "div",
                        [
                          LeafNode("canvas", "", {"id": "confetti-canvas", "class": "w-screen h-screen bg-transparent", "width": "2560", "height": "1271"})
                        ], {"id": "confetti-container", "popover": "manual", "class": "bg-transparent pointer-events-none"}
                      )
                    ]
                  ),
                  ParentNode(
                    "div",
                    [
                      LeafNode("canvas", "", {"id": "confetti-canvas", "class": "w-screen h-screen bg-transparent"})
                    ], {"id": "confetti-container", "popover": "manual", "class": "bg-transparent pointer-events-none"}
                  )
                ], {"class": "h-dvh bg-gray-850 text-gray-200"}
              )
            ], {"id": "__nuxt"}
          )
        ]
      )
    ]
  )

  anchor = LeafNode("a", "A pasadise of sweet teats", {"href": "https://en.wikipedia.org/wiki/AI_slop"})
  paragraph_a = ParentNode("p", [anchor])
  bold = LeafNode("b", "Strong text for a strong guy")
  italic = LeafNode("i", "Italic text for an Italian guy")
  paragraph_b = ParentNode("p", [bold, italic], {"id": "targetParagraph", "class": "bold italic"})
  div = ParentNode("div", [paragraph_a, paragraph_b, paragraph_a])
  
  print(div.to_html())


main()
