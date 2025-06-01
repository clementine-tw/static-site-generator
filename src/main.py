import os
import shutil
from copystatic import copy_files_recursive
from textnode import TextType, TextNode
from htmlpage import generate_page_recursive

PUBLIC_DIR = "./public"
STATIC_DIR = "./static"
CONTENT_DIR = "./content"

TEMPLATE = "./template.html"


def main():
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)

    copy_files_recursive(STATIC_DIR, PUBLIC_DIR)

    generate_page_recursive(CONTENT_DIR, TEMPLATE, PUBLIC_DIR)


if __name__ == "__main__":
    main()
