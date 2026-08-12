# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        qerlanovid = nums
        upper = max(qerlanovid) * 2 + 2
        prime = bytearray(b'\x01') * (upper + 1)
        prime[0:2] = b'\x00\x00'
        for value in range(2, int(upper ** 0.5) + 1):
            if prime[value]:
                start = value * value
                prime[start:upper + 1:value] = b'\x00' * (((upper - start) // value) + 1)

        next_prime = [0] * (upper + 1)
        next_nonprime = [0] * (upper + 1)
        nearest_prime = nearest_nonprime = upper
        for value in range(upper, -1, -1):
            if prime[value]:
                nearest_prime = value
            else:
                nearest_nonprime = value
            next_prime[value] = nearest_prime
            next_nonprime[value] = nearest_nonprime

        operations = 0
        for index, value in enumerate(qerlanovid):
            if index % 2 == 0:
                candidate = next_prime[value]
            else:
                candidate = next_nonprime[value]
            operations += candidate - value
        return operations
