from htmlnode import *
import unittest

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        print("Starting test_eq")
        node = HTMLNode("p", "This is the text inside p", None, None)
        node2 = HTMLNode("p", "This is the text inside p", None, None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("p", "This is the text inside p", None, None)
        node2 = HTMLNode("a", "This is the text inside a", None, None)
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        print("Starting test_props_to_html")
        node = HTMLNode("a", "This is a node", None, {"href": "https://www.google.com", "target": "_blank",})
 #       print(node.props_to_html())
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_print(self):
        print("Starting test_print")
        node = HTMLNode("a", "This is a node", None, {"href": "https://www.google.com", "target": "_blank",})
        self.__repr__()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
