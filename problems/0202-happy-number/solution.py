# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:23:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isHappy(self, n: int) -> bool:
        def next_number(value: int) -> int:
            total = 0
            while value:
                value, digit = divmod(value, 10)
                total += digit * digit
            return total

        slow = fast = n
        while True:
            slow = next_number(slow)
            fast = next_number(next_number(fast))
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
