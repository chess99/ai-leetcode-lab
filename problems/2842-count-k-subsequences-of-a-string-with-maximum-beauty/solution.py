# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:43Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from math import comb


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        modulus = 1_000_000_007
        frequencies = sorted(Counter(s).values(), reverse=True)
        if len(frequencies) < k:
            return 0
        threshold = frequencies[k - 1]
        greater = sum(value > threshold for value in frequencies)
        equal = frequencies.count(threshold)
        answer = 1
        for value in frequencies[:greater]:
            answer = answer * value % modulus
        needed = k - greater
        answer = answer * pow(threshold, needed, modulus) % modulus
        return answer * comb(equal, needed) % modulus
