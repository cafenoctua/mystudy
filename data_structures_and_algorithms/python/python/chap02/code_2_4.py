from math import sqrt

def calc_dist(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

def main():
    N = int(input())
    x, y = zip(*(map(float, input().split()) for _ in range(N)))
    
    minimun_dist = 100000000.0
    
    for i in range(N):
        for j in range(i + 1, N):
            dist_i_j = calc_dist(x[i], y[i], x[j], y[j])
            if (dist_i_j < minimun_dist):
                minimun_dist = dist_i_j
    
    print(minimun_dist)
    
if __name__ == "__main__":
    main()