#31ms although similar as 9ms
def isValid(self, string: str) -> bool:
    approved = {
        '(':')',
        '{':'}',
        '[':']'
    }
    stack = []
    for ch in string:
        if ch in approved:
            stack.append(ch)
        elif ch in approved.values():
            if not stack:
                return False
            val = approved[stack.pop()]
            if val != ch:
                return False
    return not stack