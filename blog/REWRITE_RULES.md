# GRITcoaching ブログ リライトルール

目的は2つ。**検索で上位に出ること**と、**LINEからの無料体験申込を増やすこと**。
元の記事は質が高いので、全文を書き直すのではなく、SEOと申込導線に効く部分だけを手直しする。

- 入力: `blog/source/{id}-{slug}.html`(WordPress本文HTML。先頭コメントにid/title/url)
- 出力: `blog/rewritten/{id}-{slug}.html`(同じ形式。先頭コメントは下記フォーマット)

## 1. 絶対に守ること(変えない・作らない)

- **事実を作らない**。経歴・体験談・数字・引用・出典・人名・料金・指導体制は元記事にあるものだけを使う。新しい統計、研究、保護者の声、実績、日付を足さない
- 辻尾の経験談・発言の中身は変えない(言い回しの微調整まで)
- 一人称「僕」、語りかけの口調、「お父さん・お母さん」への寄り添いトーンを保つ
- `author-profile` ブロック(著者紹介)は**そのまま残す**
- slug(URL)は変えない
- 「必ず上手くなる」「絶対」などの効果の断言を新たに書かない
- 文字量は元記事の ±20% に収める

## 1.5 表記と事実の統一(2026-11-06 クライアント確認済み)

- 無料体験で話すのは**メインコーチの保崎淳**(元Jリーガー)。辻尾が体験で直接話す・見るとは書かない
- 保崎淳の経歴は「**Jリーグの複数クラブでプレー**」
- インテリジェンスU15 の対象は「**中学生男女**」。日時・会場は毎週木曜19:00〜21:00、スポルティーボ南与野
- BoS理論は「Brain of Soccer」ではない。ボールを中心に考える理論として、河岸貴の著書『サッカー「BoS理論」 ボールを中心に考え、ゴールを奪う方法』(カンゼン)で紹介されているものとして書く
- 辻尾のプロ歴は「**10年以上**」
- 第三者の人名に「さん」は付けない(津越智雄、河岸貴、保崎淳)
- ブランド表記は「**GRITcoaching**」(GRITは大文字)

## 2. SEO

1. **メインキーワードを1つ、サブキーワードを2〜3個決める**。元のタイトル・見出し・本文から、保護者が実際に検索しそうな言葉を選ぶ(例:「サッカー 試合に出られない 親」)。Search Console のデータが手に入ったら、そちらを優先する
2. **タイトル**: メインキーワードを前半に置く。全角32文字前後。「元Jリーガー」など信頼の要素は残す
3. **メタディスクリプション**: 全角80〜120文字。悩み → この記事でわかること → 元Jリーガーが解説、の順で書く。本文中の `<!-- META_DESCRIPTION: ... -->` は削除し、出力ファイル先頭のコメントに書く
4. **導入文**: 最初の3段落以内に「誰の、どんな悩みに、何を答える記事か」を書き、メインキーワードを自然に1回入れる
5. **見出し(h2/h3)**: h2の半分以上にメイン/サブキーワードかその言い換えを自然に入れる。不自然な詰め込みはしない
6. **よくある質問**: なければ、本文の内容だけで答えられるQ&Aを2〜4個、まとめのCTAの前に追加する(h2「よくある質問」+ h3「Q. 〜?」)。回答に新しい事実を入れない
7. **内部リンク**: 関連記事へのリンクを2〜4本。URLは正規形 `https://gritcoaching.co.jp/blog/blog/{slug}/` にする(`/blog/{slug}/` はリダイレクトになるので直す)。存在する記事は下の一覧のみ
8. **JSON-LD**(`<script type="application/ld+json">`)の `headline` を新しいタイトルに、`description` を新しいメタディスクリプションに合わせ、`dateModified` をリライト日にする(なければ追加)。`mainEntityOfPage.@id` やURLは正規形 `/blog/blog/{slug}/` に直す。それ以外は変えない

## 3. 申込導線(LINE)

LINEのURL(全CTA共通):
`https://s.lmes.jp/landing-qr/2005957649-Lx6O9Wo7?uLand=tfTxc5`

1. **`https://gritcoaching.co.jp/contact/` へのリンクはすべて上記LINE URLに置き換える**
2. **記事の途中にCTAを1つ追加する**。位置は、最初に読者の悩みに答え終わったh2セクションの直後(記事の30〜50%あたり)。形は次のとおり:
   ```html
   <div class="cta-inline" style="margin:2.4em 0;padding:20px 22px;border:2px solid #06C755;border-radius:12px;background:#f5fff8;">
     <p style="margin:0 0 10px;font-weight:700;">{その記事の悩みにつなげた一文。例:「うちの子の場合はどうなんだろう」と思ったら}</p>
     <p style="margin:0 0 14px;font-size:0.92rem;">元Jリーガーのコーチが、お子さんの今の動きを見て直接お話しします。無料体験はLINEから申し込めます。</p>
     <p style="margin:0;"><a href="LINE_URL" style="display:inline-block;padding:12px 22px;border-radius:999px;background:#06C755;color:#fff;font-weight:700;text-decoration:none;">LINEで無料体験を申し込む</a></p>
   </div>
   ```
3. **記事末尾の `cta-free-trial` セクション**: 見出しと本文は活かし、ボタンを `LINEで無料体験を申し込む`(LINE URL)にする。本文に「LINEから申し込める」ことを一言入れる。「無理な勧誘はしません」など元記事にある安心材料は残す
4. CTAは途中1つと末尾1つの合計2つまで。それ以上は増やさない

## 4. 出力ファイルの先頭コメント

```
<!-- id: {id}
title: {新タイトル}
url: {元のurl}
meta_description: {メタディスクリプション}
main_keyword: {メインキーワード}
sub_keywords: {サブ1}, {サブ2}, {サブ3}
changes: {主な変更点を1行で}
-->
```

## 5. 記事一覧(内部リンク先)

| id | slug | テーマ |
|---|---|---|
| 2001 | elementary-soccer-physical-golden-age | 小学生のフィジカル・ゴールデンエイジ |
| 2006 | elementary-soccer-school-how-to-choose | スクールの選び方(2026を統合する正規記事) |
| 2031 | elementary-soccer-match-nerves-mental-tips | 試合での緊張・メンタル・親の声かけ |
| 2286 | soccer-pro-path-environment-interview | プロになるための環境選び |
| 2323 | u15-soccer-intelligence-off-the-ball | U15のインテリジェンス・オフザボール |
| 2337 | bos-theory-soccer-german-terms | BoS理論・ドイツ語14語 |
| 2346 | child-wants-to-quit-soccer | 「サッカーを辞めたい」と言われたら |
| 2351 | tracen-rejected-parents | トレセンに落ちた子への声かけ |
| 2353 | elementary-soccer-physical-contact | 当たり負け |
| 2393 | child-not-playing-soccer-matches | 試合に出られない・補欠 |
| 2395 | elementary-soccer-not-improving-parents | 上達しない・親の声かけ |
| 2397 | junior-high-soccer-club-or-school-team | 中学 部活かクラブチームか |
| 2412 | junior-high-soccer-selection-tips | 中学セレクション対策 |

※ 2026(elementary-soccer-school-how-to-choose-2)は2006に統合し、2006へリダイレクトする。内部リンク先には使わない。
