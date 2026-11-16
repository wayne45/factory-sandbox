from slugkit import (
    char_count,
    count_vowels,
    ends_with_digit,
    first_word,
    has_whitespace,
    is_all_digits,
    shout,
    slugify,
    starts_with_digit,
    truncate_slug,
    word_count,
)


def test_shout_basic():
    assert shout("hello-world") == "HELLO-WORLD"


def test_shout_empty():
    assert shout("") == ""


def test_shout_mixed():
    assert shout("a-1-B") == "A-1-B"


def test_shout_with_slugify():
    assert shout(slugify("Hello World")) == "HELLO-WORLD"


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


def test_starts_with_digit_true():
    assert starts_with_digit("123-abc") is True
    assert starts_with_digit("9") is True


def test_starts_with_digit_false():
    assert starts_with_digit("abc-123") is False


def test_starts_with_digit_empty():
    assert starts_with_digit("") is False


def test_starts_with_digit_leading_hyphen_or_space():
    assert starts_with_digit("-1") is False
    assert starts_with_digit(" 1") is False


def test_starts_with_digit_all_ascii_digits():
    for d in "0123456789":
        assert starts_with_digit(d + "abc") is True


def test_starts_with_digit_non_ascii_digit():
    assert starts_with_digit("²abc") is False
    assert starts_with_digit("٣abc") is False


def test_starts_with_digit_with_helpers():
    assert starts_with_digit(slugify("2024 Report")) is True
    assert starts_with_digit(slugify("Report 2024")) is False
    assert starts_with_digit(truncate_slug("1-two-three", 3)) is True


def test_ends_with_digit_true():
    assert ends_with_digit("abc-123") is True
    assert ends_with_digit("9") is True


def test_ends_with_digit_false():
    assert ends_with_digit("123-abc") is False


def test_ends_with_digit_empty():
    assert ends_with_digit("") is False


def test_ends_with_digit_trailing_hyphen_or_space():
    assert ends_with_digit("1-") is False
    assert ends_with_digit("1 ") is False
    assert ends_with_digit("1\n") is False


def test_ends_with_digit_all_ascii_digits():
    for d in "0123456789":
        assert ends_with_digit("abc" + d) is True


def test_ends_with_digit_non_ascii_digit():
    assert ends_with_digit("abc²") is False
    assert ends_with_digit("abc٣") is False


def test_ends_with_digit_with_helpers():
    assert ends_with_digit(slugify("Report 2024")) is True


def test_is_all_digits_true():
    assert is_all_digits("123") is True
    assert is_all_digits("0") is True


def test_is_all_digits_empty():
    assert is_all_digits("") is False


def test_is_all_digits_non_digit():
    for s in ["12a", "a12", "1-2", "1 2", " 1", "1\n", "abc"]:
        assert is_all_digits(s) is False


def test_is_all_digits_non_ascii():
    for s in ["²", "٣", "12٣"]:
        assert is_all_digits(s) is False


def test_is_all_digits_each_digit():
    for d in "0123456789":
        assert is_all_digits(d) is True
    assert is_all_digits("0123456789") is True


def test_is_all_digits_with_helpers():
    assert is_all_digits(slugify("2024")) is True
    assert is_all_digits(slugify("Report 2024")) is False


def test_has_whitespace_true():
    for s in ["a b", "a\tb", "a\n", "a\rb", "a\x0bb", "a\x0cb", " ", " a", "a "]:
        assert has_whitespace(s) is True


def test_has_whitespace_false():
    for s in ["abc", "a-b_c", "123"]:
        assert has_whitespace(s) is False


def test_has_whitespace_empty():
    assert has_whitespace("") is False


def test_has_whitespace_unicode():
    for s in ["\u00a0", "a\u3000b"]:
        assert has_whitespace(s) is True


def test_count_vowels_basic_and_case():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("AbEcIdOfU") == 5


def test_count_vowels_repeated():
    assert count_vowels("banana") == 3
    assert count_vowels("aaa") == 3


def test_count_vowels_none():
    for s in ("rhythm", "xyz", "bcd"):
        assert count_vowels(s) == 0


def test_count_vowels_empty():
    assert count_vowels("") == 0


def test_count_vowels_ignores_non_letters():
    assert count_vowels("a1 e-i_o!u") == 5


def test_count_vowels_non_ascii_and_y():
    assert count_vowels("éüyY") == 0


def test_count_vowels_returns_int():
    assert type(count_vowels("hello")) is int
    assert type(count_vowels("")) is int


def test_first_word_basic():
    assert first_word("hello world") == "hello"
    assert first_word("hello") == "hello"


def test_first_word_leading_whitespace():
    assert first_word("  hello world") == "hello"


def test_first_word_empty_and_whitespace_only():
    for s in ["", " ", "   ", "\t\n"]:
        assert first_word(s) == ""


def test_first_word_any_whitespace():
    for s in ["a\tb", "a\nb", "a\u00a0b", "a\u3000b"]:
        assert first_word(s) == "a"


def test_first_word_preserves_case_punctuation():
    assert first_word("Hello, World") == "Hello,"


def test_first_word_returns_str():
    for s in ["word", "", "   "]:
        assert type(first_word(s)) is str
