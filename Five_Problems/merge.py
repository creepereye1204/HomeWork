import sys
sys.setrecursionlimit(10**6)

def Divide(n):

    if len(n)<2:
        return n
    else:
        a = Divide(n[:len(n) // 2])
        b = Divide(n[len(n) // 2:])
    return Conquer(a,b)
def Conquer(n,m):
    z=[]
    l,r=0,0
    while l<len(n) and r<len(m):
        if n[l]<m[r]:
            z.append(n[l])
            l+=1
        else:
            z.append(m[r])
            r+=1
    z+=n[l:]+m[r:]
    return z


C=input()
L=[]
for c in C:
    L.append(int(ord(c)))

L=Divide(L)
u=list(map(lambda x:chr(x),L))
print(''.join(u))


