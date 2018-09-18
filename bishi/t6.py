import sys

if __name__ == "__main__":
    input = []
    for i in range(3):
        line = sys.stdin.readline().strip()
        input.append(line)
    print(str(input[0]).replace(str(input[1]), str(input[2])))
