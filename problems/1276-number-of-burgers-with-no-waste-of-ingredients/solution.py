# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
 def numOfBurgers(self,tomatoSlices:int,cheeseSlices:int)->List[int]:
  jumbo=tomatoSlices//2-cheeseSlices; small=2*cheeseSlices-tomatoSlices//2
  return [jumbo,small] if tomatoSlices%2==0 and jumbo>=0 and small>=0 else []
