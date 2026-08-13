# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
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

        def encode(counts: tuple[int, ...]) -> int:
            return sum(value * multipliers[i] for i, value in enumerate(counts))

        options_per_word = []
        for word in words:
            length = len(word)
            deletion_cost = [10**9] * (1 << length)
            deletion_cost[0] = 0
            for mask in range(1 << length):
                removed = mask.bit_count()
                for i, letter in enumerate(word):
                    if not (mask >> i & 1):
                        cost = (i - (mask & ((1 << i) - 1)).bit_count()) * (length - removed - 1 - ((mask >> (i + 1)).bit_count()))
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
                    options[key] = min(options.get(key, 10**9), cost)
            options_per_word.append(list(options.items()))

        dp = [10**9] * states
        dp[0] = 0
        for options in options_per_word:
            next_dp = dp[:]
            for state, current in enumerate(dp):
                if current == 10**9:
                    continue
                existing = []
                code = state
                for limit in limits:
                    existing.append(code % (limit + 1))
                    code //= limit + 1
                for added, cost in options:
                    total = tuple(existing[i] + added[i] for i in range(len(letters)))
                    if all(total[i] <= limits[i] for i in range(len(letters))):
                        target = encode(total)
                        next_dp[target] = min(next_dp[target], current + cost)
            dp = next_dp
        result = dp[encode(limits)]
        return -1 if result == 10**9 else result
