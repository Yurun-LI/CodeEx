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
    def shellSort(self, ls: List[int], replace=False) -> List[int]:
        if replace == False:
            nums = ls.copy()
        else:
            nums = ls
        
        gap = 4

        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i-gap
            while j >= 0 and nums[j] > temp:
                nums[j+gap] = nums[j]
                j -= gap
            nums[j+gap] = temp

        return nums

ls = [9,6,11,3,5,12,8,7,10,15,14,4,1,13,2]
print(Solution().shellSort(ls))