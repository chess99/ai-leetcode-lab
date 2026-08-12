# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        modulus1, modulus2 = 1_000_000_007, 1_000_000_009
        base = 911382323
        prefix_hashes = [set() for _ in range(max(map(len, words)) + 1)]
        for word in words:
            first = second = 0
            for length, character in enumerate(word, 1):
                value = ord(character) - 96
                first = (first * base + value) % modulus1
                second = (second * base + value) % modulus2
                prefix_hashes[length].add((first, second))

        size = len(target)
        powers1 = [1] * (size + 1)
        powers2 = [1] * (size + 1)
        hash1 = [0] * (size + 1)
        hash2 = [0] * (size + 1)
        for index, character in enumerate(target):
            value = ord(character) - 96
            powers1[index + 1] = powers1[index] * base % modulus1
            powers2[index + 1] = powers2[index] * base % modulus2
            hash1[index + 1] = (hash1[index] * base + value) % modulus1
            hash2[index + 1] = (hash2[index] * base + value) % modulus2

        def substring_hash(left, length):
            right = left + length
            return ((hash1[right] - hash1[left] * powers1[length]) % modulus1,
                    (hash2[right] - hash2[left] * powers2[length]) % modulus2)

        longest = [0] * size
        maximum_word = len(prefix_hashes) - 1
        for index in range(size):
            low, high = 0, min(maximum_word, size - index)
            while low < high:
                middle = (low + high + 1) // 2
                if substring_hash(index, middle) in prefix_hashes[middle]:
                    low = middle
                else:
                    high = middle - 1
            longest[index] = low

        jumps = 0
        current_end = farthest = 0
        for index in range(len(target)):
            if index > farthest:
                return -1
            farthest = max(farthest, index + longest[index])
            if index == current_end:
                if farthest == current_end:
                    return -1
                jumps += 1
                current_end = farthest
                if current_end >= len(target):
                    return jumps
        return -1
