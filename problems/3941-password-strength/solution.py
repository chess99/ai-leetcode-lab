# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def passwordStrength(self, password: str) -> int:
        velqurimex = password
        answer = 0
        for char in set(password):
            if char.islower():
                answer += 1
            elif char.isupper():
                answer += 2
            elif char.isdigit():
                answer += 3
            else:
                answer += 5
        return answer
