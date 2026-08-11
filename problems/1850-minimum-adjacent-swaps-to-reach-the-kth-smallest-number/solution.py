# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        target = list(num)
        def next_permutation():
            i = len(target) - 2
            while target[i] >= target[i + 1]: i -= 1
            j = len(target) - 1
            while target[j] <= target[i]: j -= 1
            target[i], target[j] = target[j], target[i]
            target[i + 1:] = reversed(target[i + 1:])
        for _ in range(k): next_permutation()
        current = list(num); answer = 0
        for i, value in enumerate(target):
            j = i
            while current[j] != value: j += 1
            while j > i:
                current[j], current[j - 1] = current[j - 1], current[j]
                answer += 1; j -= 1
        return answer
