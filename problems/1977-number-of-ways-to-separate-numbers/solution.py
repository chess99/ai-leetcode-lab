# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:03Z
# Experiment: ai-leetcode-lab, round 1
from array import array


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num[0] == '0':
            return 0

        size = len(num)
        modulus = 1_000_000_007

        # Only i < j is queried.  Each row stores values by the offset j - i,
        # and unsigned shorts are sufficient because every LCP is at most 3500.
        lcp = [None] * (size + 1)
        lcp[size] = array('H', [0])
        for first in range(size - 1, -1, -1):
            row = array('H', [0]) * (size - first + 1)
            next_row = lcp[first + 1]
            character = num[first]
            for second in range(size - 1, first, -1):
                if character == num[second]:
                    offset = second - first
                    row[offset] = next_row[offset] + 1
            lcp[first] = row

        # prefix[end][length] is the number of splits of num[:end] whose last
        # number has length at most length.  Storing just this prefix table also
        # lets us recover an exact-length DP value by subtracting neighbors.
        prefix = [array('I', [0]) * (end + 1)
                  for end in range(size + 1)]
        for end in range(1, size + 1):
            row = prefix[end]
            for length in range(1, end + 1):
                start = end - length
                value = 0
                if num[start] != '0':
                    if start == 0:
                        value = 1
                    else:
                        value = prefix[start][min(length - 1, start)]
                        if start >= length:
                            previous_start = start - length
                            common = lcp[previous_start][length]
                            if (common >= length or
                                    num[previous_start + common]
                                    <= num[start + common]):
                                same_length = (prefix[start][length]
                                               - prefix[start][length - 1])
                                value += same_length
                row[length] = (row[length - 1] + value) % modulus

        return prefix[size][size]
