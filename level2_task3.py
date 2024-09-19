a=int(input())
h=int(input())
p=int(input())
s=a
n=0
i=1
while s<=p:
    i+=1
    n+=1
    s+=(a+n*h)
print(i)
