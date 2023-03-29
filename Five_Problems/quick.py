import sys
sys.setrecursionlimit(10**6)

def Divide(l,r):
    if l<r:
        p=Conquer(l,r)
        Divide(l,p-1)
        Divide(p+1,r)

def Conquer(l,r):
    i=l-1
    for j in range(l,r):

        if L[j]<L[r]:
            i+=1
            L[i],L[j]=L[j],L[i]
    L[i+1],L[r]=L[r],L[i+1]
    return i+1

C=input()
L=[]
for c in C:
    L.append(int(ord(c)))

Divide(0,len(L)-1)
u=list(map(lambda x:chr(x),L))
print(''.join(u))
