from parentnode import *
from leafnode import *
from inline_markdown import *
from block_markdown import *
from build import copy_to_dst


def main() -> None:
  copy_to_dst("static", "public")


main()
