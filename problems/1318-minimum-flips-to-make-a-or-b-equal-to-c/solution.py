class Solution:
 def minFlips(self,a:int,b:int,c:int)->int:
  return sum(((a>>i&1)+(b>>i&1) if not(c>>i&1) else 0 if (a>>i&1 or b>>i&1) else 1) for i in range(31))
