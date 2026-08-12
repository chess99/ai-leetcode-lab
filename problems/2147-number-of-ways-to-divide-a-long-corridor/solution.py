# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        modulus = 10 ** 9 + 7
        seats = [index for index, value in enumerate(corridor) if value == "S"]
        if not seats or len(seats) % 2:
            return 0

        answer = 1
        for index in range(2, len(seats), 2):
            answer = answer * (seats[index] - seats[index - 1]) % modulus
        return answer
