line = input()
nlist1 = list(map(int, line.split('-')[0].split(',')))
nlist2 = list(map(int, line.split('-')[1].split(':')[0].split(',')))
k = int(line.split('-')[1].split(':')[1])
res = []
# nlist1 = sorted(nlist1)
# nlist2 = sorted(nlist2)
for i in range(len(nlist1)):
    for j in range(len(nlist2)):
        temp = nlist1[i]+nlist2[j]
        if len(res) < k:
            res.append(temp)
        elif temp > min(res):
            res.remove(min(res))
            res.append(temp)
print(','.join(list(map(str, sorted(res, reverse=True)))))
'''
2,4,2,7,7-3,2,5,6,1,9:6
'''
