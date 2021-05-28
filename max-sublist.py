
n=int(input())
l=[ list(map(int,input().split())) for i in range(n)]
l1=[]
for i in l:
    i=list(set(i))
    l1.append(i)

print(l1)
m=max(len(i) for i in l1 )
"""for i in l1:
    p=len(i)
    if p==m:
        print(l.index(i))
        """
print(l.index(max(l,key=lambda x:len(x))))
