def markdown_to_blocks(markdown):
    blocks = []
    sections = markdown.split("\n\n")
    for section in sections:
        stripped = section.strip(" ").strip("\n")
        if stripped == "":
            continue
        blocks.append(stripped)
    return blocks
