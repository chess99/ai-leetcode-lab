class Solution:
 def angleClock(self,h:int,m:int)->float:
  d=abs((h%12)*30+m*.5-m*6);return min(d,360-d)
