n=int(input())
m=int(input())
ls=[]
for i in range(n):
    l=[]
    for j in range(m):

        p=str(i)+","+str(j)
        l.append(p)
    print(l)
    ls.append(l)
print(ls)
