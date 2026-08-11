# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ""
        answer = ""
        for _ in range(n):
            block_size = 1 << (n - len(answer) - 1)
            for character in "abc":
                if answer.endswith(character):
                    continue
                if k > block_size:
                    k -= block_size
                else:
                    answer += character
                    break
        return answer
