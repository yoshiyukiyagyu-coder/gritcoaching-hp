"""作成済みの下書き(drafts.jsonl)を、手元のリライト版の内容で上書きするJSを出力する。
下書き(status=draft)以外は更新しない。公開中の元記事には触れない。
使い方: python3 -I blog/wp/build_update_js.py blog/rewritten/2393-....html > out.js
"""
import json, re, sys, pathlib
p = pathlib.Path(sys.argv[1])
html = p.read_text()
head = re.match(r"<!--(.*?)-->\s*", html, re.S)
meta = {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in head.group(1).strip().splitlines() if ":" in l)}
src = int(meta["id"])
pairs = {json.loads(l)["source"]: json.loads(l)["draft"] for l in open(p.parent.parent / "wp" / "drafts.jsonl")}
draft = pairs[src]
payload = {"title": meta["title"], "content": html[head.end():]}
print(f"""(async () => {{
  const nonce = await (await fetch('/wp-admin/admin-ajax.php?action=rest-nonce', {{credentials:'same-origin'}})).text();
  const h = {{'X-WP-Nonce': nonce, 'Content-Type': 'application/json'}};
  const cur = await (await fetch('/wp-json/wp/v2/blog/{draft}?context=edit', {{headers:h, credentials:'same-origin'}})).json();
  if (cur.status !== 'draft') return JSON.stringify({{error:'not a draft, refusing', id:{draft}, status:cur.status}});
  const r = await fetch('/wp-json/wp/v2/blog/{draft}', {{method:'POST', headers:h, credentials:'same-origin', body: JSON.stringify(Object.assign({json.dumps(payload, ensure_ascii=False)}, {{status:'draft'}}))}});
  const d = await r.json();
  return JSON.stringify({{http:r.status, id:d.id, status:d.status, source:{src}}});
}})()""")
