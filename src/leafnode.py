

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode value cannot be None")
        if tag == "":
            raise ValueError("LeafNode tag cannot be empty")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode value cannot be None")
        if self.tag == None:
            return self.value

# Create our opening and closing HTML tags
        opening_tag = f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"

# Handle props
        if self.props != None:
            prop_list = self.props.keys()
            open_prop_string = f"<{self.tag} "
            open_prop_string += " ".join([f'{key}="{self.props[key]}"' for key in prop_list])
            open_prop_string += ">"
            open_prop_string += f"{self.value}{closing_tag}"
            return open_prop_string
        return f"{opening_tag}{self.value}{closing_tag}"


node = LeafNode("div", "Hello", {"id": "greeting", "class": "salutation"})
print(node.to_html())
