n=int(input())
times=[300,60,10]
result=[]
for i in times:
    result.append(n//i)
    n=n%i

if n!=0:
    print(-1)
else:
    for i in result:
        print(i,end=" ")