import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    ans = 0
    input = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        input.append(values)
    def find_k_y(x, k):
        bit_num = 1
        res = 0
        while k:
            if x & bit_num == 0:
                res += bit_num * (k & 1)
                k >>= 1
            bit_num <<= 1
        print(res)
    for i in input:
        x, k = i[0], i[1]
        find_k_y(x, k)
