# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:44Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, bisect_right


class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        first, middle, last = p.split('*')
        n = len(s)

        def occurrences(pattern: str) -> list[int]:
            if not pattern:
                return list(range(n + 1))
            prefix = [0] * len(pattern)
            for i in range(1, len(pattern)):
                border = prefix[i - 1]
                while border and pattern[i] != pattern[border]:
                    border = prefix[border - 1]
                if pattern[i] == pattern[border]:
                    border += 1
                prefix[i] = border
            answer = []
            matched = 0
            for i, char in enumerate(s):
                while matched and char != pattern[matched]:
                    matched = prefix[matched - 1]
                if char == pattern[matched]:
                    matched += 1
                if matched == len(pattern):
                    answer.append(i - len(pattern) + 1)
                    matched = prefix[matched - 1]
            return answer

        first_occ = occurrences(first)
        middle_occ = occurrences(middle)
        last_occ = occurrences(last)
        answer = n + 1
        for middle_start in middle_occ:
            first_index = bisect_right(first_occ, middle_start - len(first)) - 1
            last_index = bisect_left(last_occ, middle_start + len(middle))
            if first_index >= 0 and last_index < len(last_occ):
                start = first_occ[first_index]
                end = last_occ[last_index] + len(last)
                answer = min(answer, end - start)
        return -1 if answer > n else answer
