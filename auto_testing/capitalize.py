#!usr/bin/etv python3
def capitalize(text):
    if not text:
        return ''
    return f'{text[0].upper()}{text[1:]}'


def main():
    capitalize('hello')


if __name__ == '__main__':
    main()
