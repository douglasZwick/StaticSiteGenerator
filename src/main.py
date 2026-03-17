import os
import shutil
from parentnode import *
from leafnode import *
from inline_markdown import *
from block_markdown import *
from copy_source import copy_source
from build import generate_pages


STATIC_DIR_PATH: str = "./static"
PUBLIC_DIR_PATH: str = "./public"
MARKDOWN_CONTENT_PATH: str = "content"
HTML_TEMPLATE_PATH: str = "template.html"
HTML_OUTPUT_PATH: str = PUBLIC_DIR_PATH


def main() -> None:
  if os.path.exists(PUBLIC_DIR_PATH):
    print("Cleaning up existing public directory...")
    shutil.rmtree(PUBLIC_DIR_PATH)
  
  copy_source(STATIC_DIR_PATH, PUBLIC_DIR_PATH)
  generate_pages(MARKDOWN_CONTENT_PATH, HTML_TEMPLATE_PATH, HTML_OUTPUT_PATH)


main()
