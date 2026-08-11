// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:01:28Z
// Experiment: ai-leetcode-lab, round 1
/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined || typeof classFunction !== 'function') {
        return false;
    }
    let prototype = Object.getPrototypeOf(obj);
    while (prototype !== null) {
        if (prototype === classFunction.prototype) {
            return true;
        }
        prototype = Object.getPrototypeOf(prototype);
    }
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
