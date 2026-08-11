# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:16:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        available={}
        for char in chars: available[char]=available.get(char,0)+1
        total=0
        for word in words:
            used={}
            for char in word: used[char]=used.get(char,0)+1
            if all(used[c]<=available.get(c,0) for c in used): total+=len(word)
        return total
