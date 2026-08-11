# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter, defaultdict
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        changes = defaultdict(int)
        count = Counter(nums)
        for value in nums:
            changes[value - k] += 1
            changes[value + k + 1] -= 1
        active = answer = 0
        for point in sorted(set(changes) | set(count)):
            active += changes[point]
            answer = max(answer, min(active, numOperations + count[point]))
        return answer
