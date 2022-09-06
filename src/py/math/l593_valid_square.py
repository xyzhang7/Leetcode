def validSquare(p1, p2, p3, p4):
    """
    Given four points, p_i is [x_i, y_i] in x-y axis
    Find if these four points can form a valid square
    """
    points = [p1, p2, p3, p4]
    points.sort()
    # points.sort(key=lambda axis: axis[0])
    print(points)

if __name__ == "__main__":
    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [1, 0]
    p4 = [0, 1]
    validSquare(p1, p2, p3, p4)


