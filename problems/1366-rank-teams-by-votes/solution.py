# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:07Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        scores = defaultdict(lambda: [0] * len(votes[0]))
        for vote in votes:
            for position, team in enumerate(vote): scores[team][position] -= 1
        return ''.join(sorted(scores, key=lambda team: (scores[team], team)))
