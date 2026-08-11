# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minFlips(self, target: str) -> int:
        flips=0
        for char in target:
            if int(char)!=flips%2:flips+=1
        return flips
