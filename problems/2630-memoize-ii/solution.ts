// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-12T14:41:01Z
// Experiment: ai-leetcode-lab, round 1
type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    type Node = {
        children: Map<any, Node>;
        hasValue: boolean;
        value: any;
    };
    const makeNode = (): Node => ({ children: new Map(), hasValue: false, value: undefined });
    const root = makeNode();

    return function (...args: any[]) {
        let node = root;
        for (const arg of args) {
            let next = node.children.get(arg);
            if (next === undefined) {
                next = makeNode();
                node.children.set(arg, next);
            }
            node = next;
        }
        if (!node.hasValue) {
            node.value = fn(...args);
            node.hasValue = true;
        }
        return node.value;
    };
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
