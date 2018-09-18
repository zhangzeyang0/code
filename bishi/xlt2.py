line = input().split(',')
tlist = []
for i in line:
    tlist.append(int(i))
def find_num(nlist):
    for j in range(len(nlist)):
        if nlist[j] == sum(nlist[:j]) == sum(nlist[j+1:]):
            return nlist[j]
    return False
print(find_num(tlist))
'''
3,1,4,4
'''
