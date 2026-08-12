# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        from collections import deque
        positions=[deque() for _ in range(10)]
        for i,char in enumerate(s):positions[int(char)].append(i)
        for char in t:
            digit=int(char)
            if not positions[digit]:return False
            index=positions[digit][0]
            if any(positions[smaller] and positions[smaller][0]<index for smaller in range(digit)):return False
            positions[digit].popleft()
        return True
