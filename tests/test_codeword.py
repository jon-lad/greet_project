from lib.check_codeword import *

def test_check_codeword_returns_correct_for_horse():

    actual = check_codeword("horse")

    expected = "Correct! Come in."

    assert actual == expected

def test_check_codeword_returns_close_for_hope():

    actual = check_codeword("hope")

    expected = "Close, but nope."

    assert actual == expected

def test_check_codeword_returns_wrong_for_apple():

    actual = check_codeword("apple")

    expected = "WRONG!"

    assert actual == expected

