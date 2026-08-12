# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque


class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g=[[]for _ in range(n)]
        for a,b in edges:g[a].append(b);g[b].append(a)
        # State (mask,left,right) grows a palindrome from both ends.
        q=deque();seen=set();ans=1
        for i in range(n):
            q.append((1<<i,i,i,1));seen.add((1<<i,i,i))
        for a,b in edges:
            if label[a]==label[b]:
                mask=(1<<a)|(1<<b);q.append((mask,a,b,2));seen.add((mask,a,b));ans=2
        while q:
            mask,a,b,length=q.popleft()
            for x in g[a]:
                if mask>>x&1:continue
                for y in g[b]:
                    if x==y or mask>>y&1 or label[x]!=label[y]:continue
                    key=(mask|1<<x|1<<y,x,y)
                    if key not in seen:seen.add(key);q.append((*key,length+2));ans=max(ans,length+2)
        return ans
