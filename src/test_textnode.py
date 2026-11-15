import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("hello", TextType.BOLD)
        node2 = TextNode("hello", TextType.BOLD)
        node3 = TextNode("hello", TextType.ITALIC)
        node4 = TextNode("hello", TextType.ITALIC)
        node5 = TextNode("hello", TextType.CODE)
        node6 = TextNode("hello", TextType.CODE)
        node7 = TextNode("hello", TextType.LINK)
        node8 = TextNode("hello", TextType.LINK)
        node9 = TextNode("hello", TextType.IMAGE)
        node10 = TextNode("hello", TextType.IMAGE)
        self.assertEqual(node1, node2)
        self.assertEqual(node3, node4)
        self.assertEqual(node5, node6)
        self.assertEqual(node7, node8)
        self.assertEqual(node9, node10)


    def test_not_eq(self):
        node1 = TextNode("hello", TextType.BOLD)
        node2 = TextNode("hello", TextType.ITALIC)
        node3 = TextNode("hello", TextType.CODE)
        node4 = TextNode("hello", TextType.LINK)
        node5 = TextNode("hello", TextType.IMAGE)
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node4)
        self.assertNotEqual(node1, node5)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node2, node4)
        self.assertNotEqual(node2, node5)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node3, node5)
        self.assertNotEqual(node4, node5)



    def test_eq_url(self):
        node1 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node1, node2)


    def test_repr(self):
        node1 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
                "TextNode(This is a text node, text, https://www.boot.dev)", repr(node1)
            )



    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
        unittest.main()
