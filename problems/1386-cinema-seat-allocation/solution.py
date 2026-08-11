from collections import defaultdict
from typing import List
class Solution:
 def maxNumberOfFamilies(self,n:int,reservedSeats:List[List[int]])->int:
  d=defaultdict(int)
  for r,s in reservedSeats:d[r]|=1<<s
  ans=2*n
  for mask in d.values():
   left=0b11110<<1;mid=0b11110<<3;right=0b11110<<5
   if mask&left and mask&right:ans-=1 if not mask&mid else 2
   elif mask&left or mask&right:ans-=1
  return ans
