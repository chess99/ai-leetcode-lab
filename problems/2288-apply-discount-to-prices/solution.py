# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:24Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = []
        for word in sentence.split():
            if word.startswith("$") and word[1:].isdigit():
                cents = int(word[1:]) * (100 - discount)
                word = f"${cents // 100}.{cents % 100:02d}"
            words.append(word)
        return " ".join(words)
