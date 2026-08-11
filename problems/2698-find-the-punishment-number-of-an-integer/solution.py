# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_split(square: str, target: int, index: int = 0) -> bool:
            if index == len(square):
                return target == 0
            value = 0
            for end in range(index, len(square)):
                value = value * 10 + int(square[end])
                if value > target:
                    break
                if can_split(square, target - value, end + 1):
                    return True
            return False

        return sum(value * value for value in range(1, n + 1) if can_split(str(value * value), value))
