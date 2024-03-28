class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(s:str) -> str:
            stack = []
            print(s)
            for ch in s:
                if ch=='#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
                print(stack)
            return ''.join(ch for ch in stack)
        return process(s) == process(t)