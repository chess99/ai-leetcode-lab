# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        morindale = mat
        mod = 1_000_000_007
        maximum = max(map(max, morindale))
        mobius = [1] * (maximum + 1)
        is_prime = [True] * (maximum + 1)
        primes = []
        mobius[0] = 0
        for value in range(2, maximum + 1):
            if is_prime[value]:
                primes.append(value)
                mobius[value] = -1
            for prime in primes:
                product = value * prime
                if product > maximum:
                    break
                is_prime[product] = False
                if value % prime == 0:
                    mobius[product] = 0
                    break
                mobius[product] = -mobius[value]

        answer = 0
        for divisor in range(1, maximum + 1):
            if mobius[divisor] == 0:
                continue
            ways = 1
            for row in mat:
                count = sum(value % divisor == 0 for value in row)
                ways = ways * count % mod
                if ways == 0:
                    break
            answer = (answer + mobius[divisor] * ways) % mod
        return answer
