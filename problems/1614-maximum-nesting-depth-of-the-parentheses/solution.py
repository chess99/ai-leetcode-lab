# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:18:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxDepth(self, s: str) -> int:
        depth = best = 0
        for char in s:
            if char == '(':
                depth += 1
                best = max(best, depth)
            elif char == ')':
                depth -= 1
        return best
