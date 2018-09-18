#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

def LCS_length(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[i+1][j+1] = c[i][j]+1
            else:
                c[i+1][j+1] = max(c[i+1][j], c[i][j+1])
    return c[-1][-1]
if __name__ == "__main__":
    # 读取第一行的n
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    print(LCS_length(str1, str2))


