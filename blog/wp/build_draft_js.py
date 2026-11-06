"""リライト版1本ぶんの「下書き作成」JSを出力する(Orcaブラウザの eval で、ログイン中のwp-admin上で実行)。

- 公開中の元記事には触れない。新しい blog 投稿を status=draft で作る
- アイキャッチ画像・カテゴリーは元記事から引き継ぐ
- slug は指定しない(公開時に元記事へ反映するため)
使い方: python3 blog/wp/build_draft_js.py blog/rewritten/2393-....html > out.js
"""
import json, re, sys, pathlib
p = pathlib.Path(sys.argv[1])
html = p.read_text()
head = re.match(r"<!--(.*?)-->\s*", html, re.S)
meta = dict(l.split(":", 1) for l in head.group(1).strip().splitlines() if ":" in l)
meta = {k.strip(): v.strip() for k, v in meta.items()}
content = html[head.end():]
src_id = int(meta["id"])
payload = {"title": meta["title"], "content": content, "status": "draft"}
js = f"""(async () => {{
  const nonce = await (await fetch('/wp-admin/admin-ajax.php?action=rest-nonce', {{credentials:'same-origin'}})).text();
  const h = {{'X-WP-Nonce': nonce, 'Content-Type': 'application/json'}};
  const orig = await (await fetch('/wp-json/wp/v2/blog/{src_id}?context=edit', {{headers:h, credentials:'same-origin'}})).json();
  if (!orig.id) return JSON.stringify({{error:'original not readable', orig}});
  const body = Object.assign({json.dumps(payload, ensure_ascii=False)}, {{featured_media: orig.featured_media, categories: orig.categories, tags: orig.tags}});
  const r = await fetch('/wp-json/wp/v2/blog', {{method:'POST', headers:h, credentials:'same-origin', body: JSON.stringify(body)}});
  const d = await r.json();
  return JSON.stringify({{http:r.status, id:d.id, status:d.status, title:d.title&&d.title.raw, link:d.link, err:d.code&&d.message, source:{src_id}, source_status: orig.status}});
}})()"""
print(js)
