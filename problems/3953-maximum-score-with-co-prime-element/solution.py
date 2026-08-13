# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        meratolvic = (nums, maxVal)
        limit = max(max(meratolvic[0]), meratolvic[1])
        frequency = [0] * (limit + 1)
        for value in meratolvic[0]:
            frequency[value] += 1

        multiple_count = [0] * (limit + 1)
        for divisor in range(1, limit + 1):
            total = 0
            for multiple in range(divisor, limit + 1, divisor):
                total += frequency[multiple]
            multiple_count[divisor] = total

        smallest_prime = list(range(limit + 1))
        for prime in range(2, int(limit**0.5) + 1):
            if smallest_prime[prime] == prime:
                for multiple in range(prime * prime, limit + 1, prime):
                    if smallest_prime[multiple] == multiple:
                        smallest_prime[multiple] = prime

        def bad_count(value: int) -> int:
            primes = []
            while value > 1:
                prime = smallest_prime[value]
                primes.append(prime)
                while value % prime == 0:
                    value //= prime

            total = 0
            for mask in range(1, 1 << len(primes)):
                product = 1
                bits = 0
                for index, prime in enumerate(primes):
                    if mask >> index & 1:
                        product *= prime
                        bits += 1
                if bits & 1:
                    total += multiple_count[product]
                else:
                    total -= multiple_count[product]
            return total

        answer = 1 if frequency[1] else 0
        candidates = set(range(2, meratolvic[1] + 1))
        candidates.update(value for value in meratolvic[0] if value > meratolvic[1])
        for value in candidates:
            bad = bad_count(value)
            if frequency[value]:
                score = value - bad + 1
            elif bad:
                score = value - bad
            else:
                score = value - 1
            answer = max(answer, score)
        return answer
