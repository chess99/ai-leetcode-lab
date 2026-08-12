# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:56Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        modulus = 1_000_000_007
        prime = set("2357")
        size = len(s)
        if (s[0] not in prime or s[-1] in prime
                or k * minLength > size):
            return 0

        previous = [0] * (size + 1)
        previous[0] = 1
        for part in range(1, k + 1):
            current = [0] * (size + 1)
            accumulated = 0
            minimum_end = part * minLength
            maximum_end = size - (k - part) * minLength
            for end in range(minimum_end, maximum_end + 1):
                start = end - minLength
                if (start == 0 or
                        (s[start - 1] not in prime and s[start] in prime)):
                    accumulated = (accumulated + previous[start]) % modulus
                if end == size or (s[end - 1] not in prime and s[end] in prime):
                    current[end] = accumulated
            previous = current
        return previous[size]
