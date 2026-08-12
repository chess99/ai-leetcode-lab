# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:01Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
import sys
class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        sys.setrecursionlimit(max(1_000_000, len(parents) * 2))
        n=len(parents);children=[[] for _ in range(n)];root=0
        for node,parent in enumerate(parents):
            if parent<0:root=node
            else:children[parent].append(node)
        grouped=defaultdict(list)
        for i,(node,value) in enumerate(queries):grouped[node].append((value,i))
        trie=[[0,0,0]];answer=[0]*len(queries)
        def update(value,delta):
            node=0;trie[node][2]+=delta
            for bit in range(18,-1,-1):
                branch=(value>>bit)&1
                if trie[node][branch]==0:trie[node][branch]=len(trie);trie.append([0,0,0])
                node=trie[node][branch];trie[node][2]+=delta
        def maximize(value):
            node=result=0
            for bit in range(18,-1,-1):
                branch=(value>>bit)&1;wanted=1-branch;following=trie[node][wanted]
                if following and trie[following][2]:result|=1<<bit;node=following
                else:node=trie[node][branch]
            return result
        def dfs(node):
            update(node,1)
            for value,index in grouped[node]:answer[index]=maximize(value)
            for child in children[node]:dfs(child)
            update(node,-1)
        dfs(root);return answer
