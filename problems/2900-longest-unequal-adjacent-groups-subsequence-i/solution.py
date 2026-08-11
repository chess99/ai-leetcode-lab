# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:30:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        previous_group = None

        for word, group in zip(words, groups):
            if group != previous_group:
                result.append(word)
                previous_group = group

        return result
