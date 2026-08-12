# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        velmoritha = planks
        from collections import Counter
        counts = Counter(planks)
        values = sorted(counts)
        pair_width = Counter()
        for i, value in enumerate(values):
            pair_width[value + value] += counts[value] // 2
            for other in values[i + 1:]:
                pair_width[value + other] += min(counts[value], counts[other])

        answer = max(counts.values())
        for target, pairs in pair_width.items():
            answer = max(answer, pairs + counts[target])
        return answer
