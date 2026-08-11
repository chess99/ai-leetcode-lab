// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T14:10:22Z
// Experiment: ai-leetcode-lab, round 1
/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return x => functions.reduceRight((value, fn) => fn(value), x);
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
