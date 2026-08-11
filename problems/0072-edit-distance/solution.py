# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:16:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        previous = list(range(len(word2) + 1))
        for i, char1 in enumerate(word1, 1):
            current = [i]
            for j, char2 in enumerate(word2, 1):
                if char1 == char2:
                    current.append(previous[j - 1])
                else:
                    current.append(1 + min(previous[j], current[j - 1], previous[j - 1]))
            previous = current
        return previous[-1]
