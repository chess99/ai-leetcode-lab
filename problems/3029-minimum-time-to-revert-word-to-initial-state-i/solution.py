# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        for seconds in range(1, (len(word) + k - 1) // k + 1):
            removed = seconds * k
            if removed >= len(word) or word.startswith(word[removed:]):
                return seconds
        return 0
