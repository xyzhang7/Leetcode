import math

def Combination(n, k):
    f = math.factorial
    return f(n) // f(k) // f(n-k)

if __name__ == '__main__':
    f = math.factorial
    print(f(7) // f(3) // f(2) // f(2) // 2)