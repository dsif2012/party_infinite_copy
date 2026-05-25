from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = {
    "README.md": ["雙玩家", "夜讀", "黎", "run-index.md"],
    "NEW_WINDOW_PROMPT.md": ["共享資訊", "私有資訊", "雙線敘事", "時間對齊"],
    "world-rules.md": ["白塔", "風聲", "雙玩家", "彈性隊伍"],
    "progression-system.md": ["C 級", "正式戰力評估", "論壇", "市集"],
    "combat-rating-and-command-conventions.md": ["戰力", "指揮", "C 級", "戰力平分"],
    "current-state.md": ["F", "夜讀", "黎", "副本綁定道具"],
    "character-yedu.md": ["夜讀", "學長", "由玩家演繹補充", "黎"],
    "character-li.md": ["黎", "學弟", "由玩家演繹補充", "夜讀"],
    "team-party-file.md": ["夜讀", "黎", "臨時隊友", "雙線敘事"],
    "items-and-skills.md": ["官方點數", "同頁扣環", "技能", "資源"],
    "companions.md": ["白塔", "風聲", "臨時隊友", "關係"],
    "reality-layer.md": ["現實線", "白塔", "論壇", "市場"],
    "run-index.md": ["Run Index", "Completed", "Current"],
    "runs/001-freshman-binding-run.md": ["F", "夜讀", "黎", "副本綁定道具"],
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
