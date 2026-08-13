# AI solution attribution
# Initially created by: Codex Desktop / gpt-5.6-terra / medium / terra-medium
# Completed by: Codex Desktop / gpt-5.6-sol / high / sol-high
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial
from typing import List


class Solution:
    def treeOfInfiniteSouls(self, gem: List[int], p: int, target: int) -> int:
        n = len(gem)

        # chunks describe a tree serialization as
        # chunks[0], leaf_0, chunks[1], ..., leaf_(n-1), chunks[n].
        @lru_cache(None)
        def shapes(leaves: int):
            if leaves == 1:
                return (("1", "9"),)
            result = []
            for left_size in range(1, leaves):
                for left in shapes(left_size):
                    for right in shapes(leaves - left_size):
                        result.append(("1" + left[0],) + left[1:-1] +
                                      (left[-1] + right[0],) + right[1:-1] +
                                      (right[-1] + "9",))
            return tuple(result)

        # Modulo one accepts every labelled ordered full binary tree.
        if p == 1:
            catalan = factorial(2 * n - 2) // (factorial(n - 1) * factorial(n))
            return catalan * factorial(n)

        values = [value % p for value in gem]
        lengths = [len(str(value)) for value in gem]
        max_length = sum(lengths) + 4 * n - 2
        pow10 = [1] * (max_length + 1)
        for i in range(1, max_length + 1):
            pow10[i] = pow10[i - 1] * 10 % p

        split = n // 2
        all_mask = (1 << n) - 1
        answer = 0

        for raw_chunks in shapes(n):
            chunk_values = [int(chunk) % p if chunk else 0 for chunk in raw_chunks]
            chunk_lengths = [len(chunk) for chunk in raw_chunks]

            for chosen in combinations(range(n), split):
                chosen_mask = sum(1 << i for i in chosen)
                other = tuple(i for i in range(n) if not (chosen_mask >> i) & 1)

                suffix_length = (sum(lengths[i] for i in other) +
                                 sum(chunk_lengths[split + 1:]))
                shift = pow10[suffix_length]

                suffix_counts = Counter()
                for order in permutations(other):
                    rem = 0
                    for slot, index in enumerate(order, split):
                        rem = (rem * pow10[lengths[index]] + values[index]) % p
                        clen = chunk_lengths[slot + 1]
                        rem = (rem * pow10[clen] + chunk_values[slot + 1]) % p
                    suffix_counts[rem] += 1

                for order in permutations(chosen):
                    rem = chunk_values[0]
                    for slot, index in enumerate(order):
                        rem = (rem * pow10[lengths[index]] + values[index]) % p
                        clen = chunk_lengths[slot + 1]
                        rem = (rem * pow10[clen] + chunk_values[slot + 1]) % p
                    need = (target - rem * shift) % p
                    answer += suffix_counts.get(need, 0)

        return answer
