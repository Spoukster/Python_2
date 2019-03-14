from server.text.controllers import (
    get_lower_text, get_upper_text
)

TEST_TEXT = 'SOME TEXT'
ASSERT_TEXT = 'some text'


def test_get_lower_text_is_lower():
    assert get_lower_text(TEST_TEXT) == ASSERT_TEXT
