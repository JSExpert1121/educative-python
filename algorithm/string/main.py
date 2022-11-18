def is_unique(input_str: str):
    result = {}
    for s in input_str:
        s = s.lower()
        if s.isspace():
            continue
        if s in result:
            return False
        result[s] = 1

    return True


def str_to_int(input_str: str):
    normalized = input_str.strip()
    is_negative = False
    if normalized[0] == '-':
        is_negative = True
        normalized = normalized[1:]
        normalized = normalized.strip()

    result = 0
    for ch in normalized:
        if ord(ch) < ord('0') or ord(ch) > ord('9'):
            return None

        result = result * 10 + ord(ch) - ord('0')

    return -result if is_negative else result


def run():
    print(is_unique('abcdef  sla'))


if __name__ == '__main__':
    run()
