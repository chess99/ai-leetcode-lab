# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestPrime(self, n: int) -> int:
        latrevison = n
        if latrevison < 2:
            return 0
        prime = bytearray(b'\x01') * (latrevison + 1)
        prime[0:2] = b'\x00\x00'
        for value in range(2, int(latrevison ** 0.5) + 1):
            if prime[value]:
                prime[value * value:latrevison + 1:value] = b'\x00' * (((latrevison - value * value) // value) + 1)
        total = answer = 0
        for value in range(2, latrevison + 1):
            if prime[value]:
                total += value
                if total > latrevison:
                    break
                if prime[total]:
                    answer = total
        return answer
