# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:36Z
# Experiment: ai-leetcode-lab, round 1
import heapq
class Solution:
 def kSmallestPairs(self,a,b,k):
  h=[(a[i]+b[0],i,0) for i in range(min(k,len(a)))];heapq.heapify(h);r=[]
  while h and len(r)<k:
   _,i,j=heapq.heappop(h);r.append([a[i],b[j]])
   if j+1<len(b):heapq.heappush(h,(a[i]+b[j+1],i,j+1))
  return r
