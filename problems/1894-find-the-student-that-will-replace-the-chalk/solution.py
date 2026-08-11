# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:47:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k%=sum(chalk)
        for i,value in enumerate(chalk):
            if k<value:return i
            k-=value
