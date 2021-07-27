from typing import List
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        dic = {}
        Len = len(nums)
        for i in range(Len):
            if nums[i] in dic:
                  return [dic[nums[i]],i]
            dic[target - nums[i]] = i
        return None

nums = [1,2,3,6,7]
target = 5

print(Solution().twoSum(nums, target))