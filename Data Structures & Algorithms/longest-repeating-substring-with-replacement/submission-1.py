class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_length = 0
        current_length = 1
        max_freq = 0
        pre_char = s[0]
        left = 0
        seen = {}
        # XYYX k =2
        # XY c_k =1 c_l=2
        # XYY c_k=2 c_l=3
        # 
        # len(window) - max_f <= k
        for i in range(len(s)):
            char = s[i]
            seen[char] = seen.get(char,0) + 1

            max_freq = max(max_freq, seen[char])

            while (i - left + 1) - max_freq > k:
                seen[s[left]] -= 1
                left += 1
            
            # 4. 走到這裡，代表窗戶一定是合法的，更新最大長度
            max_length = max(max_length, i - left + 1)

        return max_length

