# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:24Z
# Experiment: ai-leetcode-lab, round 1
class Allocator:
    def __init__(self, n: int):
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        run = 0
        for i, owner in enumerate(self.memory):
            run = run + 1 if owner == 0 else 0
            if run == size:
                start = i - size + 1
                self.memory[start:i + 1] = [mID] * size
                return start
        return -1

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i, owner in enumerate(self.memory):
            if owner == mID:
                self.memory[i] = 0
                freed += 1
        return freed
