from typing import List
class Solution:
    def countDigitOne(self,n:int)->int:
        if n < 10:
            if n < 1:
                return 0
            else:
                return 1
        dgs = self.digits(n) #位数
        l1 = 1 #最大位数 如 241 -> 100
        for i in range(dgs-1):
            l1*=10
        l2 = n - (n//l1)*l1 #余 241 -> 41
        l3 = n//l1 #最高位值  241 -> 2
        if l3 == 1:
            return (l2+1) + self.countDigitOne(l2) + self.countDigitOne(l1 - 1)
        else:
            return self.countDigitOne(l2) + l1 +self.countDigitOne(l1-1) + (l3-2+1) * self.countDigitOne(l1-1)
    def digits(self,n):
        dgs = 0
        while n != 0 :
            dgs +=1
            n = n//10
        return dgs
n = 53
print(Solution().countDigitOne(13))