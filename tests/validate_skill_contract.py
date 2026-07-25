from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "hot-commentary" / "SKILL.md"
CARD = ROOT / "hot-commentary" / "references" / "topic-card-contract.md"
SCRIPT = ROOT / "hot-commentary" / "references" / "script-and-archive-contract.md"
OPENAI = ROOT / "hot-commentary" / "agents" / "openai.yaml"

FIELDS = [
    "热搜原始话题", "观察时间", "榜单位置", "热度", "数据来源", "话题类型",
    "已核实的事实简述", "核心社会或营销洞察", "大众情绪与行为机制",
    "心理学依据", "传播逻辑", "口播主题", "开场摘要",
    "为什么现在值得讲", "表达风险", "事实来源链接",
]

def read(path: Path) -> str:
    assert path.is_file(), f"missing file: {path}"
    return path.read_text(encoding="utf-8")

skill = read(SKILL)
card = read(CARD)
script = read(SCRIPT)
openai = read(OPENAI)

assert re.search(r"^name: hot-commentary$", skill, re.MULTILINE)
assert re.search(r"^description: Use when ", skill, re.MULTILINE)
assert "ego-browser" in skill
assert "hot-search-insight" in skill
assert "script-writer" in skill
assert "明确选择" in skill
assert "停止" in skill
assert "恰好三张" in card
for field in FIELDS:
    assert field in card, f"missing topic-card field: {field}"
assert "120—220" in card
assert "来源未提供" in card
assert re.search(
    r"观察时间.*YYYY-MM-DD HH:mm.*来源未提供",
    card,
    re.DOTALL,
), "topic-card contract must require an exact minute timestamp or 来源未提供"
assert re.search(
    r"展示前.*自检.*三张.*观察时间.*开场摘要",
    card,
    re.DOTALL,
), "topic-card contract must require a pre-display card-format self-check"
assert "950—1300" in script
assert "/Users/zhangqiuyue/吕浩然/热点评论" in script
assert "不得静默覆盖" in script
assert re.search(
    r"^[ \t]*display_name:\s*['\"]?热点评论['\"]?\s*$",
    openai,
    re.MULTILINE,
)

print("hot-commentary contract: PASS")
