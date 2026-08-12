# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:05Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        from fractions import Fraction

        def parse(text):
            integer, _, decimal = text.partition('.')
            nonrepeating, separator, repeating = decimal.partition('(')
            repeating = repeating[:-1] if separator else ''
            result = Fraction(int(integer), 1)
            if nonrepeating:
                result += Fraction(int(nonrepeating), 10 ** len(nonrepeating))
            if repeating and int(repeating):
                result += Fraction(int(repeating),
                                   10 ** len(nonrepeating) * (10 ** len(repeating) - 1))
            return result

        return parse(s) == parse(t)
