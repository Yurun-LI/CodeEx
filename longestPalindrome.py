class Solution:
    def longestPalindrome(self,s:str)->str:
        #动态规划解法 O(N2) O(N2)
        if len(s)<2:
            return s
        max_len = 1
        begin = 0

        dp = [[False if i!=j else True for j in range(len(s))] for i in range(len(s))]
        
        #递推开始
        for L in range(2,n+1):
            for i in range(n):
                j = L + i -1 
                if j>= n:
                    break
                if s[j] != s[i]:
                    dp[i][j] = False
                else:
                    if j - i <3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    begin = i
        return s[begin:begin+max_len]