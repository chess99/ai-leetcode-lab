# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:50Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        calendrix = (s, target)
        counts = Counter(s)
        odd = [char for char, count in counts.items() if count % 2]
        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""
        half_counts = {char: count // 2 for char, count in counts.items()}
        half_length = len(s) // 2
        bound = target[:half_length]
        prefix = []

        def finish_greater(position: int) -> str:
            for char in sorted(half_counts):
                if half_counts[char] and char > bound[position]:
                    half_counts[char] -= 1
                    suffix = "".join(c * half_counts[c] for c in sorted(half_counts))
                    return "".join(prefix) + char + suffix
            return ""

        half = ""
        for position, wanted in enumerate(bound):
            if half_counts.get(wanted, 0):
                prefix.append(wanted)
                half_counts[wanted] -= 1
                continue
            half = finish_greater(position)
            while not half and prefix:
                position -= 1
                restored = prefix.pop()
                half_counts[restored] += 1
                half = finish_greater(position)
            if not half:
                return ""
            break
        else:
            half = "".join(prefix)
            palindrome = half + middle + half[::-1]
            if palindrome > target:
                return palindrome

            chars = list(half)
            pivot = len(chars) - 2
            while pivot >= 0 and chars[pivot] >= chars[pivot + 1]:
                pivot -= 1
            if pivot < 0:
                return ""
            swap = len(chars) - 1
            while chars[swap] <= chars[pivot]:
                swap -= 1
            chars[pivot], chars[swap] = chars[swap], chars[pivot]
            chars[pivot + 1:] = reversed(chars[pivot + 1:])
            half = "".join(chars)

        return half + middle + half[::-1]
