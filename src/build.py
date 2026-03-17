import os
from block_markdown import markdown_to_html_node


def extract_title(markdown: str) -> str:
  lines = markdown.split("\n")
  for line in lines:
    line = line.strip()
    if not line.startswith("# "):
      continue
    return line.removeprefix("# ").lstrip()
  raise Exception("No h1 header found in markdown file")


def generate_page(
    basepath: str,
    src_path: str,
    template_path: str,
    dst_path: str,
    depth: int = 0) -> None:
  indent = "  " * depth
  file_name, _ = os.path.splitext(dst_path)
  dst_path = f"{file_name}.html"
  print(f"{indent}Generating {dst_path} from {src_path}...")

  with open(src_path) as markdown_file, open(template_path) as template_file:
    markdown, template = markdown_file.read(), template_file.read()

  html_node = markdown_to_html_node(markdown)
  html_text = html_node.to_html()
  title = extract_title(markdown)
  html_text = template.replace("{{ Title }}", title).replace("{{ Content }}", html_text)
  html_text = html_text.replace('href="/', f'href="{basepath}')
  html_text = html_text.replace('src="/', f'src="{basepath}')

  dst_dir_path = os.path.dirname(dst_path)
  if not os.path.exists(dst_dir_path):
    os.makedirs(dst_dir_path)

  with open(dst_path, "x") as dst:
    bytes_written = dst.write(html_text)
  
  print(f"{indent}  ...Finished (wrote {bytes_written} bytes)")


def generate_pages(
    basepath: str,
    src_dir_path: str,
    template_path: str,
    dst_dir_path: str) -> None:
  print(f"Generating website from {src_dir_path} " \
    f"to {dst_dir_path} using template {template_path}")
  generate_pages_r(basepath, src_dir_path, template_path, dst_dir_path, 0)


def generate_pages_r(
    basepath: str,
    src_dir_path: str,
    template_path: str,
    dst_dir_path: str,
    depth: int = 0) -> None:
  with os.scandir(src_dir_path) as entries:
    for entry in entries:
      from_path = os.path.join(src_dir_path, entry.name)
      dst_path = os.path.join(dst_dir_path, entry.name)

      if os.path.isfile(entry):
        _, ext = os.path.splitext(entry)
        
        if ext != ".md":
          continue

        generate_page(basepath, from_path, template_path, dst_path, depth + 1)
      else:
        generate_pages_r(basepath, from_path, template_path, dst_path, depth + 1)
