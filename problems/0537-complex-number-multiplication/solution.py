# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:16:14Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parts(number: str) -> tuple[int, int]:
            real, imaginary = number[:-1].split("+")
            return int(real), int(imaginary)

        real1, imaginary1 = parts(num1)
        real2, imaginary2 = parts(num2)
        real = real1 * real2 - imaginary1 * imaginary2
        imaginary = real1 * imaginary2 + imaginary1 * real2
        return f"{real}+{imaginary}i"
