# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:19:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0: return [0] * n
        step = 1 if k > 0 else -1
        return [sum(code[(i + step * j) % n] for j in range(1, abs(k) + 1)) for i in range(n)]
