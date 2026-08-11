# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for number in range(1, n + 1):
            text = ""
            if number % 3 == 0:
                text += "Fizz"
            if number % 5 == 0:
                text += "Buzz"
            answer.append(text or str(number))
        return answer
