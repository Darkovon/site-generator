from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode value cannot be None")
        if tag == "":
            raise ValueError("LeafNode tag cannot be empty")
        super().__init__(tag=tag, value=value, children=None, props=props)


# TODO: Step 2 of the boot.dev leafnode lesson. We need to figure out how to close the tags.

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode value cannot be None")
        if tag == None or tag == "":
            return self.value

# Create out opening and closing HTML tags   
        opening_tag = f"<{tag}>"
        closing_tag = f"</{tag}>"


        return f"{tag}{value}"
