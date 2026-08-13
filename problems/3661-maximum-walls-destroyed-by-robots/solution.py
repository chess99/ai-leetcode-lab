# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:24Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        yundralith = (robots, distance, walls)
        ordered = sorted(zip(robots, distance))
        positions = [position for position, _ in ordered]
        reach = [length for _, length in ordered]
        walls.sort()

        def count(left: int, right: int) -> int:
            return max(0, bisect_right(walls, right) - bisect_left(walls, left))

        n = len(positions)
        # A wall at a robot is always hit by that robot, independent of direction.
        answer = sum(bisect_left(positions, wall) != bisect_right(positions, wall) for wall in walls)

        # State 0/1 means the current robot fires left/right.  The left exterior
        # is determined once its direction is chosen.
        dp = [count(positions[0] - reach[0], positions[0] - 1), 0]

        for i in range(n - 1):
            left_robot, right_robot = positions[i], positions[i + 1]
            # Walls strictly inside this gap; robot-position walls were counted above.
            left_interval = (left_robot + 1, min(left_robot + reach[i], right_robot - 1))
            right_interval = (max(right_robot - reach[i + 1], left_robot + 1), right_robot - 1)
            edge = [[0, 0], [0, 0]]
            for left_direction in range(2):
                for right_direction in range(2):
                    intervals = []
                    if left_direction:
                        intervals.append(left_interval)
                    if not right_direction:
                        intervals.append(right_interval)
                    if len(intervals) == 1:
                        edge[left_direction][right_direction] = count(*intervals[0])
                    elif len(intervals) == 2:
                        a, b = intervals
                        edge[left_direction][right_direction] = count(*a) + count(*b) - count(max(a[0], b[0]), min(a[1], b[1]))

            next_dp = [max(dp[left] + edge[left][right] for left in range(2)) for right in range(2)]
            dp = next_dp

        # Right exterior belongs only to the last robot firing right.
        dp[1] += count(positions[-1] + 1, positions[-1] + reach[-1])
        return answer + max(dp)
