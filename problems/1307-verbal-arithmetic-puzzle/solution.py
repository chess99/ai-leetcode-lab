# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        if len(set(''.join(words)+result))>10:return False
        leading={word[0] for word in words+[result] if len(word)>1};mapping={};used=set();columns=max(map(len,words+[result]))
        def solve(column,row,total):
            if column==columns:return total==0
            if row<len(words):
                if column>=len(words[row]):return solve(column,row+1,total)
                char=words[row][-1-column]
                if char in mapping:return solve(column,row+1,total+mapping[char])
                for digit in range(10):
                    if digit not in used and (digit or char not in leading):
                        mapping[char]=digit;used.add(digit)
                        if solve(column,row+1,total+digit):return True
                        used.remove(digit);del mapping[char]
                return False
            char=result[-1-column] if column<len(result) else None;digit=total%10;carry=total//10
            if char is None:return False
            if char in mapping:return mapping[char]==digit and solve(column+1,0,carry)
            if digit in used or (digit==0 and char in leading):return False
            mapping[char]=digit;used.add(digit);answer=solve(column+1,0,carry);used.remove(digit);del mapping[char];return answer
        return solve(0,0,0)
