# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:59Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        values=set();answer=10**9
        for value in arr:
            values={value}|{value&old for old in values}
            answer=min(answer,*(abs(value-target)for value in values))
        return answer
