# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = [{"count": 0}]
        for word in words:
            node = 0
            for character in word:
                if character not in trie[node]:
                    trie[node][character] = len(trie)
                    trie.append({"count": 0})
                node = trie[node][character]
                trie[node]["count"] += 1
        answer = []
        for word in words:
            node = 0
            score = 0
            for character in word:
                node = trie[node][character]
                score += trie[node]["count"]
            answer.append(score)
        return answer
