# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:04:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned=set(banned); counts={}; word=''
        for char in paragraph.lower()+' ':
            if char.isalpha(): word+=char
            elif word:
                if word not in banned: counts[word]=counts.get(word,0)+1
                word=''
        return max(counts,key=counts.get)
