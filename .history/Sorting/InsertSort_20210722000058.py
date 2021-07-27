from typing import List
from numpy.random import permutation
'''
插入排序 (Insertion)
平均复杂度: O(n2)
最坏复杂度: O(n2)
最好复杂度: O(n)

空间复杂度: 1
稳定性: 稳定

思路: 
for i in [1,len):
    key = list[i]
    j从i-1开始, 如果list[j] 小于key,则将值后移,直到j<0 或者 出现nums[j] <= key,停止迭代
    此时 插入点index为j+1,所有令list[j+1] = key
'''
# time
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
    def insertSort(self, ls: List[int], replace=False) -> List[int]: #选择的手段
        if replace == False:
            nums = ls.copy()
        else:
            nums = ls
        Len = len(nums)
        if Len<=1:
            return nums
        for i in range(1,Len):
            key = nums[i]
            j = i-1
            while nums[j] > key and j>=0:
                nums[j+1] = nums[j]
                j-=1 
            nums[j+1] = key
        return nums
    def insertSort2(self, ls: List[int], replace=False) -> List[int]: #冒泡的手段
        if replace == False:
            nums = ls.copy()
        else:
            nums = ls
        for i in range(1,len(nums)):
            for j in range(i,0,-1):
                if nums[j] < nums[j-1]:
                    nums[j],nums[j-1] = nums[j-1],nums[j]
        return nums

ls = permutation([i for i in range(1000)])
for i in range(5):
    ls_sorted = Solution().insertSort2(ls)
# print(f'original list:\t{ls}')
# print(f'sorted list:\t{ls_sorted}')



