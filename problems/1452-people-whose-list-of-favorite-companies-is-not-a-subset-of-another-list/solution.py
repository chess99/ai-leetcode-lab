# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:51:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        companies = [set(items) for items in favoriteCompanies]
        return [i for i, current in enumerate(companies) if not any(i != j and current <= other for j, other in enumerate(companies))]
