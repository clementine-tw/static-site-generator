import re
from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.+?)\]\((.+?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.+?)\]\((.+?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        images = extract_markdown_images(old_node.text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        origin_text = old_node.text
        for image in images:
            alt = image[0]
            link = image[1]
            sections = origin_text.split(f"![{alt}]({link})", 1)
            if len(sections[0]) != 0:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(alt, TextType.IMAGE, link))
            origin_text = sections[1]
        if len(origin_text) != 0:
            split_nodes.append(TextNode(origin_text, TextType.TEXT))

        new_nodes.extend(split_nodes)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        images = extract_markdown_links(old_node.text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        origin_text = old_node.text
        for image in images:
            alt = image[0]
            link = image[1]
            sections = origin_text.split(f"[{alt}]({link})", 1)
            if len(sections[0]) != 0:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(alt, TextType.LINK, link))
            origin_text = sections[1]
        if len(origin_text) != 0:
            split_nodes.append(TextNode(origin_text, TextType.TEXT))

        new_nodes.extend(split_nodes)

    return new_nodes
