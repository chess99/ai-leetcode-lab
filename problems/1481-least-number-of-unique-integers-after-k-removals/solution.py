# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:53:31Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        remaining=len(set(arr))
        for count in sorted(Counter(arr).values()):
            if count>k: break
            k-=count;remaining-=1
        return remaining
