# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        from collections import deque

        rows,cols=len(grid),len(grid[0]);food=mouse=cat=None;positions=[]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]!='#':positions.append((r,c))
        index={position:i for i,position in enumerate(positions)}
        for i,(r,c) in enumerate(positions):
            if grid[r][c]=='F':food=i
            elif grid[r][c]=='M':mouse=i
            elif grid[r][c]=='C':cat=i

        def build_moves(jump):
            all_moves=[]
            for r,c in positions:
                out=[index[r,c]]
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    for step in range(1,jump+1):
                        following=(r+dr*step,c+dc*step)
                        if following not in index:break
                        out.append(index[following])
                all_moves.append(out)
            return all_moves

        mouse_moves=build_moves(mouseJump)
        cat_moves=build_moves(catJump)
        size=len(positions)
        states=2*size*size
        outcome=bytearray(states)
        degree=[0]*states
        queue=deque()

        def state_id(mouse_position,cat_position,turn):
            return (mouse_position*size+cat_position)*2+turn

        for mouse_position in range(size):
            for cat_position in range(size):
                for turn in (0,1):
                    state=state_id(mouse_position,cat_position,turn)
                    degree[state]=len(mouse_moves[mouse_position] if turn==0
                                      else cat_moves[cat_position])
                    if mouse_position==cat_position or cat_position==food:
                        outcome[state]=2
                        queue.append(state)
                    elif mouse_position==food:
                        outcome[state]=1
                        queue.append(state)

        while queue:
            state=queue.popleft()
            turn=state&1
            pair=state>>1
            mouse_position,cat_position=divmod(pair,size)
            winner=outcome[state]
            if turn==0:
                parents=((mouse_position,previous_cat,1)
                         for previous_cat in cat_moves[cat_position])
            else:
                parents=((previous_mouse,cat_position,0)
                         for previous_mouse in mouse_moves[mouse_position])
            for previous_mouse,previous_cat,previous_turn in parents:
                parent=state_id(previous_mouse,previous_cat,previous_turn)
                if outcome[parent]:
                    continue
                player=1 if previous_turn==0 else 2
                if winner==player:
                    outcome[parent]=winner
                    queue.append(parent)
                else:
                    degree[parent]-=1
                    if degree[parent]==0:
                        outcome[parent]=2 if player==1 else 1
                        queue.append(parent)

        # Unresolved states are cycles. The mouse cannot force the food from
        # such a state, so the 1000-turn rule awards them to the cat.
        return outcome[state_id(mouse,cat,0)]==1
