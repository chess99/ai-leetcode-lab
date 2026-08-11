# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:23:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def digitCount(self, num: str) -> bool:
        return all(num.count(str(i)) == int(ch) for i, ch in enumerate(num))
