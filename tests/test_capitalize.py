from auto_testing.capitalize import capitalize


def test_capitalize():
    assert capitalize('hello') == 'Hello'
    assert capitalize('') == ''
    assert capitalize(' hexlet') == ' hexlet'
