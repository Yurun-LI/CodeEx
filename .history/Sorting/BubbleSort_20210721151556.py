from typing import List
from numpy.random import permutation
'''
冒泡排序 (Bubble)
平均复杂度: O(n2)
最坏复杂度: O(n2)
最好复杂度: O(n)

空间复杂度: 1
稳定性: 稳定

思路: 
for times in [0,length-1):
    从index=[0,len-1-i)依次比较nums[j]和nums[j+1],如果大于则交换位置
本质上是依次将最大的,第二大的...顺序交换到数组最后的一些位置中

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
    def bubbleSort(self,ls:List[int],replace = False)->List[int]:
        if replace == False:
            nums = ls.copy()
        else:
            nums = ls
        Len = len(nums)
        if Len<=1:
            return nums
        for i in range(Len-1):
            for j in range(0,Len-1-i):
                if nums[j] >nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums
    
ls = permutation([i for i in range(10000)])
for i in range(5):
    ls_sorted = Solution().bubbleSort(ls)
# print(f'original list:\t{ls}')
# print(f'sorted list:\t{ls_sorted}')