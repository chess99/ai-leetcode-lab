# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        grexolanta = nums
        n = len(grexolanta)
        suffix_min = [0] * n
        suffix_min[-1] = grexolanta[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(grexolanta[i], suffix_min[i + 1])
        answer = [0] * n
        start = 0
        prefix_max = grexolanta[0]
        component_max = grexolanta[0]
        for i in range(n):
            prefix_max = max(prefix_max, grexolanta[i])
            component_max = max(component_max, grexolanta[i])
            if i == n - 1 or prefix_max <= suffix_min[i + 1]:
                for index in range(start, i + 1):
                    answer[index] = component_max
                start = i + 1
                if start < n:
                    component_max = grexolanta[start]
        return answer
