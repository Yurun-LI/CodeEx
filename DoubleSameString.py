# 在给定字符串中找出最长连续同一个字符的子字符串

class Solution:
    def doubleSameString(self,str:str)->str:
        max_length = 0
        max_sub_str = None
        for i in range(len(str)):
            sub_len, sub_same_str = self.ContinueSameSubString(i,str)
            if sub_len > max_length:
                max_length = sub_len
                max_sub_str = sub_same_str
        return max_sub_str
    
    def ContinueSameSubString(self,cur_pos:int,str:str):
        """
        return [length,MaxSubstr
        """
        left,right = cur_pos,cur_pos
        while left >=0 and str[left] == str[cur_pos]:
            left-=1
        while right < len(str) and str[right] == str[cur_pos]:
            right+=1
        max_sub_str = str[left+1:right]
        return len(max_sub_str), max_sub_str

#test
test_str = 'aabssssfasfsaaasg'
print(Solution().doubleSameString(test_str))