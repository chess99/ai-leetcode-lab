# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        root = {}
        for word in dictionary:
            node = root
            for char in reversed(word):
                node = node.setdefault(char, {})
            node["#"] = True
        dp = [0] + [len(sentence)] * len(sentence)
        for end in range(1, len(sentence) + 1):
            dp[end] = dp[end - 1] + 1
            node = root
            for start in range(end - 1, -1, -1):
                if sentence[start] not in node:
                    break
                node = node[sentence[start]]
                if "#" in node:
                    dp[end] = min(dp[end], dp[start])
        return dp[-1]
