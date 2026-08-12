// AI solution attribution
// Client: Codex Desktop
// Model: gpt-5.6-terra
// Reasoning effort: medium
// Profile: terra-medium
// Created: 2026-08-12T14:41:02Z
// Experiment: ai-leetcode-lab, round 1
function cancellable<T>(generator: Generator<Promise<any>, T, unknown>): [() => void, Promise<T>] {
    let finished = false;
    let generation = 0;
    let cancel: () => void = () => {};

    const promise = new Promise<T>((resolve, reject) => {
        const advance = (method: "next" | "throw", value?: any): void => {
            if (finished) return;
            let next: IteratorResult<Promise<any>, T>;
            try {
                next = method === "next" ? generator.next(value) : generator.throw!(value);
            } catch (error) {
                finished = true;
                reject(error);
                return;
            }
            if (next.done) {
                finished = true;
                resolve(next.value);
                return;
            }

            const current = ++generation;
            Promise.resolve(next.value).then(
                result => {
                    if (!finished && current === generation) advance("next", result);
                },
                error => {
                    if (!finished && current === generation) advance("throw", error);
                }
            );
        };

        cancel = () => {
            if (finished) return;
            ++generation;
            advance("throw", "Cancelled");
        };
        advance("next");
    });
    return [cancel, promise];
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */
