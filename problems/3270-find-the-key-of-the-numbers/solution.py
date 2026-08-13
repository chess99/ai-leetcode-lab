# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:48:12Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        digits = zip(f"{num1:04d}", f"{num2:04d}", f"{num3:04d}")
        return int("".join(min(first, second, third) for first, second, third in digits))
