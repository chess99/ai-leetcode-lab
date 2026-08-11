# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:23Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        word_counts = defaultdict(int)

        for message, sender in zip(messages, senders):
            word_counts[sender] += message.count(" ") + 1

        return max(
            word_counts,
            key=lambda sender: (word_counts[sender], sender),
        )
