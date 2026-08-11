# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:05:39Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        return all(words[index][-1] == words[(index + 1) % len(words)][0] for index in range(len(words)))
