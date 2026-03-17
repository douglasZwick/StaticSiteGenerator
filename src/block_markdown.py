from enum import Enum
from collections.abc import Sequence
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from inline_markdown import text_to_text_nodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
  P = "P"
  H = "H"
  CODE = "CODE"
  QUOTE = "QUOTE"
  UL = "UL"
  OL = "OL"


def markdown_to_blocks(markdown: str) -> list[str]:
  output = []
  blocks = markdown.split("\n\n")
  
  for block in blocks:
    stripped = block.strip()
    if stripped == "":
      continue

    output.append(stripped)

  return output


def block_to_block_type(markdown_block: str) -> BlockType:
  lines = markdown_block.split("\n")

  if markdown_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
    return BlockType.H
  
  if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
    return BlockType.CODE
  
  if all(line.startswith(">") for line in lines):
    return BlockType.QUOTE
  
  if all(line.startswith("- ") for line in lines):
    return BlockType.UL
  
  if all(line.startswith(f"{line_number + 1}. ") for line_number, line in enumerate(lines)):
    return BlockType.OL
  
  return BlockType.P


def markdown_block_to_children(markdown_block: str) -> list[HTMLNode]:
  text_nodes = text_to_text_nodes(markdown_block)
  return list(map(text_node_to_html_node, text_nodes))


def extract_paragraph_content(text: str) -> str:
  return text.strip().replace("\n", " ")


def get_header_depth(header_block: str) -> int:
  i = 0
  while header_block[i] == "#":
    i += 1
  return i


def extract_header_content(text: str) -> str:
  return text.lstrip("#").strip()


def extract_code_content(text: str) -> str:
  return text.removeprefix("```").removesuffix("```").lstrip()


def extract_quote_content(text: str) -> str:
  lines = text.split("\n")
  output_lines = []

  for line in lines:
    output_lines.append(line.strip().lstrip(">").lstrip())
  
  return "\n".join(output_lines)


def extract_ul_line(text: str) -> str:
  return text[2:]


def extract_ul_lines(text: str) -> map:
  return map(extract_ul_line, text.split("\n"))


def extract_ol_line(text: str) -> str:
  return text[text.index(".") + 2:]


def extract_ol_lines(text: str) -> map:
  return map(extract_ol_line, text.split("\n"))


def create_li_node(line: str) -> ParentNode:
  children = markdown_block_to_children(line)
  return ParentNode("li", children)


def create_li_nodes(lines: map) -> list[ParentNode]:
  return list(map(create_li_node, lines))


def create_p_node(markdown_block: str) -> ParentNode:
  content = extract_paragraph_content(markdown_block)
  children = markdown_block_to_children(content)
  return ParentNode("p", children)


def create_h_node(markdown_block: str) -> ParentNode:
  content = extract_header_content(markdown_block)
  children = markdown_block_to_children(content)
  tag = f"h{get_header_depth(markdown_block)}"
  return ParentNode(tag, children)


def create_code_node(markdown_block: str) -> ParentNode:
  content = extract_code_content(markdown_block)
  text_node = TextNode(content, TextType.CODE)
  code_node = text_node_to_html_node(text_node)
  return ParentNode("pre", [code_node])


def create_quote_node(markdown_block: str) -> ParentNode:
  content = extract_quote_content(markdown_block)
  children = markdown_block_to_children(content)
  return ParentNode("blockquote", children)


def create_ul_node(markdown_block: str) -> ParentNode:
  lines = extract_ul_lines(markdown_block)
  li_nodes = create_li_nodes(lines)
  return ParentNode("ul", li_nodes)


def create_ol_node(markdown_block: str) -> ParentNode:
  lines = extract_ol_lines(markdown_block)
  li_nodes = create_li_nodes(lines)
  return ParentNode("ol", li_nodes)
  

def markdown_to_html_node(markdown: str) -> HTMLNode:
  nodes = []
  blocks = markdown_to_blocks(markdown)

  for block in blocks:
    block_type = block_to_block_type(block)
    node = None

    # Match on block_type and make a new HTMLNode based on it
    match block_type:
      case BlockType.P:
        node = create_p_node(block)
      case BlockType.H:
        node = create_h_node(block)
      case BlockType.CODE:
        node = create_code_node(block)
      case BlockType.QUOTE:
        node = create_quote_node(block)
      case BlockType.UL:
        node = create_ul_node(block)
      case BlockType.OL:
        node = create_ol_node(block)
      case _:
        raise ValueError(f"Unsupported block type: {block_type}")
    
    nodes.append(node)

  return ParentNode("div", nodes)
