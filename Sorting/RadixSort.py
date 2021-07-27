from typing import List
from numpy.random import permutation
import random
'''
基数排序 (Radix)
平均复杂度: O(kN)
最坏复杂度: O(kN)
最好复杂度: O(kN)

空间复杂度: N+k
稳定性: 稳定

思路: 
从个位开始依次对每一位进行排序:
按照排序位数将各个数组分别装入不同的堆
然后依次从各个堆中拿出,并进入下一轮的排序

改进:
LSD: 高位开始,每个关键字采用计数排序
MSD: 低位开始,每个关键字采用桶排序

如: 

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
    def radixSort(self,arr):
