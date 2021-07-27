from typing import List
from numpy.random import permutation
import random
'''
计数排序 (Count)
平均复杂度: O(n+k)
最坏复杂度: O(n+k)
最好复杂度: O(n+k)

空间复杂度: n+k
稳定性: 改进前不稳定,利用累加数组定位后稳定

思路: 
1. 建立一个计数数组,然后改造技术数组为累加数组,其中每个index的value为排序完毕后
index所在的最后位置
2. 倒叙遍历原数组,并将原数组中值进行新数组的映射: 
    new_arr[countArr[arr[i]]] = arr[i] #进行映射
    countArr[arr[i]]-=1 #映射完毕后在技术数组中相应索引的值上减去1
3. 输出新数组

用途: 大规模,小范围int数组:
如: [1, 3, 1, 2, 2, 2, 2, 1, 3, 2, 3, 1, 2, 2, 3, 3, 2, 2, 1, 3]这样的数组

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
    def countSort(self,arr):
        maxVal = max(arr)
        cntArr = [0 for i in range(maxVal+1)]
        sortedArr = [0 for i in range(len(arr))]
        for i in range(len(arr)):
            curVal = arr[i]
            cntArr[curVal] += 1
        for i in range(1,len(cntArr)):
            cntArr[i] += cntArr[i-1]
        for i in range(len(arr)-1,-1,-1):
            curVal = arr[i]
            newIdx = cntArr[curVal]-1
            sortedArr[newIdx] = curVal
        return sortedArr


for i in range(10):
    arr = random.choices(range(10),k=10000)
    print(arr[0:-1:1000])
    arr = Solution().countSort(arr)
    print(arr[0:-1:1000])
