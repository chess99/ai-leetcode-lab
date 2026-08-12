# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        rolling_hash = 0
        power_k = pow(power, k, modulo)
        answer = 0
        for index in range(len(s) - 1, -1, -1):
            rolling_hash = (rolling_hash * power + ord(s[index]) - 96) % modulo
            if index + k < len(s):
                removed = (ord(s[index + k]) - 96) * power_k
                rolling_hash = (rolling_hash - removed) % modulo
            if index + k <= len(s) and rolling_hash == hashValue:
                answer = index
        return s[answer:answer + k]
