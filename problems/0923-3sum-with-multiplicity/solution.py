# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:20Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counts = Counter(arr); values = sorted(counts); answer = 0; modulo = 1_000_000_007
        for i, first in enumerate(values):
            for j in range(i, len(values)):
                second = values[j]; third = target - first - second
                if third not in counts or third < second: continue
                if first == second == third: answer += counts[first] * (counts[first]-1) * (counts[first]-2) // 6
                elif first == second: answer += counts[first] * (counts[first]-1) // 2 * counts[third]
                elif second == third: answer += counts[first] * counts[second] * (counts[second]-1) // 2
                else: answer += counts[first] * counts[second] * counts[third]
        return answer % modulo
