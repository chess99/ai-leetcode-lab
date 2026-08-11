from typing import List
class Solution:
 def numOfSubarrays(self,a:List[int],k:int,t:int)->int:
  s=sum(a[:k]);ans=s>=k*t
  for i in range(k,len(a)):s+=a[i]-a[i-k];ans+=s>=k*t
  return ans
