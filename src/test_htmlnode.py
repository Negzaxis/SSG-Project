# Tests for  HTMLNode
import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode(props={"class": "big", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="big" id="main"')

    def test_eq_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_eq_single_attribute(self):
        node = HTMLNode(props={"class": "big"})
        self.assertEqual(node.props_to_html(), ' class="big"')

    def test_eq_empty_dictionary(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), '')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.example.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.example.com">Click me!</a>')

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("input", "Text", {"type": "text", "name": "username", "placeholder": "Enter username"})
        self.assertEqual(node.to_html(), '<input type="text" name="username" placeholder="Enter username">Text</input>')

    def test_leaf_to_html_no_props(self):
        node = LeafNode("span", "Some text")
        self.assertEqual(node.to_html(), "<span>Some text</span>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

if __name__ == "__main__":
    unittest.main()