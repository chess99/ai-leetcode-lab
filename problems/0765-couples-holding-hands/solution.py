# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        positions = [0] * len(row)
        for index, person in enumerate(row):
            positions[person] = index
        answer = 0
        for index in range(0, len(row), 2):
            partner = row[index] ^ 1
            if row[index + 1] == partner:
                continue
            partner_position = positions[partner]
            displaced = row[index + 1]
            row[index + 1], row[partner_position] = row[partner_position], row[index + 1]
            positions[partner] = index + 1
            positions[displaced] = partner_position
            answer += 1
        return answer
