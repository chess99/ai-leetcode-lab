# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        size = len(t)
        suffix = [-1] * size + [len(s)]
        index = len(s) - 1
        for target in range(size - 1, -1, -1):
            while index >= 0 and s[index] != t[target]:
                index -= 1
            if index < 0:
                break
            suffix[target] = index
            index -= 1

        answer = size
        left_position = -1
        right_start = 0
        for prefix_length in range(size + 1):
            if prefix_length:
                left_position += 1
                while left_position < len(s) and s[left_position] != t[prefix_length - 1]:
                    left_position += 1
                if left_position == len(s):
                    break
            right_start = max(right_start, prefix_length)
            while (right_start < size
                   and (suffix[right_start] == -1
                        or suffix[right_start] <= left_position)):
                right_start += 1
            answer = min(answer, right_start - prefix_length)
        return answer
