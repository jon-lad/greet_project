from lib.greet import *

def test_greet_function_returns_hello_jonnie_for_jonnie():

    actual = greet('Jonnie')

    expected = "Hello, Jonnie!"

    assert actual == expected
