import os
import shutil
from htmlnode import *
from block_markdown import *

dst = "public/"
src = "static/"


def file_copy(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
        os.mkdir(destination)
    else:
        print(f"{destination} not found. Creating now.")
        os.mkdir(destination)
    if os.path.exists(source): # If the source path exists
        print("Path exists", source) # print it
        print("Source contents", os.listdir(source)) # print it's files
        files = os.listdir(source) # make a list of all of the files in it
        for file in files: # go through each file
            if not os.path.exists(source + file + "/"): # If not a directory
                print("Copying", file) # copy it
                shutil.copy(source + file, destination)
            else:
                print(f"Directory found. Recursing into {file}/")
                print(f"New source is {file}/")
                print("New Destination is", destination + file + "/")
                file_copy(source + file + "/", destination + file + "/")

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("H1 not found")

def generate_path(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open("content/index.md", "r") as content:
        read_content = content.read()
    with open(template_path, "r") as template:
        read_template = template.read()
    node = markdown_to_html_node(read_content)
    html = node.to_html()
    title = extract_title(read_content)
    title_update = read_template.replace("{{ Title }}", title)
    completed_updates = title_update.replace("{{ Content }}", html)
    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as new_html:
        new_html.write(completed_updates)
