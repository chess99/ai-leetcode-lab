# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:03:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def valid(number):
            value = number
            while value:
                digit = value % 10
                if digit == 0 or number % digit:
                    return False
                value //= 10
            return True
        return [number for number in range(left, right + 1) if valid(number)]
