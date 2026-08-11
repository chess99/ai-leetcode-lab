// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-11T21:14:12Z
// Experiment: ai-leetcode-lab, round 1
/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = new Array(functions.length);
        let remaining = functions.length;
        if (remaining === 0) {
            resolve(results);
            return;
        }
        functions.forEach((fn, index) => {
            try {
                fn().then(
                    value => {
                        results[index] = value;
                        remaining -= 1;
                        if (remaining === 0) {
                            resolve(results);
                        }
                    },
                    reject,
                );
            } catch (error) {
                reject(error);
            }
        });
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
