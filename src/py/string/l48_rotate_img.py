from typing import List


def rotate(matrix: List[List[int]]) -> None:
    N = len(matrix)
    for i in range(N>>1):
        temp_row = matrix[i][:]
        matrix[i] = matrix[N - 1 - i][:]
        matrix[N - 1 - i] = temp_row

if __name__ == "__main__":
    n, digit = divmod(10036, 10)
