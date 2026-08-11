# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def calculateScore(self, s: str) -> int:
        positions = [[] for _ in range(26)]
        score = 0
        for i, char in enumerate(s):
            mirror = 25 - (ord(char) - ord('a'))
            if positions[mirror]:
                score += i - positions[mirror].pop()
            else:
                positions[ord(char) - ord('a')].append(i)
        return score
