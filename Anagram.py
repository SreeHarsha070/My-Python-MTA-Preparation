"""
s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=sorted(s1)
s2=sorted(s2)
print(s1)
print(s2)
if(s1==s2):
    print("True")
else:
    print("False")
"""
#----------------------
"""
def isanagram(s1,s2):
    dic={}
    if(len(s1)!=len(s2)):
        return False
    else:
        for i in s1:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1
        for i in s2:
            if i not in dic.keys():
                return False
            else:
                dic[i]-=1
    return not any(dic.values())
                
s1=input()
s2=input()
print(isanagram(s1,s2))
"""
s1=input()
dic = {}
for i in s1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(max(dic.values(),dic.keys()))


