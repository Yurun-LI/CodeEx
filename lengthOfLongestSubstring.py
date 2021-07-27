# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) == 0 or len(s) == 1:
#             return len(s)
#         max_diff_len = 0
#         for i in range(len(s)):
#             sub_len = self.judgeDiffSubstr(curr_pos=i,s=s) #子串为s[l:r],l包含,r不包含
#             max_diff_len = max(max_diff_len,sub_len)
#         return max_diff_len
#     def judgeDiffSubstr(self,curr_pos:int,s:str):
#         l,r = curr_pos-1,curr_pos+1
#         ls = [s[curr_pos]]
#         while (l>=0) and (s[l] not in ls):
#             ls.append(s[l])
#             l-=1
#         while (r<len(s)) and (s[r] not in ls):
#             ls.append(s[r])
#             r+=1
#         return r - (l+1)


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L= 0
        last_diff_pos = -1 #没出现过
        save = {} #储存各个符号上次出现位置
        for curr_pos in range(len(s)):
            if s[curr_pos] in save:#如果当前符号曾经出现过,更新为max(当前符号上一次出现的位置,其他符号不会重复时i的位置)
                last_diff_pos = max(last_diff_pos,save[s[curr_pos]])
            L = max(L,curr_pos-last_diff_pos) #当前符号的最大不重复子串长度
            save[s[curr_pos]] = curr_pos #更新当前符号出现的位置(历史上最后一次出现位置)
        return L  
#test
test_str= 'abba'
print(Solution().lengthOfLongestSubstring(test_str))