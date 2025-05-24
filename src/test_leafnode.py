from htmlnode import *
import unittest

print("Starting test_leafnode.py")

def test_leafnode(node):
    node = LeafNode("p", "This is a paragraph of text")
    node2 = LeafNode("p", "This is a paragraph of text")
    self.assertEqual(node, node2)

def test_to_html(node):
    node = LeafNode("p", "This is a paragraph of text")
    node2 = LeafNode("a", "CLick me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), "<p>This is a paragraph of text</p>")
    self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">CLick me!</a>")

def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_leaf_to_html_a(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(
        node.to_html(),
        '<a href="https://www.google.com">Click me!</a>',
        )

def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Hello, world!")
    self.assertEqual(node.to_html(), "Hello, world!")
