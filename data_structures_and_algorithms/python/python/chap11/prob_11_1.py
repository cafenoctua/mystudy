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
    
    def unit(self, x, y):
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
        
    res = 0
    for e in range(M):
        uf = UnionFind(N)
        for i in range(M):
            if i == e: continue
            uf.unit(A[i], B[i])
            
        num = 0
        for v in range(N):
            if uf.root(v) == v: num += 1
        
        if num > 1: res += 1

    print(res)
    
if __name__ == "__main__":
    main()