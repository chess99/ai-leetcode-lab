# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countPalindromes(self, s: str) -> int:
        modulus = 10 ** 9 + 7
        right_single = [0] * 10
        right_pair = [[0] * 10 for _ in range(10)]
        for character in reversed(s):
            digit = ord(character) - 48
            for second in range(10):
                right_pair[digit][second] += right_single[second]
            right_single[digit] += 1

        left_single = [0] * 10
        left_pair = [[0] * 10 for _ in range(10)]
        answer = 0
        for character in s:
            digit = ord(character) - 48
            right_single[digit] -= 1
            for second in range(10):
                right_pair[digit][second] -= right_single[second]
            for first in range(10):
                for second in range(10):
                    answer += left_pair[first][second] * right_pair[second][first]
            for first in range(10):
                left_pair[first][digit] += left_single[first]
            left_single[digit] += 1
        return answer % modulus
