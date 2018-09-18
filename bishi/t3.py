import sys

def group(ss):
    if not len(ss):
        return []
    if len(ss) == 1:
        return list(ss)
    charList = list(ss)
    charList.sort()
    pStr = []
    for i in range(len(charList)):
        pStr.append(charList[i])
        if i > 0 and charList[i] == charList[i - 1]:
            continue
        temp = group(''.join(charList[i + 1:]))
        for j in temp:
            pStr.append(charList[i] + j)
        pStr = list(set(pStr))
        pStr.sort()
    return pStr


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    temp_list = []
    num_list = [str(one) for one in range(10)]
    idx = 0
    idx1_list = []
    while idx < len(values):
        if values[idx] == 0:
            temp_list.append(num_list[idx])
            idx += 1
        else:
            start = idx
            while idx < len(values) and values[idx] == 1:
                idx += 1
            temp_list.append(num_list[start:idx])
            idx1_list.append(len(temp_list)-1)
    del(values)
    del(num_list)
    temp_list = [''.join(one) for one in temp_list]

    input_list = [str(i) for i in range(len(temp_list))]
    res_list = group(input_list)
    del(input_list)
    res_list = sorted(res_list)
    for one in res_list:
        temp = ''
        flag = True
        for idx in idx1_list:
            if str(idx) not in one:
                flag = False
                break
        if flag:
            for i in one:
                temp += temp_list[int(i)]
            print(temp)
