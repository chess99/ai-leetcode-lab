# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:08:33Z
# Experiment: ai-leetcode-lab, round 1
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            value = (rand7() - 1) * 7 + rand7()
            if value <= 40:
                return (value - 1) % 10 + 1
