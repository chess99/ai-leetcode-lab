# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
# Handoff: terra-medium -> sol-medium
# The original implementation and attribution above are preserved.  The
# sol-medium pass fixes the per-removal right-side cardinality calculation.
from typing import List


class Solution:
    def Leetcode(self, words: List[str]) -> int:
        needed = {'h': 1, 'e': 4, 'l': 3, 'o': 2, 't': 1, 'c': 1, 'd': 1}
        letters = tuple(needed)
        letter_index = {letter: index for index, letter in enumerate(letters)}
        limits = tuple(needed[letter] for letter in letters)
        multipliers = [1]
        for limit in limits:
            multipliers.append(multipliers[-1] * (limit + 1))
        states = multipliers[-1]
        infinity = 10**9

        def encode(counts: tuple[int, ...]) -> int:
            return sum(value * multipliers[i] for i, value in enumerate(counts))

        state_counts = []
        for state in range(states):
            counts = []
            code = state
            for limit in limits:
                counts.append(code % (limit + 1))
                code //= limit + 1
            state_counts.append(tuple(counts))

        options_per_word = []
        for word in words:
            length = len(word)
            deletion_cost = [infinity] * (1 << length)
            deletion_cost[0] = 0
            for mask in range(1 << length):
                removed = mask.bit_count()
                for i, letter in enumerate(word):
                    if not (mask >> i & 1):
                        removed_left = (mask & ((1 << i) - 1)).bit_count()
                        removed_right = (mask >> (i + 1)).bit_count()
                        remaining_left = i - removed_left
                        remaining_right = length - 1 - i - removed_right
                        cost = remaining_left * remaining_right
                        next_mask = mask | (1 << i)
                        deletion_cost[next_mask] = min(deletion_cost[next_mask], deletion_cost[mask] + cost)
            options = {}
            for mask, cost in enumerate(deletion_cost):
                counts = [0] * len(letters)
                valid = True
                for i, letter in enumerate(word):
                    if mask >> i & 1:
                        if letter not in letter_index:
                            valid = False
                            break
                        counts[letter_index[letter]] += 1
                key = tuple(counts)
                if valid and all(key[i] <= limits[i] for i in range(len(letters))):
                    options[key] = min(options.get(key, infinity), cost)
            options_per_word.append(
                [(encode(counts), cost, counts) for counts, cost in options.items()]
            )

        dp = [infinity] * states
        dp[0] = 0
        compatible_sources = {}
        for options in options_per_word:
            next_dp = dp[:]
            for added_code, cost, added in options:
                if added_code == 0:
                    continue
                sources = compatible_sources.get(added)
                if sources is None:
                    sources = [
                        state
                        for state, existing in enumerate(state_counts)
                        if all(existing[i] + added[i] <= limits[i] for i in range(len(letters)))
                    ]
                    compatible_sources[added] = sources
                for state in sources:
                    current = dp[state]
                    if current != infinity:
                        target = state + added_code
                        candidate = current + cost
                        if candidate < next_dp[target]:
                            next_dp[target] = candidate
            dp = next_dp
            if dp[-1] == 0:
                return 0
        result = dp[encode(limits)]
        return -1 if result == infinity else result
