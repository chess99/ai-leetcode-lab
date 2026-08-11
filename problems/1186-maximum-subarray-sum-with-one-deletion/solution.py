# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:26:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        keep=arr[0]; deleted=float('-inf'); answer=arr[0]
        for value in arr[1:]:
            deleted=max(deleted+value, keep)
            keep=max(keep+value, value)
            answer=max(answer, keep, deleted)
        return answer
