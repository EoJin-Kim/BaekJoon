a=list(map(int,input().split()))
b=list(map(int,input().split()))
aSum=sum(a)
bSum=sum(b)

if aSum>=bSum:
    print(aSum)
else:
    print(bSum)
