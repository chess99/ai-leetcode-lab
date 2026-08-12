# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:53Z
# Experiment: ai-leetcode-lab, round 1
from array import array


class Solution:
    def deleteString(self, s: str) -> int:
        size = len(s)
        longest_common_prefix = [None] * (size + 1)
        longest_common_prefix[size] = array('H', [0])
        dynamic = [1] * size
        for first in range(size - 1, -1, -1):
            row = array('H', [0]) * (size - first + 1)
            next_row = longest_common_prefix[first + 1]
            for second in range(first + 1, size):
                if s[first] == s[second]:
                    offset = second - first
                    row[offset] = next_row[offset] + 1
            longest_common_prefix[first] = row
            for length in range(1, (size - first) // 2 + 1):
                if row[length] >= length:
                    dynamic[first] = max(dynamic[first], 1 + dynamic[first + length])
        return dynamic[0]
