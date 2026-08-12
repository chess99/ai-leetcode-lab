# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:48Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def trafficCommand(self, directions: List[str]) -> int:
        names = "ESWN"
        size, lane = 10, 3
        entry = {"E": (size, lane), "S": (lane, -size), "W": (-size, -lane), "N": (-lane, size)}
        exit_point = {"E": (size, -lane), "S": (-lane, -size), "W": (-size, lane), "N": (lane, size)}

        def orientation(first, second, third):
            return (second[0] - first[0]) * (third[1] - first[1]) - (
                second[1] - first[1]
            ) * (third[0] - first[0])

        def intersects(first_start, first_end, second_start, second_end):
            first_a = orientation(first_start, first_end, second_start)
            first_b = orientation(first_start, first_end, second_end)
            second_a = orientation(second_start, second_end, first_start)
            second_b = orientation(second_start, second_end, first_end)
            return (first_a == 0 or first_b == 0 or (first_a < 0) != (first_b < 0)) and (
                second_a == 0 or second_b == 0 or (second_a < 0) != (second_b < 0)
            )

        goal = tuple(map(len, directions))
        start = (0, 0, 0, 0)
        queue = deque([start])
        distance = {start: 0}
        while queue:
            state = queue.popleft()
            if state == goal:
                return distance[state]
            available = [lane_index for lane_index in range(4) if state[lane_index] < goal[lane_index]]
            for subset in range(1, 1 << len(available)):
                moving = [available[index] for index in range(len(available)) if subset >> index & 1]
                destinations = [directions[lane_index][state[lane_index]] for lane_index in moving]
                if len(destinations) != len(set(destinations)):
                    continue
                valid = True
                for first in range(len(moving)):
                    for second in range(first):
                        if intersects(
                            entry[names[moving[first]]],
                            exit_point[destinations[first]],
                            entry[names[moving[second]]],
                            exit_point[destinations[second]],
                        ):
                            valid = False
                            break
                    if not valid:
                        break
                if not valid:
                    continue
                next_state = list(state)
                for lane_index in moving:
                    next_state[lane_index] += 1
                next_state = tuple(next_state)
                if next_state not in distance:
                    distance[next_state] = distance[state] + 1
                    queue.append(next_state)
        raise RuntimeError("unreachable traffic state")
