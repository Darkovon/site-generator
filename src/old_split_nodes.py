from enum import Enum
from typing import List
from textnode import *

# 1. Take in a node. If it is not a texttype.text, add it to the node list.
# 2. other wise, If no delimiter is found, add it to node_list as a TextType.TEXT- WORKS
# 3. If the delimier is there, search through the text for the first occurance delimiter.
# 3. When the delimiter is found, search through the text for the closing delimiter.
#   a. If a closing delimiter is not found, raise an error message that it is invalid Markdown
# 4. Add the text before and not including the first delimiter to the list of nodes as a TextType.TEXT node
# 5. Add the text inside and not including the delimiter pair to the list of nodes as a TextType that matches the delimiter
# 6. If there is any text after the closing delimiter, repeat steps 1-4 until there are no delimiters left



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        delimited_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid Markdown. No Matching Delimiter")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                delimited_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                delimited_nodes.append(TextNode(sections[i], text_type))
        node_list.extend(delimited_nodes)
    return node_list



test_nodes = [TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT, None)]
no_delimiter = [TextNode("This is text with no delimiter", TextType.TEXT, None)]
not_text_type = [TextNode("This is not a TextType.TEXT node", TextType.BOLD, None)]

split_nodes_delimiter(test_nodes, "**", TextType.TEXT)
# print(split_nodes_delimiter(no_delimiter, "**", TextType.BOLD))
# print(split_nodes_delimiter(not_text_type, "**", TextType.BOLD))


# result = test_nodes[0].index("**")
# print(result)
