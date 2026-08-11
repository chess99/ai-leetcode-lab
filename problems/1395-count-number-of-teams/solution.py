# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        for middle in range(1, len(rating) - 1):
            left_smaller = sum(value < rating[middle] for value in rating[:middle])
            left_larger = middle - left_smaller
            right_smaller = sum(value < rating[middle] for value in rating[middle + 1:])
            right_larger = len(rating) - middle - 1 - right_smaller
            teams += left_smaller * right_larger + left_larger * right_smaller
        return teams
