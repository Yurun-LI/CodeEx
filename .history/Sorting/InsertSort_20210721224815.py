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
    def insertSort(self, ls: List[int], replace=False) -> List[int]:
        if replace == False:
            nums = ls.copy()
        else:
            nums = ls
        Len = len(nums)
        if Len<=1:
            return nums
        for i in range(1, Len):
            curVal = nums[i]
            for j in range(i-1,-1,-1):
                if nums[j] > curVal:
                    nums[j+1] = nums[j]
                    nums[j] = curVal
                else:
                    break
            nums[j+1] = curVal

        return nums

ls = permutation([i for i in range(10)])
for i in range(1):
    ls_sorted = Solution().insertSort([3,1,2])
# print(f'original list:\t{ls}')
print(f'sorted list:\t{ls_sorted}')



