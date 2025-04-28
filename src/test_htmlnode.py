# Tests for  HTMLNode
import unittest
from htmlnode import HTMLNode

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

        