from typing import List
class Solution:
    def maximumSubArray(self,nums:List[int])-> int:
        pre = 0
        max_ans = nums[0]
        for i in range(0,len(nums)):
            pre = max(pre+nums[i],nums[i])
            max_ans = max(max_ans, pre)
        return max_ans
        
nums = [-1,-2,1]
print(Solution().maximumSubArray(nums))