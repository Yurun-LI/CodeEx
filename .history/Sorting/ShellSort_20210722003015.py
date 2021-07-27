from typing import List
from numpy.random import permutation
'''
插入排序 (Insertion)
平均复杂度: O(n1.3)
最坏复杂度: O(n2)
最好复杂度: O(n)

空间复杂度: 1
稳定性: 稳定

思路: 

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
    @timeCount
    def shellSort(self, ls: List[int], replace=False) -> List[int]:
        if replace == False:
            nums = ls.copy()
        else:
            nums = ls
        gap = len(nums) >>1
        while gap>0:
            for i in range(gap, len(nums)):
                temp = nums[i]
                j = i-gap
                while j >= 0 and nums[j] > temp:
                    nums[j+gap] = nums[j]
                    j -= gap
                nums[j+gap] = temp
            gap = gap >>1 

        return nums

ls = permutation([i for i in range(10000)])
for i in range(5):
    ls_sorted = Solution().shellSort(ls)