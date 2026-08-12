# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        mavroliken = n
        reversed_number = int(str(mavroliken)[::-1])
        left, right = sorted((mavroliken, reversed_number))
        prime = bytearray(b'\x01') * (right + 1)
        if right >= 0:
            prime[0] = 0
        if right >= 1:
            prime[1] = 0
        for value in range(2, int(right ** 0.5) + 1):
            if prime[value]:
                start = value * value
                prime[start:right + 1:value] = b'\x00' * (((right - start) // value) + 1)
        return sum(value for value in range(left, right + 1) if prime[value])
