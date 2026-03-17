import unittest
from build import extract_title


class TestExtractTitle(unittest.TestCase):
  def test_with_basic_markdown(self) -> None:
    markdown = """
# Properly Titled Markdown

Additional text after
"""
    expected = "Properly Titled Markdown"
    actual = extract_title(markdown)
    self.assertEqual(expected, actual)

  def test_with_no_following_text(self) -> None:
    markdown = """
# Properly Titled Markdown
"""
    expected = "Properly Titled Markdown"
    actual = extract_title(markdown)
    self.assertEqual(expected, actual)

  def test_with_preceding_text(self) -> None:
    markdown = """
Additional text before

# Properly Titled Markdown

Additional text after
"""
    expected = "Properly Titled Markdown"
    actual = extract_title(markdown)
    self.assertEqual(expected, actual)

  def test_with_preceding_and_no_following(self) -> None:
    markdown = """
Additional text before

# Properly Titled Markdown
"""
    expected = "Properly Titled Markdown"
    actual = extract_title(markdown)
    self.assertEqual(expected, actual)

  def test_raises_with_no_h1(self) -> None:
    markdown = """
Improperly titled markdown
"""
    with self.assertRaises(Exception):
      extract_title(markdown)


if __name__ == "main":
  unittest.main()
