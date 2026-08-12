# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:29Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        frequencies = Counter()
        selected = 0
        answer = 0
        dominant = -1
        for index, (first, second) in enumerate(zip(nums1, nums2)):
            if first == second:
                selected += 1
                answer += index
                frequencies[first] += 1
                if frequencies[first] > frequencies[dominant]:
                    dominant = first

        for index, (first, second) in enumerate(zip(nums1, nums2)):
            if frequencies[dominant] * 2 <= selected:
                break
            if first != second and first != dominant and second != dominant:
                selected += 1
                answer += index
        return answer if frequencies[dominant] * 2 <= selected else -1
