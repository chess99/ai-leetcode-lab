# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = [{}]
        best = [-1]

        def improve(node, index):
            current = best[node]
            if (current == -1 or len(wordsContainer[index]) < len(wordsContainer[current])
                    or (len(wordsContainer[index]) == len(wordsContainer[current])
                        and index < current)):
                best[node] = index

        for index, word in enumerate(wordsContainer):
            node = 0
            improve(node, index)
            for character in reversed(word):
                if character not in trie[node]:
                    trie[node][character] = len(trie)
                    trie.append({})
                    best.append(-1)
                node = trie[node][character]
                improve(node, index)
        answer = []
        for word in wordsQuery:
            node = 0
            for character in reversed(word):
                if character not in trie[node]:
                    break
                node = trie[node][character]
            answer.append(best[node])
        return answer
