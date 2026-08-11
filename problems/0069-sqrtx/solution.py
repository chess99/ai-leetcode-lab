# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:13:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        answer = 0
        while left <= right:
            middle = (left + right) // 2
            if middle * middle <= x:
                answer = middle
                left = middle + 1
            else:
                right = middle - 1
        return answer
