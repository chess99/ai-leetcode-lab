# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:08:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        longest_ending_at = [0] * 26
        current_length = 0

        for index, char in enumerate(s):
            if index and (ord(char) - ord(s[index - 1])) % 26 == 1:
                current_length += 1
            else:
                current_length = 1
            char_index = ord(char) - ord("a")
            longest_ending_at[char_index] = max(
                longest_ending_at[char_index], current_length
            )

        return sum(longest_ending_at)
