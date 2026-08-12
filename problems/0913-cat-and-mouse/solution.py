# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:02Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        from collections import deque

        size=len(graph)
        outcome=[[[0]*2 for _ in range(size)]for _ in range(size)]
        degree=[[[len(graph[mouse]),len([node for node in graph[cat]if node])]
                 for cat in range(size)]for mouse in range(size)]
        queue=deque()
        for cat in range(1,size):
            for turn in range(2):
                outcome[0][cat][turn]=1;queue.append((0,cat,turn,1))
                outcome[cat][cat][turn]=2;queue.append((cat,cat,turn,2))

        while queue:
            mouse,cat,turn,winner=queue.popleft()
            if turn==0:
                parents=((mouse,previous,1)for previous in graph[cat]if previous)
            else:
                parents=((previous,cat,0)for previous in graph[mouse])
            for previous_mouse,previous_cat,previous_turn in parents:
                if outcome[previous_mouse][previous_cat][previous_turn]:continue
                player=1 if previous_turn==0 else 2
                if winner==player:
                    outcome[previous_mouse][previous_cat][previous_turn]=winner
                    queue.append((previous_mouse,previous_cat,previous_turn,winner))
                else:
                    degree[previous_mouse][previous_cat][previous_turn]-=1
                    if degree[previous_mouse][previous_cat][previous_turn]==0:
                        other=2 if player==1 else 1
                        outcome[previous_mouse][previous_cat][previous_turn]=other
                        queue.append((previous_mouse,previous_cat,previous_turn,other))
        return outcome[1][2][0]
