from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    delimited_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            delimited_nodes.append(node)
            continue
        sections = node.text.split(delimiter)
        split_sections = []
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown: Delimiter must close")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_sections.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_sections.append(TextNode(sections[i], text_type))
        delimited_nodes.extend(split_sections)
    return delimited_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    split_nodes = []
    for node in old_nodes:
        image_tuple_list = extract_markdown_images(node.text)
        original_text = node.text
        if len(image_tuple_list) == 0:
            split_nodes.append(node)
            continue
        image_alt, image_link = image_tuple_list[0]
        sections = original_text.split(f"![{image_alt}]({image_link})", 1)
        if sections[0] != "":
            split_nodes.append(TextNode(sections[0], TextType.TEXT))
        split_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
        if sections[1] != "":
            split_nodes.extend(split_nodes_image([TextNode(sections[1], TextType.TEXT)]))
    return split_nodes

def split_nodes_link(old_nodes):
    split_nodes = []
    for node in old_nodes:
        link_tuple_list = extract_markdown_links(node.text)
        original_text = node.text
        if len(link_tuple_list) == 0:
            split_nodes.append(node)
            continue
        link_text, link_url = link_tuple_list[0]
        sections = original_text.split(f"[{link_text}]({link_url})", 1)
        if sections[0] != "":
            split_nodes.append(TextNode(sections[0], TextType.TEXT))
        split_nodes.append(TextNode(link_text, TextType.LINK, link_url))
        if sections[1] != "":
            split_nodes.extend(split_nodes_link([TextNode(sections[1], TextType.TEXT)]))
    return split_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    delimiters = ["_", "`", "**"]
    current_nodes = [node]
    for delimiter in delimiters:
        if delimiter == "_":
            text_type = TextType.ITALIC
        elif delimiter == "`":
            text_type = TextType.CODE
        elif delimiter == "**":
            text_type = TextType.BOLD
        result = split_nodes_delimiter(current_nodes, delimiter, text_type)
        current_nodes = result
    image_split = split_nodes_image(current_nodes)
    link_split = split_nodes_link(image_split)
    return link_split
