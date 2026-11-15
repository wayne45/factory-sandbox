from slugkit import char_count, is_slug, slugify, truncate_slug, word_count


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


def test_word_count_basic():
    assert word_count("") == 0
    assert word_count("hello") == 1
    assert word_count("a-b-c-d") == 4


def test_word_count_slugify_output():
    assert word_count(slugify("Hello, World!")) == 2
    assert word_count(slugify("")) == 0
    assert word_count(slugify("!!!")) == 0


def test_word_count_truncate_slug_output():
    assert word_count(truncate_slug("hello-big-world", 12)) == 2
    assert word_count(truncate_slug("hello-big-world", 9)) == 2
    assert word_count(truncate_slug("supercalifragilistic", 5)) == 1
    assert word_count(truncate_slug("hello-world", 0)) == 0


def test_word_count_composition():
    for n, expected in [(0, 0), (12, 2), (100, 3)]:
        assert word_count(truncate_slug(slugify("Hello Big World"), n)) == expected


def test_word_count_with_char_count():
    slug = slugify("Hello Big World")
    assert char_count(slug) + word_count(slug) - 1 == len(slug)


def test_word_count_malformed():
    assert word_count("-") == 0
    assert word_count("a--b") == 2
    assert word_count("-a-") == 1


def test_is_slug_valid():
    for s in ["hello-world", "hello", "a1-b2-c3", "123"]:
        assert is_slug(s) is True


def test_is_slug_empty():
    assert is_slug("") is False


def test_is_slug_hyphen_misuse():
    for s in ["-a", "a-", "a--b", "-", "--"]:
        assert is_slug(s) is False


def test_is_slug_uppercase():
    assert is_slug("Hello-world") is False


def test_is_slug_bad_chars():
    for s in ["a b", "a_b", "a.b", "café", "日本", "٣", "abc\n"]:
        assert is_slug(s) is False


def test_is_slug_accepts_slugify_output():
    for s in ["Hello, World!", "  A  b--C ", "x1 y2"]:
        assert is_slug(slugify(s)) is True
    assert is_slug(truncate_slug(slugify("Hello big world"), 9)) is True


def test_is_slug_non_string():
    for v in [None, 123, b"abc", ["a"]]:
        assert is_slug(v) is False


def test_is_slug_returns_bool():
    assert type(is_slug("a")) is bool
