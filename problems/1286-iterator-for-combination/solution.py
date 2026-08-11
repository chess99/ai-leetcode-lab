# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:15Z
# Experiment: ai-leetcode-lab, round 1
from itertools import combinations
class CombinationIterator:
 def __init__(self,characters:str,combinationLength:int): self.items=[''.join(x) for x in combinations(characters,combinationLength)];self.i=0
 def next(self)->str: value=self.items[self.i];self.i+=1;return value
 def hasNext(self)->bool: return self.i<len(self.items)
