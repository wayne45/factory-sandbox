from slugkit import slugify


def test_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_empty():
    assert slugify("") == ""


def test_no_limit():
    assert slugify("Hello, World!", max_length=None) == "hello-world"
    assert slugify("Hello, World!", max_length=100) == "hello-world"


def test_limit_mid_word():
    assert slugify("Hello, World!", max_length=8) == "hello-wo"


def test_limit_on_hyphen():
    assert slugify("Hello, World!", max_length=6) == "hello"


def test_limit_zero():
    assert slugify("Hello, World!", max_length=0) == ""
