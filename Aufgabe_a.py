def findMax(l):
    max =l[0]
    maxIndex=0
    for i in range(0,len(l)):
        if l[i] > max:
            max = l[i]
            maxIndex = i
    return maxIndex

def findMin(l):
    min = l[0]
    minIndex = 0
    for i in range(0,len(l)):
        if l[i] < min:
            min = l[i]
            minIndex = i
    return minIndex


L = [5, 1, 7, -2, -6, 0, 3, -1, 8, 4]
print(L)
b = findMin(L)

del L[b]
#print(a)
c = findMin(L)
del L[c]
#print(a)

d= findMax(L)
del L[d]
#print(a)
e= findMax(L)
del L[e]
print(L)
