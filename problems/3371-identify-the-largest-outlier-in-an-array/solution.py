# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        count = Counter(nums)
        answer = -float('inf')
        for outlier in nums:
            remaining = total - outlier
            if remaining % 2 == 0:
                special = remaining // 2
                if count[special] > (special == outlier):
                    answer = max(answer, outlier)
        return answer
