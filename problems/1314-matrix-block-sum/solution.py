from typing import List
class Solution:
 def matrixBlockSum(self,mat:List[List[int]],k:int)->List[List[int]]:
  m,n=len(mat),len(mat[0]);p=[[0]*(n+1) for _ in range(m+1)]
  for i in range(m):
   for j in range(n):p[i+1][j+1]=mat[i][j]+p[i][j+1]+p[i+1][j]-p[i][j]
  return [[p[min(m,i+k+1)][min(n,j+k+1)]-p[max(0,i-k)][min(n,j+k+1)]-p[min(m,i+k+1)][max(0,j-k)]+p[max(0,i-k)][max(0,j-k)] for j in range(n)] for i in range(m)]
