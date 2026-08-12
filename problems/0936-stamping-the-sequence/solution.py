# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:03Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_length, target_length = len(stamp), len(target)
        windows = []
        queue = deque()
        erased = [False] * target_length
        answer = []

        for start in range(target_length - stamp_length + 1):
            matched, mismatched = set(), set()
            for offset, char in enumerate(stamp):
                position = start + offset
                if target[position] == char:
                    matched.add(position)
                else:
                    mismatched.add(position)
            windows.append((matched, mismatched))
            if not mismatched:
                answer.append(start)
                for position in matched:
                    if not erased[position]:
                        erased[position] = True
                        queue.append(position)

        while queue:
            position = queue.popleft()
            first = max(0, position - stamp_length + 1)
            last = min(target_length - stamp_length, position)
            for start in range(first, last + 1):
                matched, mismatched = windows[start]
                if position not in mismatched:
                    continue
                mismatched.remove(position)
                if not mismatched:
                    answer.append(start)
                    for following in matched:
                        if not erased[following]:
                            erased[following] = True
                            queue.append(following)

        return answer[::-1] if all(erased) else []
