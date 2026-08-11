# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:13Z
# Experiment: ai-leetcode-lab, round 1

class SQL:
    def __init__(self, names: list[str], columns: list[int]):
        self.tables = {name: [count, 1, {}] for name, count in zip(names, columns)}
    def ins(self, name: str, row: list[str]) -> bool:
        if name not in self.tables or len(row) != self.tables[name][0]: return False
        table = self.tables[name]; table[2][table[1]] = row; table[1] += 1; return True
    def rmv(self, name: str, rowId: int) -> None:
        if name in self.tables: self.tables[name][2].pop(rowId, None)
    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables or rowId not in self.tables[name][2] or not 1 <= columnId <= self.tables[name][0]: return '<null>'
        return self.tables[name][2][rowId][columnId - 1]
    def exp(self, name: str) -> list[str]:
        if name not in self.tables: return []
        return [','.join([str(row_id), *row]) for row_id, row in self.tables[name][2].items()]
