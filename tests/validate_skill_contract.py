from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "hot-commentary" / "SKILL.md"
CARD = ROOT / "hot-commentary" / "references" / "topic-card-contract.md"
DOSSIER = ROOT / "hot-commentary" / "references" / "argument-dossier-contract.md"
MECHANISMS = ROOT / "hot-commentary" / "references" / "china-social-mechanism-lenses.md"
AUTHOR = ROOT / "hot-commentary" / "references" / "author-profile-contract.md"
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
dossier = read(DOSSIER)
mechanisms = read(MECHANISMS)
author = read(AUTHOR)
script = read(SCRIPT)
openai = read(OPENAI)

# Skill routing and hard selection gate.
assert re.search(r"^name: hot-commentary$", skill, re.MULTILINE)
assert re.search(r"^description: Use when ", skill, re.MULTILINE)
for dependency in ["ego-browser", "hot-search-insight", "script-writer", "humanizer-zh"]:
    assert dependency in skill
assert "用户已明确选择一个选题" in skill
assert "恰好三张" in skill
assert "证据不足时不得硬写" in skill
assert "补充两张" in skill

# Complete cards remain intact, but all early angles are provisional.
for field in FIELDS:
    assert field in card, f"missing topic-card field: {field}"
assert "恰好三张" in card
assert "120—220" in card
assert "来源未提供" in card
assert card.count("【初步假设】") >= 15
assert re.search(
    r"观察时间.*YYYY-MM-DD HH:mm.*来源未提供",
    card,
    re.DOTALL,
), "topic-card contract must require an exact minute timestamp or 来源未提供"
assert re.search(
    r"展示前.*自检.*三张.*观察时间.*初步假设.*开场摘要",
    card,
    re.DOTALL,
), "topic-card contract must require a pre-display card-format self-check"

# The argument system adjudicates claims before language generation.
for term in [
    "流行结论", "叙事裂缝", "可裁决问题", "事实时间线", "一致性检查",
    "最强反方", "决定性证据", "中国社会机制假设", "责任判决",
    "结论边界与置信度", "过界检查", "强制反向审稿",
]:
    assert term in dossier, f"missing argument-dossier requirement: {term}"
assert "不得写入磁盘" in dossier
assert "不创建 TXT" in dossier
assert "补充两张" in dossier
assert "明显偏离选题卡" in dossier
assert "两个互不兼容的结论" in dossier

# Mechanisms are questions, never plug-in answers.
assert "用于提出问题，不是预制答案" in mechanisms
assert "替代解释" in mechanisms
assert "单篇 AI 稿" in mechanisms
for term in ["正式规则与实际执行", "中央、地方、部门与基层激励", "企业、平台与行政权力", "收益、风险与责任分配", "历史记忆与集体经验"]:
    assert term in mechanisms

# User worldview stays machine-local and explicit.
assert "/Users/zhangqiuyue/吕浩然/.hot-commentary-data/author-profile.md" in author
assert "只保存在本机" in author
assert "不得从单篇稿件、选题选择或沉默推断" in author
assert "用户明确表达并确认" in author

# Downstream skills are translators/editors and must preserve frozen reasoning.
assert "只做口播转译" in script
assert "只做表面语言审校" in script
assert "事实不变量" in script
assert "不得新增具名事实、数字、引语、案例、个人经历或来源" in script
assert "不得改变责任主体和结论范围" in script
assert "`script-writer` 的历史、项目、模板或偏好数据库" in script
assert "唯一允许持久化的稿件成品" in script
assert "取消 **45/50**" in script
assert "不使用固定六段式" in script
assert "不强制三层机制、现实启示、评论区问题或 CTA" in script
assert "1200—1800" in script
assert "不是机械验收配额" in script
assert "反向审稿" in script

# TXT remains clean and safe.
assert "/Users/zhangqiuyue/吕浩然/热点评论" in script
assert "不得写入内部立论案卷" in script
assert "不得静默覆盖" in script
assert "路径穿越" in script
assert "最终交付只产生或复用一份干净 TXT" in script

# UI metadata remains discoverable and aligned.
assert re.search(
    r"^[ \t]*display_name:\s*['\"]?热点评论['\"]?\s*$",
    openai,
    re.MULTILINE,
)
assert "证据立论" in openai
assert "$hot-commentary" in openai

print("hot-commentary evidence-led contract: PASS")
