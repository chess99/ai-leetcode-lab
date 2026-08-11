# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:11:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countAndSay(self, n: int) -> str:
        term = "1"
        for _ in range(n - 1):
            parts = []
            index = 0
            while index < len(term):
                next_index = index
                while next_index < len(term) and term[next_index] == term[index]:
                    next_index += 1
                parts.append(str(next_index - index))
                parts.append(term[index])
                index = next_index
            term = "".join(parts)
        return term
