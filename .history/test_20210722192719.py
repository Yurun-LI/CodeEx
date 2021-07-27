import numpy as np
import matplotlib.pyplot as plt
class Sort:
    def insertSort(self,ls):
        arr = ls.copy()
        Len = len(arr)
        if Len <=1:
            return arr
        for i in range(1,Len-1):
            curVal = arr[i]
            j = i-1
            while j>=0 and arr[j] > curVal:
                arr[j+1] = arr[j]
            arr[j+1] = curVal
        return arr
        

arr = np.random.permutation(np.arange(10))
print(Sort().insertSort(arr))
# def check():
#     for i in range(10):
        
        