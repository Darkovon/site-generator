from enum import Enum


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
        if lines[i].startswith(f"{i+1}."):
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
