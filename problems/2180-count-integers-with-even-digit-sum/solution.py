# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:18:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countEven(self, num: int) -> int:
        return sum(sum(map(int, str(value))) % 2 == 0 for value in range(1, num + 1))
