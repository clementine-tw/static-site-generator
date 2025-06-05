import os
from block_markdown import markdown_to_html_node


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# ") and len(line) > 2:
            return line[2:]
    raise Exception("level 1 header is not found")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md_file:
        md_content = md_file.read()

    with open(template_path) as template_file:
        template_content = template_file.read()

    html_node = markdown_to_html_node(md_content)
    html_content = html_node.to_html()

    title = extract_title(md_content)
    html = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_content
    )
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as html_file:
        html_file.write(html)


def generate_page_recursive(from_path, template, to_path, basepath):
    for dir in os.listdir(from_path):
        new_path = os.path.join(from_path, dir)
        if os.path.isfile(new_path):
            if not dir.endswith(".md"):
                raise Exception(
                    f"the source file must be markdown file with '.md': {new_path}"
                )
            generate_page(
                new_path,
                template,
                os.path.join(to_path, dir.replace(".md", ".html")),
                basepath,
            )
        else:
            generate_page_recursive(
                new_path,
                template,
                os.path.join(to_path, dir),
                basepath,
            )
