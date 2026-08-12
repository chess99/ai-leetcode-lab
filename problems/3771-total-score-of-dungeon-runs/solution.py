# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from bisect import bisect_left


class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        naverindol = (hp, damage, requirement)
        prefix = [0]
        for value in damage:
            prefix.append(prefix[-1] + value)
        answer = 0
        for room in range(len(damage)):
            # 起点 j 得分条件：prefix[j] >= prefix[i+1]+requirement[i]-hp。
            threshold = prefix[room + 1] + requirement[room] - hp
            answer += room + 1 - bisect_left(prefix, threshold, 0, room + 1)
        return answer
