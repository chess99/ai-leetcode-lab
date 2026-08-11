# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
Map 将事件名映射到按订阅顺序排列的回调数组；emit 顺序调用，unsubscribe 从所属数组移除回调。
## 复杂度
订阅 `O(1)`，触发 `O(k)`，取消订阅 `O(k)`；空间 `O(k)`。
## 边界条件与本地验证
无订阅事件返回空数组；取消后不再触发。已验证题面操作序列。
