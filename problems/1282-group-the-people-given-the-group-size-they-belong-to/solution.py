# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:14Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
 def groupThePeople(self,groupSizes:List[int])->List[List[int]]:
  buckets=defaultdict(list); answer=[]
  for i,size in enumerate(groupSizes):
   buckets[size].append(i)
   if len(buckets[size])==size: answer.append(buckets.pop(size))
  return answer
