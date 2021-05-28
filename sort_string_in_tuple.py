"""tup=tuple(input().split())
print(sorted(tup,key=lambda x:x[1]))
"""
tup=[tuple(tuple(map(int,input().split()))) for i in range(3)]
print(tuple(sorted(tup,key=lambda x:len(x))))


