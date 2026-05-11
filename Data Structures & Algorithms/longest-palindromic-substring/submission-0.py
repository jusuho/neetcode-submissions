class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        longest = 0
        ans = ""
        n = len(s)
        # dp[i][j] means s[i:j+1] is Palindorme or not
        # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        dp = [[False] * n for _ in range(n)]
            
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j - i <= 2: #a, aa, aba
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    if j - i + 1 > len(ans):
                        ans = s[i:j+1]
        return ans