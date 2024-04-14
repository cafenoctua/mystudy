import math
PI = math.pi

def main():
    A, B, C = input().split()
    A, B, C = int(A), int(B), int(C)
    
    def func(t) -> float:
        return A * t + B * math.sin(C * PI * t)
    
    alpha = 0
    beta = 200
    for iter in range(100):
        gamma = (alpha + beta) / 2
        if func(gamma) < 100: alpha = gamma
        else: beta = gamma
    
    print(round(alpha, 15))

if __name__ == "__main__":
    main()