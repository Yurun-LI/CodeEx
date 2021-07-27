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
    def countSort(self,arr):
        maxVal = max(arr)
        countArray = [0 for i in range(maxVal+1)]
        for i in range(len(arr)):
            curVal = arr[i]
            countArray[curVal] += 1
        j = 0
        for i in range(len(arr)):
            while countArray[j] != 0:
                arr[i] = j
                countArray[j]-=1
                i+=1
        print(arr)
        print(countArray)

arr = [0,5,5,3,3,2,5,1,6]
Solution().countSort(arr)