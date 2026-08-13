# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:31:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        chosen, remaining = cards[:cnt], cards[cnt:]
        score = sum(chosen)
        if score % 2 == 0:
            return score

        candidates = []
        selected_odd = [card for card in chosen if card % 2]
        selected_even = [card for card in chosen if card % 2 == 0]
        remaining_odd = [card for card in remaining if card % 2]
        remaining_even = [card for card in remaining if card % 2 == 0]
        if selected_odd and remaining_even:
            candidates.append(score - min(selected_odd) + max(remaining_even))
        if selected_even and remaining_odd:
            candidates.append(score - min(selected_even) + max(remaining_odd))
        return max(candidates, default=0)
