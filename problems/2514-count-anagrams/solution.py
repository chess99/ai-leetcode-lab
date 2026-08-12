# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:31Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def countAnagrams(self, s: str) -> int:
        modulus = 10 ** 9 + 7
        maximum = max(map(len, s.split()))
        factorial = [1] * (maximum + 1)
        for value in range(1, maximum + 1):
            factorial[value] = factorial[value - 1] * value % modulus
        answer = 1
        for word in s.split():
            ways = factorial[len(word)]
            for count in Counter(word).values():
                ways = ways * pow(factorial[count], modulus - 2, modulus) % modulus
            answer = answer * ways % modulus
        return answer
