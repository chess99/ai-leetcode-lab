# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路
计算前缀和。令 `difference` 为从某个可操作前缀开始，当前玩家能取得的最大分差；选择长度 `i+1` 后得到前缀和并交换行动方，候选为 `prefix[i]-difference`。从右向左维护最大值。

## 复杂度
时间 $O(n)$，空间 $O(n)$。

## 边界条件与本地验证
两颗石子时只能全部合并，答案为总和。已与短数组完整极小极大游戏递归对拍。
