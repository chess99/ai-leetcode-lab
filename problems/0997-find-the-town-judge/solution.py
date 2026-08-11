# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:22:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1; score[b] += 1
        for person in range(1, n + 1):
            if score[person] == n - 1: return person
        return -1
