S = "CH2546DF3"
print(S)

def checkType(s):
    l = 0
    n = 0

    for i in range(0,len(s)):
        a=s[i]
        if(a.isalpha()):
            l=l+1
        else:
            n=n+1

    a={'letters':l,'num':n}
    print(a)

checkType(S)