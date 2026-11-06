"""リライト済み記事を REWRITE_RULES.md の機械的に確認できる項目でチェックする。

使い方: python3 blog/check_rewrite.py   (リポジトリのルートで実行)
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
LINE = "s.lmes.jp/landing-qr/2005957649-Lx6O9Wo7"
SLUGS = {p.stem.split("-", 1)[1] for p in (ROOT / "source").glob("*.html")}
SLUGS.discard("elementary-soccer-school-how-to-choose-2")


def visible_len(html):
    html = re.sub(r"<!--.*?-->|<script.*?</script>|<style.*?</style>", "", html, flags=re.S)
    return len(re.sub(r"\s", "", re.sub(r"<[^>]+>", "", html)))


def author_block(html):
    m = re.search(r'<div class="author-profile".*?</details>', html, re.S)
    if m:
        return m.group(0)
    m = re.search(r'<p class="author-byline">.*?</details>', html, re.S)
    return m.group(0) if m else None


def check(out):
    src = ROOT / "source" / out.name
    s, o = src.read_text(), out.read_text()
    problems = []
    header = re.match(r"<!--(.*?)-->", o, re.S)
    meta = {}
    if not header:
        problems.append("先頭コメントがない")
    else:
        for line in header.group(1).strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        for k in ("id", "title", "meta_description", "main_keyword"):
            if not meta.get(k):
                problems.append(f"先頭コメントに {k} がない")
    md = meta.get("meta_description", "")
    if md and not 70 <= len(md) <= 130:
        problems.append(f"メタディスクリプション {len(md)}字")
    if "META_DESCRIPTION" in o:
        problems.append("META_DESCRIPTION コメントが残っている")
    if "gritcoaching.co.jp/contact/" in o:
        problems.append("/contact/ リンクが残っている")
    n_line = len(re.findall(r'<a [^>]*href="[^"]*' + re.escape(LINE), o))
    if n_line != 2:
        problems.append(f"LINEボタン {n_line}個")
    if 'class="cta-inline"' not in o:
        problems.append("途中CTAがない")
    for href in re.findall(r'href="(https://gritcoaching\.co\.jp/blog/[^"]*)"', o):
        m = re.fullmatch(r"https://gritcoaching\.co\.jp/blog/blog/([^/]+)/", href)
        if not m or m.group(1) not in SLUGS:
            problems.append(f"内部リンク不正: {href}")
    a, b = visible_len(s), visible_len(o)
    ratio = b / a - 1
    limit = 0.6 if "merged_from" in meta else 0.2
    if abs(ratio) > limit:
        problems.append(f"文字数 {a}→{b} ({ratio:+.0%})")
    if author_block(s) and author_block(s) != author_block(o):
        problems.append("著者ブロックが変わっている")
    for js in re.findall(r'<script type="application/ld\+json">(.*?)</script>', o, re.S):
        try:
            data = json.loads(js)
        except ValueError as e:
            problems.append(f"JSON-LD 不正: {e}")
            continue
        items = data if isinstance(data, list) else data.get("@graph", [data])
        for d in items:
            if d.get("@type") in ("Article", "BlogPosting"):
                if d.get("headline") != meta.get("title"):
                    problems.append("JSON-LD headline がタイトルと不一致")
                if d.get("dateModified", "")[:10] != "2026-11-06":
                    problems.append("JSON-LD dateModified 未更新")
    print(f"{'OK ' if not problems else 'NG '} {out.name}  {a}→{b}字 ({ratio:+.0%})  「{meta.get('title','')}」")
    for p in problems:
        print("     -", p)
    return not problems


results = [check(p) for p in sorted((ROOT / "rewritten").glob("*.html"))]
print(f"\n{sum(results)}/{len(results)} OK")
sys.exit(0 if all(results) else 1)
