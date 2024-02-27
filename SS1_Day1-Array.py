#https://leetcode.com/problems/set-matrix-zeroes/

matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
row=[]
col=[]
r=len(matrix)
cn=len(matrix[0])
for i in range(r):
    if(0 in matrix[i]):
        ind=[j for j,e in enumerate(matrix[i]) if e==0]
        col=list(set(col+ind))
        row+=[i]
        continue
for i in range(r):
    if i in row:
        matrix[i]=[0]*cn
    else:
        for j in col:
            matrix[i][j]=0
print(matrix)
