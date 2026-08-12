# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
        def digit_sum(x): return sum(map(int, str(x)))
        stack, seen = [(0, 0)], set()
        while stack:
            r, c = stack.pop()
            if r >= m or c >= n or (r, c) in seen or digit_sum(r) + digit_sum(c) > cnt: continue
            seen.add((r, c)); stack.extend(((r + 1, c), (r, c + 1)))
        return len(seen)
