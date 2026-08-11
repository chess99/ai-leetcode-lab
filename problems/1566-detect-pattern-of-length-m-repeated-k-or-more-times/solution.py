# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:08:38Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        return any(all(arr[i + j] == arr[i + j - m] for j in range(m, m * k)) for i in range(len(arr) - m * k + 1))
