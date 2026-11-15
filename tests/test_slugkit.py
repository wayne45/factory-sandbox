from slugkit import char_count, slugify, truncate_slug


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


def test_char_count_empty():
    assert char_count("") == 0


def test_char_count_excludes_hyphens():
    assert char_count("hello-world") == 10
    assert char_count("abc") == 3
    assert char_count("a1-b2") == 4


def test_char_count_slugify_output():
    assert char_count(slugify("Hello, World!")) == 10
    assert char_count(slugify("")) == 0
    assert char_count(slugify("!!!")) == 0


def test_char_count_truncate_output():
    assert char_count(truncate_slug("hello-world-foo", 11)) == 10
    assert char_count(truncate_slug("hello-world", 0)) == 0


def test_char_count_only_hyphens():
    assert char_count("---") == 0
    assert char_count("-a--b-") == 2


def test_char_count_returns_int():
    assert type(char_count("a-b")) is int
