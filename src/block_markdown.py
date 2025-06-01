
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n").strip()
    no_empty_blocks = blocks
    for block in blocks:
        if block != "":
            no_empty_blocks.append(block)
