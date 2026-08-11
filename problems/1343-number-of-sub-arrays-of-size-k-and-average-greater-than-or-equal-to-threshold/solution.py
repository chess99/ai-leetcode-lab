# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:41:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        count = int(total >= k * threshold)
        for i in range(k, len(arr)):
            total += arr[i] - arr[i - k]
            count += total >= k * threshold
        return count
