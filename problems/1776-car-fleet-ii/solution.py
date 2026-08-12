# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        answer = [-1.0] * len(cars)
        stack = []
        for index in range(len(cars) - 1, -1, -1):
            position, speed = cars[index]
            while stack:
                following = stack[-1]
                next_position, next_speed = cars[following]
                if speed <= next_speed:
                    stack.pop()
                    continue
                collision = (next_position - position) / (speed - next_speed)
                if answer[following] < 0 or collision <= answer[following]:
                    answer[index] = collision
                    break
                stack.pop()
            stack.append(index)
        return answer
