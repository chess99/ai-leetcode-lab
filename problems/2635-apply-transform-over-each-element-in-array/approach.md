# 解题记录

- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium

## 思路

预先创建等长结果数组，使用普通 `for` 循环逐个执行 `returnedArray[i] = fn(arr[i], i)`。不调用 `Array.prototype.map` 或任何借用该方法的形式。

## 复杂度

时间 `O(n)`，输出空间 `O(n)`。

## 边界条件与本地验证

覆盖空数组、仅依赖元素的回调、依赖下标的回调和常量回调；与手写 oracle 对拍，并做禁用 API 静态检查。
