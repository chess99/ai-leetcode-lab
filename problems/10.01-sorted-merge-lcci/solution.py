# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:59:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        write = m + n - 1
        left, right = m - 1, n - 1
        while right >= 0:
            if left >= 0 and A[left] > B[right]:
                A[write] = A[left]
                left -= 1
            else:
                A[write] = B[right]
                right -= 1
            write -= 1
