# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:04:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        previous=0
        for value in arr:
            missing=value-previous-1
            if k<=missing:return previous+k
            k-=missing; previous=value
        return previous+k
