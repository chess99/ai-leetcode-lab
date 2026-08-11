# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:18:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countMonobit(self, n: int) -> int:
        count = 1
        value = 1
        while value <= n:
            count += 1
            value = (value << 1) | 1
        return count
