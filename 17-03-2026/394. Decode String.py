class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''
        for val in s:
            if not val ==']':
                stack.append(val)
            else:
                alp = ''
                num = ''
                while stack[-1] != '[':
                    alp = stack.pop() + alp
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*alp)
        return ''.join(stack)