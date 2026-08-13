# 解题记录

封装 setTimeout 为 Promise，并在异步函数中 await 该 Promise。

## 思路

返回在指定毫秒数后兑现的 Promise。

## 复杂度

创建时间、额外空间均为 `O(1)`。

## 边界条件与本地验证

覆盖零延迟与正延迟。
