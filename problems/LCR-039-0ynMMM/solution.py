# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []; ans = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                p = stack.pop(); left = stack[-1] if stack else -1
                ans = max(ans, heights[p] * (i - left - 1))
            stack.append(i)
        return ans
