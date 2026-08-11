# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        answer = counts[1] if counts[1] % 2 else counts[1] - 1
        for start in counts:
            if start == 1:
                continue
            length = 1
            value = start
            while counts[value] >= 2 and value * value in counts:
                length += 2
                value *= value
            answer = max(answer, length)
        return answer
