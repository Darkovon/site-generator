from textnode import *


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
            if i % 2 == 0:
                split_sections.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_sections.append(TextNode(sections[i], text_type))
        delimited_nodes.extend(split_sections)
    return delimited_nodes



node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
print(new_nodes)
