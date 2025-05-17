from htmlnode import HTMLNode
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
