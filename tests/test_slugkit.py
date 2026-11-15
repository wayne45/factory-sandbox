from slugkit import is_slug, slugify


def test_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_empty():
    assert slugify("") == ""


def test_is_slug_valid():
    assert is_slug("hello-world-2")
    assert is_slug("abc")


def test_is_slug_empty():
    assert not is_slug("")


def test_is_slug_uppercase():
    assert not is_slug("Hello")


def test_is_slug_double_hyphen():
    assert not is_slug("a--b")


def test_is_slug_edge_hyphens():
    assert not is_slug("-a")
    assert not is_slug("a-")
    assert not is_slug("-")


def test_is_slug_trailing_newline_and_non_ascii():
    assert not is_slug("a\n")
    assert not is_slug("é")
