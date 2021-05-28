n=int(input())
l=[]
print("Primes : ")
for i in range(2,n+1):
    if i not in l:
        print(i, end=' ')
    for j in range(i*i,n+1,i):
        l.append(j)

