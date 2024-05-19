class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        
        if x == y:
            return False
        
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True
    
    def size(self, x):
        return self.siz[self.root(x)]
    
if __name__ == "__main__":
    uf = UnionFind(7)  # {0}, {1}, {2}, {3}, {4}, {5}, {6}

    uf.unite(1, 2)  # {0}, {1, 2}, {3}, {4}, {5}, {6}
    uf.unite(2, 3)  # {0}, {1, 2, 3}, {4}, {5}, {6}
    uf.unite(5, 6)  # {0}, {1, 2, 3}, {4}, {5, 6}
    print(uf.issame(1, 3))  # True
    print(uf.issame(2, 5))  # False

    uf.unite(1, 6)  # {0}, {1, 2, 3, 5, 6}, {4}
    print(uf.issame(2, 5))  # True