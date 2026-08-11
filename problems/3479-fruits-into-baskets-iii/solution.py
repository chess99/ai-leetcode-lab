# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(baskets); size=1
        while size<n:size*=2
        tree=[0]*(2*size)
        tree[size:size+n]=baskets
        for i in range(size-1,0,-1):tree[i]=max(tree[i*2],tree[i*2+1])
        missed=0
        for fruit in fruits:
            if tree[1]<fruit: missed+=1; continue
            node=1
            while node<size:
                node=node*2 if tree[node*2]>=fruit else node*2+1
            tree[node]=0; node//=2
            while node:
                tree[node]=max(tree[node*2],tree[node*2+1]); node//=2
        return missed
