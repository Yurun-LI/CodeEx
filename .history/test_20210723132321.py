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
        if Len <=1:
            return arr
        for i in range(Len-1):
            minIdx = i
            for j in range(i+1,Len):
                if arr[j] < arr[minIdx]:
                    minIdx = j
            
            arr[i],arr[minIdx] = arr[minIdx],arr[i]
            print(f'i={i},arr={arr}')
        return arr
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
print([4,2,6,1,7,3])
Sort().selectSort([4,2,6,1,7,3])  