# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        count = len(students)
        compatibility = [
            [sum(answer_a == answer_b for answer_a, answer_b in zip(student, mentor)) for mentor in mentors]
            for student in students
        ]
        best_for_mask = [0] * (1 << count)

        for mask in range(1 << count):
            student_index = mask.bit_count()
            if student_index == count:
                continue
            for mentor_index in range(count):
                if not (mask & (1 << mentor_index)):
                    next_mask = mask | (1 << mentor_index)
                    best_for_mask[next_mask] = max(
                        best_for_mask[next_mask],
                        best_for_mask[mask] + compatibility[student_index][mentor_index],
                    )

        return best_for_mask[-1]
