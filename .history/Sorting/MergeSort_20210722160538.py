from typing import List
from numpy.random import permutation
'''
归并排序 (Merge)
平均复杂度: O(nlogn)
最坏复杂度: O(nlogn)
最好复杂度: O(nlogn)

空间复杂度: n
稳定性: 稳定

思路: 
采用分而治之的方法
将数组先分,而后在重新合并

伪代码:
def sort():
    mid = left + (right-left) // 2
    sort(arr[left:mid])
    sort(arr[mid+1:right])
    merge(arr)->合并左右侧的两个有序数组

用途:速度仅次于快速排序，为稳定排序算法，一般用于对总体无序，但是各子项相对有序的数列
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
    def mergeSort(self,arr:List[int]):
        def sort(arr,left,right):
            if left<right:
                mid = left + (right - left) // 2 
                #左边归并排序
                sort(arr,left,mid)
                #右边归并排序
                sort(arr,mid+1,right)
                #将左右两个有序子数组进行合并操作
                self.merge(arr,left,mid+1,right)
        sort(arr,0,len(arr)-1)
        return arr
    #选定区域arr[left:right-1],arr[right:rightBound]两个有序子数组进行合并
    def merge(self,arr: List[int],leftPtr:int,rightPtr:int,rightBound:int)-> List[int]: #治-排序
        Start = leftPtr
        if leftPtr == rightPtr:
            return 
        leftBound = rightPtr-1
        temp = []
        while leftPtr<=leftBound and rightPtr <= rightBound:
            if arr[leftPtr] < arr[rightPtr]:
                temp.append(arr[leftPtr])
                leftPtr+=1
            else:
                temp.append(arr[rightPtr])
                rightPtr+=1 
        while(leftPtr<=leftBound):
            temp.append(arr[leftPtr])
            leftPtr+=1 
        while(rightPtr<=rightBound):
            temp.append(arr[rightPtr])
            rightPtr+=1 
        arr[Start:rightBound+1] = temp

ls = permutation([i for i in range(1000)])
print(f'original list:\t{ls}')
for i in range(1):
    ls_sorted = Solution().mergeSort(ls)
print(f'sorted list:\t{ls_sorted}')