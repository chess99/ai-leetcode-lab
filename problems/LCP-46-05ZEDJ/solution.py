# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def volunteerDeployment(self, finalCnt: List[int], totalNum: int, edges: List[List[int]], plans: List[List[int]]) -> List[int]:
        n = len(finalCnt) + 1
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        # 每个值表示为 coefficient * unknown + constant，unknown 是最终场馆 0 人数。
        expressions = [[1, 0]] + [[0, value] for value in finalCnt]
        for operation, index in reversed(plans):
            if operation == 1:
                expressions[index][0] *= 2
                expressions[index][1] *= 2
            elif operation == 2:
                for neighbor in graph[index]:
                    expressions[neighbor][0] -= expressions[index][0]
                    expressions[neighbor][1] -= expressions[index][1]
            else:
                for neighbor in graph[index]:
                    expressions[neighbor][0] += expressions[index][0]
                    expressions[neighbor][1] += expressions[index][1]

        coefficient = sum(item[0] for item in expressions)
        constant = sum(item[1] for item in expressions)
        unknown = (totalNum - constant) // coefficient
        return [a * unknown + b for a, b in expressions]
