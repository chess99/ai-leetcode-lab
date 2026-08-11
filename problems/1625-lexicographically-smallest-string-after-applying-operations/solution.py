# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:25Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue = deque([s]); seen = {s}; best = s
        while queue:
            current = queue.popleft(); best = min(best, current)
            changed = ''.join(str((int(char) + a) % 10) if i % 2 else char for i, char in enumerate(current))
            rotated = current[-b:] + current[:-b]
            for candidate in (changed, rotated):
                if candidate not in seen: seen.add(candidate); queue.append(candidate)
        return best
