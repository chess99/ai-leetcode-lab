# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes); count = steps = 0
        for i, char in enumerate(boxes): answer[i] += steps; count += int(char); steps += count
        count = steps = 0
        for i in range(len(boxes)-1,-1,-1): answer[i] += steps; count += int(boxes[i]); steps += count
        return answer
