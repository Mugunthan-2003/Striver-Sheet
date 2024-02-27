#https://leetcode.com/problems/pascals-triangle/description/

n=20
pt=[[1],[1,1]]
for i in range(3,n+1):
    l=[1,1]
    for j in range(i-2):
        n=pt[i-2][j]+pt[i-2][j+1]
        l.insert(len(l)-1,n)
    pt.append(l)
print(pt)
