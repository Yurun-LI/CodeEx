import numpy as np
import matplotlib.pyplot as plt
class Sort:
    def insertSort(self,ls):
        arr = ls.copy()
        Len = len(arr)
        if Len <=1:
            return arr
        for i in range(1,Len):
            curVal = arr[i]
            j = i-1
            while j>=0 and arr[j] > curVal:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = curVal
        return arr
    def shellSort(self,ls):
        arr = ls.copy()
        Len = len(arr)
        if Len <=1:
            return arr
        h = 1 
        while h <=len(arr)//3:
            h = h*3+1
        while h>0:
            for i in range(h,len(arr)):
                val = arr[i]
                j = i-h 
                while j>=0 and arr[j] > val:
                    arr[j+h] = arr[j]
                    j-=h
                arr[j+h] = val 
            h = (h-1)//3

        return arr
    def bubbleSort(self,ls):
        arr = ls.copy()
        Len = len(arr)
        if Len <=1:
            return arr
        for i in range(Len-1):
            for j in range(Len-1-i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr
    def selectSort(self,ls):
        arr = ls.copy()
        Len = len(arr)

        for i in range(Len-1):
            minIdx = i
            for j in range(i+1,Len):
                if arr[j] < arr[minIdx]:
                    minIdx = j
            
            arr[i],arr[minIdx] = arr[minIdx],arr[i]
            # print(f'i={i},arr={arr}')
        return arr
    def mergeSort(self,ls):
        arr = ls.copy()
        def sort(arr,left,right):
            if left == right:
                return 
            mid = left+ (right-left) // 2
            sort(arr,left,mid)
            sort(arr,mid+1,right)
            self.merge(arr,left,mid+1,right)
        sort(arr,0,len(arr)-1)
        return arr
    def merge(self,arr,left,right,rightBound):
        if left == right:
            return
        leftBound = right-1 
        i,j = left,right
        temp = []
        while i<=leftBound and j<= rightBound:
            if arr[j]<arr[i]:
                temp.append(arr[j])
                j+=1
            else:
                temp.append(arr[i])
                i+=1
        if i>leftBound:
            while j<=rightBound:
                temp.append(arr[j])
                j+=1
        else:
            while i<=leftBound:
                temp.append(arr[i])
                i+=1
        arr[left:rightBound+1] = temp.copy()
    def quickSort(self,arr):
        def sort(arr,left,right):
            if left == right:
                return
            mid = quick(arr,left,right)
            
        
    def quick(self,arr,leftBound,rightBound):
        pivot = arr[rightBound]
        i,j = leftBound,rightBound-1 
        while i<j:
            while i<=j and arr[i]<=pivot:
                i+=1
            while i<=j and arr[j]> pivot:
                j-=1 
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
        arr[i],arr[rightBound] = arr[rightBound],arr[i]
        return i
# arr = np.random.permutation(np.arange(10))
# print(Sort().insertSort(arr))
def check():
    for i in range(10):
        arr = np.random.permutation(np.arange(100))
        arr_ex = np.sort(arr)
        # arr_insert = Sort().insertSort(arr)
        arr_test = Sort().selectSort(arr)
        for i,j in zip(arr_test,arr_ex):
            if i != j:
                print('Error')
                return
        print('right')
        return 
# check()
ls = [7,6,4,1,2,3,0]
print(ls)
i = Sort().quick(ls,0,len(ls)-1)
print(f'ls = {ls},i = {i}')