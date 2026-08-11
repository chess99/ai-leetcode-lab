# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        return sum(colors[i] != colors[(i+1)%len(colors)] != colors[(i+2)%len(colors)] for i in range(len(colors)))
