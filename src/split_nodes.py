from enum import Enum
from typing import List
from textnode import *

def split_nodes_delimiter(old_nodes: List, delimiter: str, text_type: TextType) -> List[TextNode]:
    node_list = []
    for node in old_nodes:
        if text_type != TextType.TEXT:
            node_list.append(node)

 #       if delimiter == '**':

    return node_list


test_nodes = ["This is text with a **bolded phrase** in the middle"]

print(split_nodes_delimiter(test_nodes, "**", TextType.TEXT))

result = test_nodes[0].index("**")
print(result)
