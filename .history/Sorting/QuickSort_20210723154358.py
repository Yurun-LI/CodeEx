from typing import List
from numpy.random import permutation
import random
'''
快速排序 (Quick))
平均复杂度: O(nlogn)
最坏复杂度: O(n2)
最好复杂度: O(n)

空间复杂度: logn
稳定性: 不稳定

思路: 
采用分治思维
sort函数为:
治 : 先对当前序列进行切割 {x| x < pivot } {pivot} { x| x>= pivot} -->return pivot所在位置
分 : 对左半部分arr[left:mid] 实行排序, 再对右半部分arr[mid+1:right] 实行排序

核心伪代码:
def sort():
    if right>= left:
        return
    mid = partition(arr,left,right)
    sort(arr,left,mid-1)
    sort(arr,mid+1,right)


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
        print(f'{func.__name__}的运行时间为{end-start}')
        return result
    return wrapper


class Solution:
    @timeCount
    def quickSort(self, arr: List[int]):
        def sort(arr, leftBound, rightBound):
            if leftBound >= rightBound:
                return
            mid = self.partition(arr,leftBound,rightBound)
            sort(arr, leftBound,mid-1)
            sort(arr,mid+1, rightBound)
        sort(arr,0, len(arr)-1)

    def partition(self, arr: List[int], leftBound: int, rightBound: int):
        pivot = random.randint(leftBound, rightBound)
        arr[rightBound],arr[pivot] = arr[pivot],arr[rightBound]
        pivot = arr[rightBound]
        low, high = leftBound, rightBound-1
        # while low<high:
        #     if arr[low] >= pivot:
        #         if arr[high]<=pivot:
        #             arr[low],arr[high] = arr[high],arr[low]
        #             continue
        #         high-=1
        #         continue
        #     low+=1
        while low<=high:
            while low<=high and arr[low]<=pivot:
                low+=1 
            while low<=high and arr[high] > pivot:
                high-=1
            if low<high:
                arr[low],arr[high] = arr[high],arr[low]
    
        arr[low],arr[rightBound] = arr[rightBound],arr[low]
        return low
# arr = [1, 4, 5, 8, 2, 5, 7, 9, 12, 6]

# Solution().quickSort(arr)
# print(arr)

for i in range(10):
    ls = permutation([i for i in range(50000)])
    Solution().quickSort(ls)
    # print(ls)