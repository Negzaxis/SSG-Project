from textnode import TextNode, TextType
import os
import shutil

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




main()


