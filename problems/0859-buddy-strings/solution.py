# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:05:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        differences = [(left, right) for left, right in zip(s, goal) if left != right]
        return len(differences) == 2 and differences[0] == differences[1][::-1]
