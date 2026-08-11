# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:05:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(value) if value.isdigit() else len(value) for value in strs)
