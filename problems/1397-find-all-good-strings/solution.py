# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:53Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        modulus = 1_000_000_007
        failure = [0] * len(evil)
        for index in range(1, len(evil)):
            matched = failure[index - 1]
            while matched and evil[index] != evil[matched]:
                matched = failure[matched - 1]
            if evil[index] == evil[matched]:
                matched += 1
            failure[index] = matched

        @lru_cache(None)
        def count(index, matched, lower_tight, upper_tight):
            if matched == len(evil):
                return 0
            if index == n:
                return 1
            low = s1[index] if lower_tight else 'a'
            high = s2[index] if upper_tight else 'z'
            answer = 0
            for code in range(ord(low), ord(high) + 1):
                char = chr(code)
                following = matched
                while following and evil[following] != char:
                    following = failure[following - 1]
                if evil[following] == char:
                    following += 1
                answer += count(index + 1, following,
                                lower_tight and char == low,
                                upper_tight and char == high)
            return answer % modulus

        return count(0, 0, True, True)
