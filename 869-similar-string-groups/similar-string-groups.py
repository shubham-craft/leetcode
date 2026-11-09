class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.components = n
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        
        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[y_root] > self.rank[x_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        
        self.components -= 1

        return True

class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                str1 = strs[i]
                str2 = strs[j]
                diff = 0
                for pos in range(len(str1)):
                    if str1[pos] != str2[pos]:
                        diff += 1
                    
                        if diff > 2:
                            break
                
                if diff <= 2:
                    uf.union(i, j)

        return uf.components