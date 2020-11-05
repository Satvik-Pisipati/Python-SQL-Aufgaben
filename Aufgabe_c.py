def ref(a):
    max = len(a[0])
    maxIndex = 0


    for i in range(0, len(a)):
        if len(a[i]) > max:
            max = len(a[i])
            maxIndex=i

    print(maxIndex, max)


    for k in range (0,len(a)):
        if k != maxIndex:
            h = len(a[k])


            u = max-h


            d=[]
            for z in range(0,u):

                d.append(0)

            r=a[k]

            for t in range(0,len(d)):
                r.append(d[t])
    print(a)

l=[[12, -3], [-2], [15, 2, -8], [-1, 0, 5], []]
ref(l)