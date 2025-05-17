

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        href = self.props["href"]
        target = self.props["target"]
        return f' href="{href}" target="{target}"'

    def __repr__(self):
        print(f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}")
