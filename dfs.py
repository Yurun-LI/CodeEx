#%%
from typing import List
import collections

# %%
class Solution():
    def __init__(self,n,relation,k):
        self.n = n
        self.relation = relation
        self.k = k
    def numWays(self) -> int:
        self.ways = 0
        self.edges = collections.defaultdict(list)
        for src, dst in self.relation:
            self.edges[src].append(dst)

        self.dfs(0,0)
        return self.ways 

    def dfs(self, index, steps):
        if steps == self.k:
            if index == self.n-1:
                self.ways += 1
            return
        for to in self.edges[index]:
            print(index,to)
            self.dfs(to, steps+1)
    
#%%
def main():
    n = 5
    relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
    k = 3
    solution = Solution(n,relation,k)
    return solution.numWays()
    

if __name__ == '__main__':
    print(main())