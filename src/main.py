import os
import shutil
from parentnode import *
from leafnode import *
from inline_markdown import *
from block_markdown import *
from copy_source import copy_source


STATIC_DIR_PATH: str = "./static"
PUBLIC_DIR_PATH: str = "./public"


def main() -> None:
  if os.path.exists(PUBLIC_DIR_PATH):
    print("Cleaning up existing public directory...")
    shutil.rmtree(PUBLIC_DIR_PATH)
  
  copy_source(STATIC_DIR_PATH, PUBLIC_DIR_PATH)


main()
