# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:14Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        counts = Counter(nums)
        answer = 0
        for split in range(1, len(target)):
            left = target[:split]
            right = target[split:]
            if left == right:
                answer += counts[left] * (counts[left] - 1)
            else:
                answer += counts[left] * counts[right]
        return answer
