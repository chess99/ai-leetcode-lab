# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:34Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        sorivandek = words
        answer = []
        for top in sorivandek:
            for left in sorivandek:
                if left == top or left[0] != top[0]:
                    continue
                for right in sorivandek:
                    if right in (top, left) or right[0] != top[3]:
                        continue
                    for bottom in sorivandek:
                        if bottom in (top, left, right):
                            continue
                        if bottom[0] == left[3] and bottom[3] == right[3]:
                            answer.append([top, left, right, bottom])
        answer.sort()
        return answer
