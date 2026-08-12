# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        below_twenty = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen",
        ]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def chunk(value: int):
            words = []
            if value >= 100:
                words.extend((below_twenty[value // 100], "Hundred"))
                value %= 100
            if value >= 20:
                words.append(tens[value // 10])
                value %= 10
            if value:
                words.append(below_twenty[value])
            return words

        words = []
        for divisor, name in ((10**9, "Billion"), (10**6, "Million"), (1000, "Thousand"), (1, "")):
            part, num = divmod(num, divisor)
            if part:
                words.extend(chunk(part))
                if name:
                    words.append(name)
        return " ".join(words)
