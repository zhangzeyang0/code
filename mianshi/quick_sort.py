def partition(nlist, l, r):
    flag = nlist[r]
    j = -1
    for i in range(l, r):
        if nlist[i] < flag:
            j += 1
            nlist[i], nlist[j] = nlist[j], nlist[i]
    nlist[j+1] ,nlist[r] = nlist[r], nlist[j+1]
    return j+1

def quick_sort(nlist, l, r):
    if l < r:
        mid = partition(nlist, l, r)
        quick_sort(nlist, l, mid-1)
        quick_sort(nlist, mid+1, r)
a = [1,1,3,2,4]
quick_sort(a, 0, 4)
print(a)
