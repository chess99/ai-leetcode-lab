# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(value: int) -> bool:
            if value < 2:
                return False
            divisor = 2
            while divisor * divisor <= value:
                if value % divisor == 0:
                    return False
                divisor += 1
            return True

        digits = str(num)
        return all(is_prime(int(digits[:i])) and is_prime(int(digits[-i:]))
                   for i in range(1, len(digits) + 1))
