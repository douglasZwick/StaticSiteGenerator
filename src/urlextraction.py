import re


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
  image_url_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  return re.findall(image_url_pattern, text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
  link_url_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
  return re.findall(link_url_pattern, text)
