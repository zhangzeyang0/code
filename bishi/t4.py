import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    max_sum_list = []
    for i in values:
        if not max_sum_list:
            max_sum_list.append([i, i])
        else:
            for j in range(len(max_sum_list)):
                if max_sum_list[j][0] < i:
                    max_sum_list.append([i, max_sum_list[j][1] + i])
                elif max_sum_list[j][0] >= i:
                    if [i, i] not in max_sum_list:
                        max_sum_list.append([i, i])
    print(sorted(max_sum_list, key=lambda x:x[1])[-1][1])

# 5 1 3 4 9 7 6 8
# 13478
