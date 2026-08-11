# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:30:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for first, second in zip(s1, s2):
            if first == 'x' and second == 'y': xy += 1
            elif first == 'y' and second == 'x': yx += 1
        if (xy + yx) % 2:
            return -1
        return xy // 2 + yx // 2 + 2 * (xy % 2)
