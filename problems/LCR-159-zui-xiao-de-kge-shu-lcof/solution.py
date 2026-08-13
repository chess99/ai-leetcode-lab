# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:43:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        return sorted(stock)[:cnt]
