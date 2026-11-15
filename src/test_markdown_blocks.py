import unittest

from markdown_blocks import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
)


# Boot.dev wrote these tests, not me. #
class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )



        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )





# I wrote these tests T.T #
class TestBlockToBlockType(unittest.TestCase):
    def test_eq_block_types(self):
        paragraph_block = "This is a paragraph block"
        paragraph_result = block_to_block_type(paragraph_block)
        heading_block = "# This is a heading block"
        heading_result = block_to_block_type(heading_block)
        code_block = """```
        This is code block```"""
        code_result = block_to_block_type(code_block)
        quote_block = "> This is a quote block"
        quote_result = block_to_block_type(quote_block)
        unorderded_block = "- This is an unordered list"
        unordered_result = block_to_block_type(unorderded_block)
        ordered_block = "1. This is an ordered list"
        ordered_result = block_to_block_type(ordered_block)
        self.assertEqual([
            paragraph_result,
            heading_result,
            code_result,
            quote_result,
            unordered_result,
            ordered_result],
        [BlockType.paragraph,
        BlockType.heading,
        BlockType.code,
        BlockType.quote,
        BlockType.unordered_list,
        BlockType.ordered_list,])


    def test_uneq_heading(self):
        not_heading_block = "####### This is not a heading block"
        not_heading_result = block_to_block_type(not_heading_block)
        self.assertEqual(not_heading_result,BlockType.paragraph)


    def test_uneq_quote(self):
        not_quote_block = "> Valid quote block\n Not valid quote block"
        not_quote_result = block_to_block_type(not_quote_block)
        self.assertEqual(not_quote_result,BlockType.paragraph)


    def test_uneq_unordered_list(self):
        not_unordered_list_block = "1. "
        not_unordered_list_result = block_to_block_type(not_unordered_list_block)
        self.assertEqual(not_unordered_list_result,BlockType.ordered_list)


    def test_uneq_ordered_list(self):
        not_ordered_list_block = "2. "
        not_ordered_list_result = block_to_block_type(not_ordered_list_block)
        self.assertEqual(not_ordered_list_result,BlockType.paragraph)



if __name__ == "__main__":
    unittest.main()
