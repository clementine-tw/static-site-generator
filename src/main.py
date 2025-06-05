import os
import sys
import shutil
from copystatic import copy_files_recursive
from textnode import TextType, TextNode
from htmlpage import generate_page_recursive

PUBLIC_DIR = "./docs"
STATIC_DIR = "./static"
CONTENT_DIR = "./content"

TEMPLATE = "./template.html"


def main():
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)

    copy_files_recursive(STATIC_DIR, PUBLIC_DIR)

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    generate_page_recursive(CONTENT_DIR, TEMPLATE, PUBLIC_DIR, basepath)


if __name__ == "__main__":
    main()
