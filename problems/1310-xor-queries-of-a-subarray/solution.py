# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for value in arr: prefix.append(prefix[-1] ^ value)
        return [prefix[right + 1] ^ prefix[left] for left, right in queries]
