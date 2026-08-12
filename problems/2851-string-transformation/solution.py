# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        modulus = 1_000_000_007
        size = len(s)
        prefix = [0] * len(t)
        for index in range(1, len(t)):
            matched = prefix[index - 1]
            while matched and t[index] != t[matched]:
                matched = prefix[matched - 1]
            if t[index] == t[matched]:
                matched += 1
            prefix[index] = matched
        matches = 0
        matched = 0
        for character in (s + s)[:-1]:
            while matched and character != t[matched]:
                matched = prefix[matched - 1]
            if character == t[matched]:
                matched += 1
            if matched == size:
                matches += 1
                matched = prefix[matched - 1]
        if matches == 0:
            return 0

        def multiply(first, second):
            return [[sum(first[i][p] * second[p][j] for p in range(2)) % modulus
                     for j in range(2)] for i in range(2)]

        transition = [[matches - 1, matches],
                      [size - matches, size - matches - 1]]
        # Columns are source states: equal-to-t and different-from-t rotations.
        result = [[1, 0], [0, 1]]
        while k:
            if k & 1:
                result = multiply(result, transition)
            transition = multiply(transition, transition)
            k //= 2
        source = 0 if s == t else 1
        return result[0][source]
