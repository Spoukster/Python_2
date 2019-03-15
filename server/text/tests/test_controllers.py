from server.text.controllers import (
    get_lower_text, get_upper_text, get_title_text
)

TEST_TEXT_1 = 'SOME TEXT'
ASSERT_TEXT_1 = 'some text'


def test_get_lower_text_is_lower():
    assert get_lower_text(TEST_TEXT_1) == ASSERT_TEXT_1


TEST_TEXT_2 = 'some text'
ASSERT_TEXT_2 = 'SOME TEXT'


def test_get_upper_text_is_upper():
    assert get_upper_text(TEST_TEXT_2) == ASSERT_TEXT_2


TEST_TEXT_3 = 'some text'
ASSERT_TEXT_3 = 'Some Text'


def test_get_title_text_is_title():
    assert get_title_text(TEST_TEXT_3) == ASSERT_TEXT_3
