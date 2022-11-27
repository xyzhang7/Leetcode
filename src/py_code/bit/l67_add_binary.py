def addBinary_bit_by_bit_computation(a: str, b: str) -> str:
    n = max(len(a), len(b))
    a.zfill(n)
    b.zfill(n)
    carry = 0
    result = []
    for i in range(n-1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1
        result.append(carry % 2)
        carry //= 2
    result.reverse()
    return ''.join(result)

def addBinary_bit_manipulation(a: str, b: str) -> str:
    """
    Add without using addition operation
    * Here XOR is a key as well, because it's a sum of two binaries without taking carry into account.
    * To find current carry is quite easy as well, it's AND of two input numbers, shifted one bit to the left.
    """
    a, b = int(a, 2), int(b, 2)
    while b:
        answer = a ^ b
        carry = (a & b) << 1
        a, b = answer, carry
    return bin(a)[2:]  # convert result to binary format and remove the '0b' prefix

if __name__ == '__main__':
    addBinary_bit_manipulation("1111", "10")
