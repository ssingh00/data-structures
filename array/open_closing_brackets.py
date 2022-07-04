class OpenClosingBracket:

    OPEN_CLOSE_MAP = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    def isValid(self, s: str) -> bool:
        closing_braces_stack = []

        for char in s:
            if char in OpenClosingBracket.OPEN_CLOSE_MAP:
                closing_braces_stack.append(OpenClosingBracket.OPEN_CLOSE_MAP[char])
            else:
                if not closing_braces_stack or char != closing_braces_stack.pop():
                    return False

        return len(closing_braces_stack) == 0

if __name__=="__main__":
    s = "{[]}"
    ocb = OpenClosingBracket()
    print(ocb.isValid(s))