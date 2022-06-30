from auto_testing.capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('function not work')

if capitalize('') != '':
    raise Exception('function not work not args')

def test_capitalize():
    assert capitalize('hello') == 'Hello'
    assert capitalize('') == ''

print('capitalize work')
