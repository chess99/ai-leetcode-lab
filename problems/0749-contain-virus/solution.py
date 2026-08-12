# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        rows, columns = len(isInfected), len(isInfected[0])
        answer = 0
        while True:
            visited = set()
            regions, frontiers, walls = [], [], []
            for row in range(rows):
                for column in range(columns):
                    if isInfected[row][column] != 1 or (row, column) in visited:
                        continue
                    region, frontier, needed = set(), set(), 0
                    stack = [(row, column)]
                    visited.add((row, column))
                    while stack:
                        current_row, current_column = stack.pop()
                        region.add((current_row, current_column))
                        for next_row, next_column in ((current_row-1,current_column),
                                                      (current_row+1,current_column),
                                                      (current_row,current_column-1),
                                                      (current_row,current_column+1)):
                            if not (0 <= next_row < rows and 0 <= next_column < columns):
                                continue
                            if isInfected[next_row][next_column] == 0:
                                frontier.add((next_row, next_column))
                                needed += 1
                            elif (isInfected[next_row][next_column] == 1 and
                                  (next_row, next_column) not in visited):
                                visited.add((next_row, next_column))
                                stack.append((next_row, next_column))
                    regions.append(region)
                    frontiers.append(frontier)
                    walls.append(needed)
            if not regions:
                return answer
            quarantine = max(range(len(regions)), key=lambda index: len(frontiers[index]))
            if not frontiers[quarantine]:
                return answer
            answer += walls[quarantine]
            for row, column in regions[quarantine]:
                isInfected[row][column] = -1
            for index, frontier in enumerate(frontiers):
                if index != quarantine:
                    for row, column in frontier:
                        isInfected[row][column] = 1
