from slugkit import slugify, truncate_slug


def test_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_empty():
    assert slugify("") == ""


def test_truncate_shorter_than_limit():
    assert truncate_slug("hello-world", 20) == "hello-world"
    assert truncate_slug("hello-world", 11) == "hello-world"


def test_truncate_on_boundary():
    assert truncate_slug("hello-big-world", 12) == "hello-big"  # mid-word cut backs up
    assert truncate_slug("hello-big-world", 9) == "hello-big"  # exact boundary
    assert truncate_slug("hello-big-world", 10) == "hello-big"  # would end with hyphen


def test_truncate_single_long_word():
    assert truncate_slug("supercalifragilistic", 5) == "super"


def test_truncate_limit_zero():
    assert truncate_slug("hello-world", 0) == ""
    assert truncate_slug("hello-world", -3) == ""
