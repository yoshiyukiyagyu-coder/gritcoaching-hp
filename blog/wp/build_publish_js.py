"""リライト版を「公開中の元記事」に反映するJSを出力する(URL・公開日はそのまま)。
- 本文とタイトルを更新し、AIOSEO のメタディスクリプションを設定する
- 元記事が publish でなければ何もしない
使い方: python3 -I blog/wp/build_publish_js.py blog/rewritten/2393-....html > out.js
"""
import json, re, sys, pathlib
p = pathlib.Path(sys.argv[1])
html = p.read_text()
head = re.match(r"<!--(.*?)-->\s*", html, re.S)
meta = {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in head.group(1).strip().splitlines() if ":" in l)}
src = int(meta["id"])
payload = {"title": meta["title"], "content": html[head.end():]}
seo = {"postId": src, "title": None, "description": meta["meta_description"]}
print(f"""(async () => {{
  const nonce = await (await fetch('/wp-admin/admin-ajax.php?action=rest-nonce', {{credentials:'same-origin'}})).text();
  const h = {{'X-WP-Nonce': nonce, 'Content-Type': 'application/json'}};
  const cur = await (await fetch('/wp-json/wp/v2/blog/{src}?context=edit', {{headers:h, credentials:'same-origin'}})).json();
  if (cur.status !== 'publish') return JSON.stringify({{error:'source not published, refusing', id:{src}, status:cur.status}});
  const r = await fetch('/wp-json/wp/v2/blog/{src}', {{method:'POST', headers:h, credentials:'same-origin', body: JSON.stringify({json.dumps(payload, ensure_ascii=False)})}});
  const d = await r.json();
  const s = await fetch('/wp-json/aioseo/v1/posts-list/update-details-column', {{method:'POST', headers:h, credentials:'same-origin', body: JSON.stringify({json.dumps(seo, ensure_ascii=False)})}});
  const st = await s.text();
  return JSON.stringify({{http:r.status, id:d.id, status:d.status, link:d.link, seo_http:s.status, seo:st.slice(st.indexOf('{{')).slice(0,300)}});
}})()""")
