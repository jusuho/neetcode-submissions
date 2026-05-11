class Solution:
    def countSubstrings(self, s: str) -> int:
        # DP
        n = len(s)
        # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        dp = [[False]* n for _ in range(n)]
        cnt = 0 # ans

        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    cnt+=1
        return cnt
