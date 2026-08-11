# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:24:05Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right


class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.history[index][-1][0] == self.snap_id:
            self.history[index][-1] = (self.snap_id, val)
        else:
            self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        current = self.snap_id
        self.snap_id += 1
        return current

    def get(self, index: int, snap_id: int) -> int:
        changes = self.history[index]
        position = bisect_right(changes, (snap_id, float("inf"))) - 1
        return changes[position][1]
