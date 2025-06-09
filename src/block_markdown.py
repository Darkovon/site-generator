from enum import Enum
from htmlnode import *
from inline_markdown import *


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    headings = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    if block.startswith(headings[0]):
        return BlockType.HEADING
    elif block.startswith(headings[1]):
        return BlockType.HEADING
    elif block.startswith(headings[2]):
        return BlockType.HEADING
    elif block.startswith(headings[3]):
        return BlockType.HEADING
    elif block.startswith(headings[4]):
        return BlockType.HEADING
    elif block.startswith(headings[5]):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    count = 0
    for line in lines:
        if line.startswith(">"):
            count += 1
    if count == len(lines):
        return BlockType.QUOTE
    count = 0
    for line in lines:
        if line.startswith("- "):
            count += 1
    if count == len(lines):
        return BlockType.UNORDERED_LIST
    count = 0
    for i in range(len(lines)):
        if lines[i].startswith(f"{i+1}. "):
            count += 1
    if count == len(lines):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    no_empty_blocks = []
    for block in blocks:
        stripped = block.strip()
        if stripped != "":
            no_empty_blocks.append(stripped)
    return no_empty_blocks


def block_type_to_htmlnode_tag(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        lines = block.split("\n")
        if lines[0].startswith("######"):
            return "h6"
        elif lines[0].startswith("#####"):
            return "h5"
        elif lines[0].startswith("####"):
            return "h4"
        elif lines[0].startswith("###"):
            return "h3"
        elif lines[0].startswith("##"):
            return "h2"
        elif lines[0].startswith("#"):
            return "h1"
    elif block_type == BlockType.QUOTE:
        return "blockquote"
    elif block_type == BlockType.UNORDERED_LIST:
        return "ul"
    elif block_type == BlockType.ORDERED_LIST:
        return "ol"
    elif block_type == BlockType.CODE:
        return "pre"
    elif block_type == BlockType.PARAGRAPH:
        return "p"

def strip_headings(text):
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('#'):
            cleaned_line = stripped.lstrip('#').lstrip()
        else:
            cleaned_line = line
        cleaned_lines.append(cleaned_line)
    return "\n".join(cleaned_lines)

def strip_quotes(text):
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('>'):
            cleaned_line = stripped.lstrip('>').lstrip()
        else:
            cleaned_line = line
        cleaned_lines.append(cleaned_line)
    return "\n".join(cleaned_lines)

def unordered_list(text):
    lines = text.split("\n")
    cleaned_lines = []
    nodes = []
    for line in lines:
        cleaned_lines.append(line.strip("- "))
    for cleaned_line in cleaned_lines:
        nodes.append(ParentNode("li", text_to_children(cleaned_line)))
    return nodes

def ordered_list(text):
    lines = text.split("\n")
    cleaned_lines = []
    nodes = []
    for line in lines:
        cleaned_lines.append(line.split(". ")[1])
    for cleaned_line in cleaned_lines:
        nodes.append(ParentNode("li", text_to_children(cleaned_line)))
    return nodes

def text_to_children(text):
    children = []
    children.extend(text_to_textnodes(text))
    html_nodes = []
    for node in children:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        tag = block_type_to_htmlnode_tag(block)
        if tag == "pre":
            content = block[4:-3]
            code_node = ParentNode("code", [text_node_to_html_node(TextNode(content, TextType.TEXT))])
            html_nodes.append(ParentNode("pre", [code_node]))
        else:
            headings = ["h1", "h2", "h3", "h4", "h5", "h6"]
            if tag in headings:
                cleaned = strip_headings(block)
                html_nodes.append(ParentNode(tag, text_to_children(cleaned)))
            elif tag == "blockquote":
                cleaned = strip_quotes(block)
                html_nodes.append(ParentNode(tag, text_to_children(cleaned)))
            elif tag == "p":
                lines = block.split("\n")
                paragraph = " ".join(lines)
                html_nodes.append(ParentNode(tag, text_to_children(paragraph)))
            elif tag == "ul":
                html_nodes.append(ParentNode(tag, unordered_list(block)))
            elif tag == "ol":
                html_nodes.append(ParentNode(tag, ordered_list(block)))
    return ParentNode("div", html_nodes)
