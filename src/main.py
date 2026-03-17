from parentnode import *
from leafnode import *
from inline_markdown import *
from block_markdown import *


def main() -> None:
  text = """
Begin with an ordinary paragraph. Then we'll do a header.

#### THIS IS THE HEADER I MENTIONED

```
next:
  some_code()
```
"""
  node = markdown_to_html_node(text)
  print(text)
  print(node.to_html())


main()
