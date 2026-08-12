# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:03Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        def recover(values,left):
            if left==0:return []
            values.sort();difference=values[1]-values[0];counter=Counter(values);without=[];with_value=[]
            for value in values:
                if counter[value]:counter[value]-=1;counter[value+difference]-=1;without.append(value);with_value.append(value+difference)
            if 0 in without:return [difference]+recover(without,left-1)
            return [-difference]+recover(with_value,left-1)
        return recover(sums,n)
