from operator import itemgetter

def sol():
    T = input()

    for t in range(int(T)):
        N = int(input())
        fabrics = []
        for idx in range(N):
            fabrics.append(tuple(input().split()))
        fabrics = sorted(fabrics, key=itemgetter(0))
        print(fabrics)
        fabrics_pos = {i: fabrics[i][2] for i in range(N)}
        print(fabrics_pos)
        for i in range(1, 3):
            fabrics = sorted(fabrics, key=itemgetter(i))
            for k, v in dict(fabrics_pos).items():
                if fabrics[k][2] != v:
                    fabrics_pos.pop(k)
        print(f"Case #{t}: {len(fabrics_pos)}")

if __name__ == '__main__':
    sol()

