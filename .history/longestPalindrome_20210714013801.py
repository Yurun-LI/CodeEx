
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if s == '':
#             return None
#         self.longestStr = s[0]
#         def longestSubStr(str:str):
#             if len(str) > 1:
#                 #如果当前字符串为回文字符串,则将其长度与储存最长的字符串长度对比,并返回空
#                 if self.palindrome(str) == True:
#                     if len(self.longestStr) < len(str):
#                         self.longestStr = str
#                 #当前字符串不为回文,则考虑左子串和右子串是否为回文
#                 longestSubStr(str[:-1])
#                 longestSubStr(str[1:])
#         longestSubStr(s)
#         return self.longestStr

#     def palindrome(self,s:str): #判断是否为回文数
#         l,r = 0,len(s)-1
#         while l<r:
#             if s[l] !=s[r]:
#                 return False
#             l+=1
#             r-=1
#         return True

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return None
        longestStr=s[0]
        for i in range(len(s)):
            left,right = self.longest_from_a_char(s,i,i)
            longestStr = s[left:right+1] if (right+1-left > len(longestStr)) else longestStr
            i = right
        return longestStr

    def longest_from_a_char(self,s:str,left,right): #从当前字符向两边衍生的最大回文字符串
        if (left>=0 and right<len(s)):
            if right+1 <len(s) and left-1 >=0 and s[right+1] == s[left-1]:
                return self.longest_from_a_char(s,left-1,right+1)
            elif left -1 >=0 and s[left-1] == s[right] and (right == left):
                return self.longest_from_a_char(s,left-1,right)
            elif right+1 <len(s) and s[right+1] == s[left] and (right == left):
                return self.longest_from_a_char(s,left,right+1)
            else:
                return left,right


        
test_str= "aacabdkacaa"
print(Solution().longestPalindrome(test_str))