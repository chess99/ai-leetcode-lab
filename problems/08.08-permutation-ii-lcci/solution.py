# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        chars = list(S)
        answer = []

        def search(index):
            if index == len(chars):
                answer.append(''.join(chars))
                return
            used = set()
            for following in range(index, len(chars)):
                if chars[following] in used:
                    continue
                used.add(chars[following])
                chars[index], chars[following] = chars[following], chars[index]
                search(index + 1)
                chars[index], chars[following] = chars[following], chars[index]

        search(0)
        return answer
