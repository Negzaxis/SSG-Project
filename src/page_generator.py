# This file has the page generator function
import os
from markdown_blocks import *
from pathlib import Path


def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)



def generate_page(basepath, from_path, template_path, dest_path):
    """
    Generate an HTML page from a markdown file using a template.
    
    Args:
        from_path (str): Path to the markdown file
        template_path (str): Path to the HTML template
        dest_path (str): Path where the henerated HTML filw will be saved
    """

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown_content = f.read()

    with open(template_path, "r") as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)

    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)
