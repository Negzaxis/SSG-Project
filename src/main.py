from textnode import TextNode, TextType
import os
import shutil
from page_generator import *

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def copy_static(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.makedirs(dest_dir)

    items = os.listdir(source_dir)

    for item in items:
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)

        if os.path.isfile(source_item):
            shutil.copy(source_item, dest_item)
            print(f"Copied file: {source_item} -> {dest_item}")
        else:
            os.mkdir(dest_item)
            print(f"Created directory: {dest_item}")
            copy_static(source_item, dest_item)

def main():
    copy_static("static", "public")

    # Process all markdown files in content directory
    for root, dirs, files in os.walk("content"):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                
                # Get the relative path from content directory
                rel_path = os.path.relpath(from_path, "content")
                
                # Create the corresponding path in public directory
                # Replace .md with .html for the destination
                dest_path = os.path.join("public", os.path.splitext(rel_path)[0] + ".html")
                
                # Make sure the destination directory exists
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                print("Generating content...")
                generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()


