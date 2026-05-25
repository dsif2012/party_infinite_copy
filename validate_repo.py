from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = {
    "README.md": ["雙玩家", "自建", "NEW_WINDOW_PROMPT.md"],
    "NEW_WINDOW_PROMPT.md": ["共享資訊", "私有資訊", "雙線敘事", "時間對齊"],
    "world-rules.md": ["白塔", "風聲", "雙玩家", "彈性隊伍"],
    "progression-system.md": ["C 級", "正式戰力評估", "論壇", "市集"],
    "combat-rating-and-command-conventions.md": ["戰力", "指揮", "C 級", "戰力平分"],
    "current-state.md": ["F", "副本綁定道具", "雙線敘事", "時間對齊"],
    "team-party-file.md": ["玩家自行決定", "臨時隊友", "指揮", "雙線敘事"],
    "runs/001-freshman-binding-run.md": ["F", "雙玩家", "副本綁定道具", "各 +80"],
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
