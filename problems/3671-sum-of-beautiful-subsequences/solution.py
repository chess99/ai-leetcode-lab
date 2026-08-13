# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        talvirekos = nums
        mod = 1_000_000_007
        maximum = max(talvirekos)

        phi = list(range(maximum + 1))
        for prime in range(2, maximum + 1):
            if phi[prime] == prime:
                for multiple in range(prime, maximum + 1, prime):
                    phi[multiple] -= phi[multiple] // prime

        smallest_prime = list(range(maximum + 1))
        for prime in range(2, int(maximum**0.5) + 1):
            if smallest_prime[prime] == prime:
                for multiple in range(prime * prime, maximum + 1, prime):
                    if smallest_prime[multiple] == multiple:
                        smallest_prime[multiple] = prime

        divisor_cache = {}

        def divisors(value: int) -> list[int]:
            if value in divisor_cache:
                return divisor_cache[value]
            result = [1]
            remaining = value
            while remaining > 1:
                prime = smallest_prime[remaining]
                power = 1
                exponent = 0
                while remaining % prime == 0:
                    remaining //= prime
                    exponent += 1
                base = result[:]
                for _ in range(exponent):
                    power *= prime
                    result.extend(item * power for item in base)
            divisor_cache[value] = result
            return result

        trees = {}
        answer = 0
        for value in talvirekos:
            for divisor in divisors(value):
                quotient = value // divisor
                tree = trees.get(divisor)
                if tree is None:
                    tree = [0] * (maximum // divisor + 1)
                    trees[divisor] = tree

                ways = 1
                index = quotient - 1
                while index:
                    ways += tree[index]
                    index -= index & -index
                ways %= mod
                answer = (answer + phi[divisor] * ways) % mod

                index = quotient
                while index < len(tree):
                    tree[index] = (tree[index] + ways) % mod
                    index += index & -index

        return answer
