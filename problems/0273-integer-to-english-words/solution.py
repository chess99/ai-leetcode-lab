# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        below_twenty = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
                         'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
                         'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
                         'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
                'Seventy', 'Eighty', 'Ninety']

        def three_digits(value):
            words = []
            if value >= 100:
                words += [below_twenty[value // 100], 'Hundred']
                value %= 100
            if value >= 20:
                words.append(tens[value // 10])
                value %= 10
            if value:
                words.append(below_twenty[value])
            return words

        result = []
        for scale, name in ((1_000_000_000, 'Billion'),
                            (1_000_000, 'Million'),
                            (1_000, 'Thousand'), (1, '')):
            group, num = divmod(num, scale)
            if group:
                result.extend(three_digits(group))
                if name:
                    result.append(name)
        return ' '.join(result)
