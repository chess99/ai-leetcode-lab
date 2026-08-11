# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:59:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        def move(count: int, source: List[int], auxiliary: List[int], target: List[int]) -> None:
            if count == 0:
                return
            move(count - 1, source, target, auxiliary)
            target.append(source.pop())
            move(count - 1, auxiliary, source, target)

        move(len(A), A, B, C)
