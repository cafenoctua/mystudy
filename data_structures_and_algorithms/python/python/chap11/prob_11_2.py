class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1] * n
        
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    def unit(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.par[x] < self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        return True

    def size(self, x):
        return -self.par[self.root(x)]
    
def main():
    # 入力
    input_data = [
        "5 4",
        "1 2",
        "2 3",
        "3 4",
        "4 5"
    ]
    
    input_iterator = iter(input_data)
    N, M = map(int, next(input_iterator).split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, next(input_iterator).split())
        A.append(a - 1)
        B.append(b - 1)
        
    uf = UnionFind(N)
    cur = N * (N-1) / 2
    res = []
    for i in range(M):
        res.append(cur)
        
        a = A[M - 1 - i]
        b = B[M - 1 - i]
        if uf.issame(a, b): continue
        
        sa = uf.size(a)
        sb = uf.size(b)
        cur -= sa * sb
        uf.unit(a, b)
    
    res.reverse()
    for i in range(len(res)):
        print(res[i])
    
    print(res)
    
if __name__ == "__main__":
    main()