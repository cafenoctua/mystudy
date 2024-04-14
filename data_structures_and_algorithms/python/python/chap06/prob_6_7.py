class BIT:
    def __init__(self, n):
        self.UNITY_SUM = 0  # to be set
        self.dat = [self.UNITY_SUM] * (n + 1)

    def init(self, n):
        self.dat = [self.UNITY_SUM] * (n + 1)

    def add(self, a, x):
        while a < len(self.dat):
            self.dat[a] += x
            a += a & -a

    def sum(self, a):
        res = self.UNITY_SUM
        while a > 0:
            res += self.dat[a]
            a -= a & -a
        return res

    def sum_range(self, a, b):
        return self.sum(b - 1) - self.sum(a - 1)

    def print(self):
        for i in range(1, len(self.dat)):
            print(self.sum_range(i, i + 1), end=",")
        print()


def main():
    N = int(input())
    a = list(map(int, input().split()))
    low, high = 0, 1 << 30
    geta = N + 1

    while high - low > 1:
        mid = (low + high) // 2
        num = 0
        bit = BIT(N * 2 + 10)
        s = 0
        bit.add(s + geta, 1)

        for i in range(N):
            val = 1 if a[i] <= mid else -1
            s += val
            num += bit.sum_range(1, s + geta)
            bit.add(s + geta, 1)

        if num > (N + 1) * N // 2 // 2:
            high = mid
        else:
            low = mid

    print(high)


if __name__ == "__main__":
    main()
