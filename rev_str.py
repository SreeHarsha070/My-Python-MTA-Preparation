"""
s=input()
rev=[]
s1=''
for i in s.split(" "):
    s1+=''.join(i[::-1])
    s1+=' '
print(s1)
"""
"""
leet code : Plus One
digits=[1,0,0,0,0,0]
num = 0
for i in range(len(digits)):
    num += digits[i] * pow(10, (len(digits)-1-i))
k=[int(i) for i in str(num+1)]
print(k)
"""
