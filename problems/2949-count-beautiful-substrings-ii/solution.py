# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:49Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        length_modulus = 1
        while (length_modulus // 2) ** 2 % k != 0 or length_modulus % 2:
            length_modulus += 1
        frequencies = Counter({(0, 0): 1})
        balance = 0
        answer = 0
        vowels = set("aeiou")
        for index, character in enumerate(s, 1):
            balance += 1 if character in vowels else -1
            key = (balance, index % length_modulus)
            answer += frequencies[key]
            frequencies[key] += 1
        return answer
