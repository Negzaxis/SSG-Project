from textnode import TextNode, TextType
import os
import sys
import shutil
from page_generator import *

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

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
    # Step 4: Use docs instead of public
    dir_path_output = "./docs"
    
    # Clear and recreate output directory
    if os.path.exists(dir_path_output):
        shutil.rmtree(dir_path_output)
    os.makedirs(dir_path_output)
    
    # Copy static files
    copy_static("static", dir_path_output)
    
    # Generate pages
    print("Generating content...")
    generate_pages_recursive(basepath, dir_path_content, template_path, dir_path_output)

main()



