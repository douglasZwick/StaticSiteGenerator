import unittest
from urlextraction import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownImages(unittest.TestCase):
  def test_with_1(self) -> None:
    text = "Text, with... ![lmnop](https://img.z.com/image.png) ...an image!"
    expected = [
      ("lmnop", "https://img.z.com/image.png"),
    ]
    actual = extract_markdown_images(text)
    self.assertListEqual(expected, actual)

  def test_with_2(self) -> None:
    text = "Img A: ![qrs](https://img.z.com/a.png), Img B: ![tuv](https://img.z.com/b.png), coda"
    expected = [
      ("qrs", "https://img.z.com/a.png"),
      ("tuv", "https://img.z.com/b.png"),
    ]
    actual = extract_markdown_images(text)
    self.assertListEqual(expected, actual)

  def test_with_no_alt(self) -> None:
    text = "Text, with... ![](https://img.z.com/image.png) ...an image!"
    expected = [
      ("", "https://img.z.com/image.png"),
    ]
    actual = extract_markdown_images(text)
    self.assertListEqual(expected, actual)

  def test_with_no_url(self) -> None:
    text = "Text, with... ![abcde]() ...no image!"
    expected = [
      ("abcde", ""),
    ]
    actual = extract_markdown_images(text)
    self.assertListEqual(expected, actual)

  def test_with_nothing(self) -> None:
    text = "Text, with... ![]() ...bupkis!"
    expected = [
      ("", ""),
    ]
    actual = extract_markdown_images(text)
    self.assertListEqual(expected, actual)


class TestExtractMarkdownLinks(unittest.TestCase):
  def test_with_1(self) -> None:
    text = "A link to [the past]" \
    "(https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_A_Link_to_the_Past)"
    expected = [
      ("the past", "https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_A_Link_to_the_Past"),
    ]
    actual = extract_markdown_links(text)
    self.assertListEqual(expected, actual)

  def test_with_2(self) -> None:
    text = "Article on [the first letter](https://en.wikipedia.org/wiki/A), " \
    "article on [the second letter](https://en.wikipedia.org/wiki/B)"
    expected = [
      ("the first letter", "https://en.wikipedia.org/wiki/A"),
      ("the second letter", "https://en.wikipedia.org/wiki/B"),
    ]
    actual = extract_markdown_links(text)
    self.assertListEqual(expected, actual)

  def test_with_no_anchor(self) -> None:
    text = "A link with no anchor [](https://en.wikipedia.org/wiki/Link_rot)"
    expected = [
      ("", "https://en.wikipedia.org/wiki/Link_rot"),
    ]
    actual = extract_markdown_links(text)
    self.assertListEqual(expected, actual)

  def test_with_no_url(self) -> None:
    text = "A link with [no url??]()"
    expected = [
      ("no url??", ""),
    ]
    actual = extract_markdown_links(text)
    self.assertListEqual(expected, actual)

  def test_with_nothing(self) -> None:
    text = "What kind of silly link is this??? []() ???"
    expected = [
      ("", ""),
    ]
    actual = extract_markdown_links(text)
    self.assertListEqual(expected, actual)


if __name__ == "main":
  unittest.main()
