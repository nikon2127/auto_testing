from auto_testing.example import revers


def test_revers():
    assert revers('Hexlet') == 'telxeH'
    assert revers('Nikon') == 'nokiN'


def test_reverse_for_empty_string():
    assert revers('') == ''
