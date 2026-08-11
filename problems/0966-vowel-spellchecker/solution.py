# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:05:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels=set('aeiou')
        def devowel(word): return ''.join('*' if c in vowels else c for c in word.lower())
        exact=set(wordlist); caps={}; vowel={}
        for word in wordlist: caps.setdefault(word.lower(),word);vowel.setdefault(devowel(word),word)
        return [q if q in exact else caps.get(q.lower(),vowel.get(devowel(q),'')) for q in queries]
