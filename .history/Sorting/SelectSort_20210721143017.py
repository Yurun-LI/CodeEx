from typing import List
from numpy.random import permutation
'''
选择排序 (Selection)
平均复杂度: O(n2)
最坏复杂度: O(n2)
最好复杂度: O(n2)

空间复杂度: 1
稳定性: 不稳定

思路: 
for i in [0,len-1):
    记录当前 i 所在位置的值 List[i]
    搜索序列空间[i,len),逐个与List[i]进行对比,找出最小值,并与List[i]交换,并重复过程直到结束.
'''
#time
import time
from functools import wraps

def timeCount(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}的计算时间为:{end-start}')
        return result
    return wrapper


class Solution:
    @timeCount
    def selectSort(self,ls:List[int],replace = False)->List[int]:
        if replace == False:
            nums = ls.copy()
        else:
            nums = ls
        Len = len(nums)
        if Len <=1:
            return Len
        for idx in range(0,Len-1):
            minIdx = idx
            for j in range(idx,Len):
                minIdx = (j if nums[minIdx] > nums[j] else minIdx)
            nums[minIdx], nums[idx] = nums[idx], nums[minIdx]
        return nums



ls = permutation([i for i in range(2000)])
for i in range(5):
    ls_sorted = Solution().selectSort(ls)
# print(f'original list:\t{ls}')
# print(f'sorted list:\t{ls_sorted}')