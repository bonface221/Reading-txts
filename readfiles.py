
text_file = 'text.txt'


def read_file(file):
    try:
        with open(file, 'r', encoding='utf_8') as handle:
            data = handle.read()
            return data

    except FileNotFoundError:
        return None
