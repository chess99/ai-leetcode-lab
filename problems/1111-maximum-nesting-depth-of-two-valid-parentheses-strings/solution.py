# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        answer = []
        depth = 0
        for character in seq:
            if character == "(":
                answer.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                answer.append(depth % 2)
        return answer
