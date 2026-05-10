class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Key 存右括號，Value 存對應的左括號
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            # 如果是右括號
            if char in bracket_map:
                # 1. 檢查 Stack 是否為空（預防第一個就是右括號）
                # 2. 檢查彈出的元素是否匹配
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # 如果是左括號，直接推進 Stack
                stack.append(char)
        
        # 最後檢查 Stack 是否清空
        return not stack