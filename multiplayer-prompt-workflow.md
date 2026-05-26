# GPT 多人對話 Prompt 工作流｜Party Infinite

## 使用前提

本玩法是在 GPT 的多人對話模式中進行。

多人對話模式本身通常無法直接讀取 GitHub repo，因此不能期待主持模型自行讀取、比對或更新本 repo 的所有檔案。

每次要開始副本、現實段、結算段或新場景前，應由一個有 GitHub / 本地 repo 權限的 AI 先閱讀目前存檔，整合出一份可直接貼進多人對話模式的 session prompt。

## 有權限 AI 的工作

有權限 AI 每次準備 prompt 時，必須先閱讀：

1. `current-state.md`
2. `world-rules.md`
3. `difficulty-design.md`
4. `rules/player-control.md`
5. `first-session-setup.md`
6. 相關角色檔
7. `team-party-file.md`
8. `items-and-skills.md`
9. `companions.md`
10. `reality-layer.md`
11. `progression-system.md`
12. `combat-rating-and-command-conventions.md`
13. `run-index.md`
14. 當前副本檔，例如 `runs/001-freshman-binding-run.md`

然後產出一份本次可用 prompt，放在 `prompts/current-session-prompt.md`。

## Prompt 整合原則

每次 prompt 只放「本次會用到的內容」。

應包含：

- 目前要跑的是角色建立、副本、現實段、結算段，或其他段落。
- 當前時間線與角色狀態。
- 玩家角色的行動控制權限制。
- 本次副本的難度、定位、HE / TE 尺度。
- 本次副本會遇到的規則、風險、場域、NPC 與主持尺度。
- 本次可以使用的道具、資訊入口與隊友資源。
- 本次不能預設知道的情報。
- 本次結束後需要更新哪些 repo 檔案。

不應包含：

- 本次難度不會遇到的高階機制。
- 過早揭露的世界觀真相。
- 玩家角色尚未知道的隱藏情報。
- 與當前副本無關的高階戰鬥、PvP、勢力戰或貢獻競爭規則。

## 難度裁切規則

如果當前是 F 級副本，prompt 應只保留 F 級需要的資訊：

- 規則是真的。
- 不照規則會出事。
- 保命規則清楚、少量、可理解。
- HE 以照規則、完成簡單目標、活著離開為主。
- TE 只需要一次簡單推理或一次有限風險承擔。
- 不需要真正戰鬥。
- 不需要複雜隊伍戰術。
- 不需要玩家勢力或 PvP。
- 不需要 D 級以上的戰鬥力貢獻、搶貢獻、戰利品分配或隊伍指揮壓力。

如果之後升到 D / C / B 以上，再由有權限 AI 根據 `difficulty-design.md` 重新裁切 prompt。

## 本 repo 當前用法

本 repo 目前是第一次遊玩前模板：

- 需要先設定玩家 A 姓名。
- 需要先設定玩家 B 姓名。
- 需要設定兩人的關係與願意公開的基礎資訊。
- 之後再進入第一個 F 級副本 `舊教學樓四樓：請一起簽退`。

因此當前多人對話 prompt 應使用：

`prompts/current-session-prompt.md`

這份 prompt 已經針對「角色建立 + 第一個 F 級副本開場」裁切，不包含 D 級以上才會使用的機制。

## 每次遊玩後

多人對話模式跑完一段後，應把結果交回有權限 AI，由其更新：

- `current-state.md`
- 當前 `runs/` 副本檔
- 必要時更新角色檔、隊伍檔、道具與技能檔、隊友與關係檔
- 若副本完成，更新 `run-index.md`

多人對話本身不負責直接改 repo；repo 更新應交給有檔案權限的 AI 執行。
