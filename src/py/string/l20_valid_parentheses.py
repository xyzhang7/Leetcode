def isValid(s: str) -> bool:
    def match(start: chr, end: chr) -> bool:
        if (start == '(' and end == ')') or \
                (start == '{' and end == '}') or \
                (start == '[' and end == ']'):
            return True
        else:
            return False

    stack = list()
    for c in s:
        if match(stack[-1], c):
            stack.pop()
        else:
            stack.append(c)
    return False if stack else True

if __name__ == "__main__":
    isValid("()")