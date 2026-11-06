"""blog/factcheck/*.json から事実確認リストのHTMLを作る。
使い方: python3 -I blog/factcheck/build_page.py  → blog/factcheck/factcheck.html
"""
import glob
import html
import json
import pathlib

HERE = pathlib.Path(__file__).parent
arts = [json.load(open(f)) for f in sorted(glob.glob(str(HERE / "*.json")))]
drafts = {}
for line in open(HERE.parent / "wp" / "drafts.jsonl"):
    p = json.loads(line)
    drafts[p["source"]] = p["draft"]
for a in arts:
    a["draft"] = drafts.get(a["id"])

# 複数記事にまたがる項目と、クライアントの決定(2026-11-06)
CROSS = [
    ("無料体験で誰が話すか", "決定: メインコーチの保崎淳が話す。辻尾が直接話すとしていた記述を直した", "2001, 2006, 2031, 2286 ほか"),
    ("保崎淳の経歴", "決定: 「Jリーグの複数クラブでプレー」に統一", "2006, 2323, 2337, 2353 ほか"),
    ("インテリジェンスU15", "決定: 対象は中学生男女。日時・会場(毎週木曜19:00〜21:00、スポルティーボ南与野)は正しい", "2323, 2337, 2397, 2412"),
    ("BoS理論の説明", "決定: Brain of Soccer ではない。2337 と出版社ページの説明・書名にそろえた", "2006, 2323, 2337"),
    ("辻尾のプロ歴", "決定: 「10年以上」に統一", "2006 ほか"),
    ("敬称・表記", "決定: 第三者の人名に「さん」は付けない。ブランドは GRITcoaching(GRITは大文字)", "全記事"),
]

data = json.dumps(arts, ensure_ascii=False)
cross_html = "\n".join(
    f'<li class="cross"><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p><p class="where">対象: {html.escape(w)}</p></li>'
    for t, d, w in CROSS
)
total = sum(len(a["items"]) for a in arts)
high = sum(1 for a in arts for i in a["items"] if i["priority"] == "高")
mism = [(a, i) for a in arts for i in a["items"] if i["source_check"].startswith("不一致")]
mism_html = "\n".join(
    f'<li><span class="aid">{a["id"]}</span><div><p class="q">{html.escape(i["what_to_check"])}</p>'
    f'<p class="cur">現在の記述: 「{html.escape(i["current_text"])}」</p>'
    f'<p class="res">{html.escape(i["source_check"])}</p></div></li>'
    for a, i in mism
)

from collections import Counter
res = Counter(i.get("resolution", "未対応") for a in arts for i in a["items"])
open_high = sum(1 for a in arts for i in a["items"] if i.get("resolution", "要確認").startswith("要確認") and i["priority"] == "高")
res_html = "".join(f'<div class="stat"><b>{n}</b><span>{html.escape(k)}</span></div>' for k, n in res.most_common())

page = (HERE / "template.html").read_text()
page = page.replace("__RES__", res_html).replace("__OPENHIGH__", str(open_high))
page = (page.replace("__DATA__", data.replace("</", "<\\/"))
            .replace("__CROSS__", cross_html)
            .replace("__MISM__", mism_html)
            .replace("__TOTAL__", str(total))
            .replace("__HIGH__", str(high))
            .replace("__NMISM__", str(len(mism)))
            .replace("__NART__", str(len(arts))))
(HERE / "factcheck.html").write_text(page)
print("written", total, "items")
