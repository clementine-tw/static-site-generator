import os
import shutil
from copystatic import copy_files_recursive
from textnode import TextType, TextNode

PUBLIC_DIR = "./public"
STATIC_DIR = "./static"


def main():
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)

    copy_files_recursive(STATIC_DIR, PUBLIC_DIR)


if __name__ == "__main__":
    main()
