from typing import List
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        def cal_add_rungs_between_two_steps(curr:int,nxt:int)->int:
            if (nxt-curr)%dist == 0:
                return (nxt-curr) //dist-1
            return (nxt-curr) //dist 
        rungs = [0]+rungs
        if rungs == [0]:
            return 0
        res = 0
        for ptr in range(len(rungs)-1):
            print(rungs[ptr])
            if rungs[ptr+1]-rungs[ptr] >dist:
                res += cal_add_rungs_between_two_steps(rungs[ptr],rungs[ptr+1])
        return res

rungs = [1,3,5,10]
dist = 2
print(Solution().addRungs(rungs,dist))