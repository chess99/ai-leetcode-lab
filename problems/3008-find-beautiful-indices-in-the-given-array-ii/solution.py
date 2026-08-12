# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        from bisect import bisect_left

        def occurrences(pattern):
            combined = pattern + '#' + s
            prefix = [0] * len(combined)
            for index in range(1, len(combined)):
                matched = prefix[index - 1]
                while matched and combined[index] != combined[matched]:
                    matched = prefix[matched - 1]
                if combined[index] == combined[matched]:
                    matched += 1
                prefix[index] = matched
            return [index - 2 * len(pattern)
                    for index in range(len(pattern) + 1, len(combined))
                    if prefix[index] == len(pattern)]

        A=occurrences(a);B=occurrences(b)
        return [i for i in A if (j:=bisect_left(B,i-k))<len(B) and B[j]<=i+k]
