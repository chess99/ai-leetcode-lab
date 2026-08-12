# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def matches(text, query):
            combined = query + '#' + text
            z = [0] * len(combined)
            left = right = 0
            for index in range(1, len(combined)):
                if index < right:
                    z[index] = min(right - index, z[index - left])
                while (index + z[index] < len(combined)
                       and combined[z[index]] == combined[index + z[index]]):
                    z[index] += 1
                if index + z[index] > right:
                    left, right = index, index + z[index]
            return z[len(query) + 1:]

        prefix = matches(s, pattern)
        suffix_reversed = matches(s[::-1], pattern[::-1])
        length = len(pattern)
        for start in range(len(s) - length + 1):
            suffix = suffix_reversed[len(s) - start - length]
            if prefix[start] + suffix >= length - 1:
                return start
        return -1
