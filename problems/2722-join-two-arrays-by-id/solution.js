// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:14:13Z
// Experiment: ai-leetcode-lab, round 1
/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const byId = new Map();
    for (const item of arr1) {
        byId.set(item.id, {...item});
    }
    for (const item of arr2) {
        byId.set(item.id, {...byId.get(item.id), ...item});
    }
    return [...byId.values()].sort((left, right) => left.id - right.id);
};
