from typing import List
from numpy.random import permutation
'''
希尔排序 (Shell)
平均复杂度: O(n1.3)
最坏复杂度: O(n2)
最好复杂度: O(n)

空间复杂度: 1
稳定性: 不稳定

思路: 
将整个序列分成gap分, 对于每个gap分的各个位置
while (gap>0):
    for i in range(gap,len(List)):  #本来插入排序是从idx=1的位置开始对比,但由于分组,所以需要从idx = 0+gap的时候开始
        key = list[i]
        j = i-gap  #间隔跳跃
        while j >= 0 and nums[j] > key: 
            nums[j+gap] = nums[j]
            j -= gap
        nums[j+gap] = key

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
        h=1
        while h <= len(nums)//3:
            h = h*3+1

        gap = len(nums) >>1
        while gap>0:
            for i in range(gap, len(nums)):
                temp = nums[i]
                j = i-gap
                while j >= 0 and nums[j] > temp:
                    nums[j+gap] = nums[j]
                    j -= gap
                nums[j+gap] = temp
            gap = (gap-1) //3

        return nums

ls = permutation([i for i in range(10000)])
for i in range(5):
    ls_sorted = Solution().shellSort(ls)