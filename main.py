def parser(string: str) -> str:
    open_char_list = []
    for i in range(0, len(string)):
        if string[i] == '(':
            open_char_list.append(i)
            continue
        if string[i] == ')' and len(open_char_list):
            return parser(string[0:open_char_list[-1]] + string[i + 1:len(string)])
    return ' '.join(string.split())
