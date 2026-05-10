class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        put = ['[','{','(']
        map = {
            ']':'[',
            ')': '(',
            '}': '{'
        }
        for ss in s:
            if ss in put:
                ans.append(ss)
                continue
            left = map.get(ss, None)
            if left is None or len(ans) == 0:
                return False
            if ans.pop() != left:
                return False
        return len(ans) == 0