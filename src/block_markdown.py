from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = []
    sections = markdown.split("\n\n")
    for section in sections:
        stripped = section.strip(" ").strip("\n")
        if stripped == "":
            continue
        blocks.append(stripped)
    return blocks


def check_heading(text):
    return re.search(r"^#{1,6} .+", text) != None


def check_code(text):
    lines = text.split("\n")
    if (
        len(lines) < 2
        or not lines[0].startswith("```")
        or not lines[-1].startswith("```")
    ):
        return False
    return True


def check_quote(text):
    lines = text.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True


def check_unordered_list(text):
    lines = text.split("\n")
    for line in lines:
        if not line.startswith("- "):
            return False
    return True


def check_ordered_list(text):
    lines = text.split("\n")
    num = 1
    for line in lines:
        if not line.startswith(f"{num}. "):
            return False
        num += 1
    return True


def block_to_block_type(block_text):
    if check_heading(block_text):
        return BlockType.HEADING
    if check_code(block_text):
        return BlockType.CODE
    if check_quote(block_text):
        return BlockType.QUOTE
    if check_unordered_list(block_text):
        return BlockType.UNORDERED_LIST
    if check_ordered_list(block_text):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
