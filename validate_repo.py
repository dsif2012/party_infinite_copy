from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = {
    "README.md": ["雙玩家", "第一次遊玩", "rules/player-control.md", "多人遊玩規則"],
    "NEW_WINDOW_PROMPT.md": ["共享資訊", "私有資訊", "回合制度", "時間對齊"],
    "rules/player-control.md": ["角色綁定", "行動控制權", "回合時間制度", "凍結狀態"],
    "world-rules.md": ["白塔", "風聲", "雙玩家", "回合時間制度"],
    "difficulty-design.md": ["難度設計細節", "HE", "TE", "夜讀當前適配"],
    "multiplayer-prompt-workflow.md": ["多人對話", "GitHub", "current-session-prompt.md", "難度裁切"],
    "prompts/current-session-prompt.md": ["角色建立", "第一個 F 級副本", "玩家 A", "現實局外增強"],
    "progression-system.md": ["C 級", "正式戰力評估", "論壇", "市集"],
    "combat-rating-and-command-conventions.md": ["戰力", "指揮", "C 級", "戰力平分"],
    "current-state.md": ["第一次遊玩", "副本綁定道具", "雙線敘事", "姓名"],
    "first-session-setup.md": ["姓名", "關係", "玩家 A", "玩家 B"],
    "character-player-a.md": ["玩家 A", "第一次遊玩時設定", "由玩家演繹補充"],
    "character-player-b.md": ["玩家 B", "第一次遊玩時設定", "由玩家演繹補充"],
    "team-party-file.md": ["玩家 A", "玩家 B", "臨時隊友", "雙線敘事"],
    "items-and-skills.md": ["官方點數", "同頁扣環", "技能", "資源"],
    "companions.md": ["白塔", "風聲", "臨時隊友", "第一次遊玩時自行設定"],
    "reality-layer.md": ["現實線", "白塔", "論壇", "回合制度"],
    "run-index.md": ["Run Index", "Completed", "Current"],
    "runs/001-freshman-binding-run.md": ["F", "副本框架", "副本綁定道具", "現實局外增強"],
}


def main() -> int:
    missing = []
    errors = []
    for rel_path, keywords in REQUIRED_FILES.items():
        path = ROOT / rel_path
        if not path.exists():
            missing.append(rel_path)
            continue
        text = path.read_text(encoding="utf-8")
        for keyword in keywords:
            if keyword not in text:
                errors.append(f"{rel_path} missing keyword: {keyword}")

    if missing:
        print("Missing files:")
        for rel_path in missing:
            print(f"  - {rel_path}")
    if errors:
        print("Content errors:")
        for err in errors:
            print(f"  - {err}")

    if missing or errors:
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
