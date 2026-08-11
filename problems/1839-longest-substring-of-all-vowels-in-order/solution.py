# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        start = 0
        vowel_groups = 1
        longest = 0

        for index in range(1, len(word)):
            if word[index] < word[index - 1]:
                start = index
                vowel_groups = 1
            elif word[index] > word[index - 1]:
                vowel_groups += 1

            if vowel_groups == 5:
                longest = max(longest, index - start + 1)

        return longest
