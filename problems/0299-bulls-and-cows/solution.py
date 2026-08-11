# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:44:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        balance = [0] * 10
        cows = 0
        for secret_digit, guess_digit in zip(secret, guess):
            if secret_digit == guess_digit:
                bulls += 1
            else:
                secret_index, guess_index = int(secret_digit), int(guess_digit)
                if balance[secret_index] < 0:
                    cows += 1
                if balance[guess_index] > 0:
                    cows += 1
                balance[secret_index] += 1
                balance[guess_index] -= 1
        return f"{bulls}A{cows}B"
