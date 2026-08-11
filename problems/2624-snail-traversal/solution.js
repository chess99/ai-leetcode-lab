// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:01:28Z
// Experiment: ai-leetcode-lab, round 1
/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (this.length !== rowsCount * colsCount) {
        return [];
    }
    const result = Array.from({ length: rowsCount }, () => Array(colsCount));
    for (let col = 0; col < colsCount; col++) {
        for (let row = 0; row < rowsCount; row++) {
            const targetRow = col % 2 === 0 ? row : rowsCount - 1 - row;
            result[targetRow][col] = this[col * rowsCount + row];
        }
    }
    return result;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
