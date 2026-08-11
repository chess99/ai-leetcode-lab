# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:32:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            quotient, remainder = divmod(num, mid)
            if remainder == 0 and quotient == mid:
                return True
            if mid < quotient:
                left = mid + 1
            else:
                right = mid - 1
        return False
