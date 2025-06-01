from enum import Enum
import re
from htmlnode import ParentNode
from textnode import TextType, TextNode, text_node_to_html_node
from inline_markdown import text_to_textnodes


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


def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return olist_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return ulist_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def heading_to_html_node(block):
    level = 0
    for c in block:
        if c == "#":
            level += 1
        else:
            break

    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")

    children = text_to_children(block[level + 1 :])
    return ParentNode(f"h{level}", children)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote value")
        new_lines.append(line.lstrip(">").strip())
    children = text_to_children(" ".join(new_lines))
    return ParentNode("blockquote", children)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)
