# gritcoaching.co.jp トップページ改修 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** gritcoaching.co.jp のトップページを、ストーリー型レイアウトで全面改修したHTMLプロトタイプを作成する。

**Architecture:** 純粋な HTML5 + CSS3 + Vanilla JS の静的ファイル構成。CSSカスタムプロパティでカラーシステムを管理し、コンポーネントごとにセクションを分割。JavaScriptはスクロール連動・カルーセル・ヘッダー変化のみ担当。

**Tech Stack:** HTML5, CSS3 (Custom Properties, Flexbox, Grid), Vanilla JavaScript (ES6+)

---

## ファイル構成

```
/index.html                  ← メインHTML（全セクション含む）
/assets/
  css/
    main.css                 ← デザイントークン＋全セクションのスタイル
  js/
    main.js                  ← スクロール効果・カルーセル・ヘッダー制御
  images/
    hero.jpg                 ← ヒーロー背景写真（差し替え用プレースホルダー）
    coach.jpg                ← コーチポートレート写真
    mission.jpg              ← 代表写真
    voice-1.jpg              ← 体験談1の写真
    voice-2.jpg              ← 体験談2の写真
    voice-3.jpg              ← 体験談3の写真
    blog-1.jpg               ← ブログ記事1サムネイル
    blog-2.jpg               ← ブログ記事2サムネイル
    blog-3.jpg               ← ブログ記事3サムネイル
    logo.svg                 ← ロゴ（SVGまたはPNG）
```

---

### Task 1: プロジェクトセットアップ

**Files:**
- Create: `index.html`
- Create: `assets/css/main.css`
- Create: `assets/js/main.js`
- Create: `assets/images/` (ディレクトリのみ)

- [ ] **Step 1: ディレクトリ構造を作成する**

```bash
mkdir -p assets/css assets/js assets/images
```

- [ ] **Step 2: index.html の骨格を作成する**

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>グリットコーチング・ジャパン株式会社</title>
  <meta name="description" content="やり抜く力と正しい努力で才能を凌駕する。スポーツを通じた人材育成と社会貢献。">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Montserrat:wght@400;600;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
  <!-- sections go here -->
  <script src="assets/js/main.js"></script>
</body>
</html>
```

- [ ] **Step 3: main.css にデザイントークンを定義する**

```css
:root {
  --color-main: #000032;
  --color-accent: #ee0044;
  --color-white: #ffffff;
  --color-gray-light: #f5f5f5;
  --color-gray-text: #aaaaaa;

  --font-ja: 'Noto Sans JP', sans-serif;
  --font-en: 'Montserrat', sans-serif;

  --section-padding: 80px 5%;
  --border-radius: 4px;
  --transition: 0.3s ease;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-ja);
  color: var(--color-main);
  background: var(--color-white);
  line-height: 1.7;
}

img {
  max-width: 100%;
  display: block;
}

a {
  text-decoration: none;
  color: inherit;
}

.section-label {
  font-family: var(--font-en);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: var(--color-accent);
  text-transform: uppercase;
  display: block;
  margin-bottom: 8px;
}

.section-title {
  font-size: clamp(1.5rem, 3vw, 2.5rem);
  font-weight: 700;
  line-height: 1.3;
}
```

- [ ] **Step 4: main.js の初期化コードを追加する**

```js
document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initCarousel();
  initScrollFade();
});
```

- [ ] **Step 5: ブラウザで index.html を開き、空白ページが文字化けなく表示されることを確認する**

```bash
open index.html
```

- [ ] **Step 6: コミットする**

```bash
git init
git add .
git commit -m "chore: initial project setup with design tokens"
```

---

### Task 2: ヘッダー

**Files:**
- Modify: `index.html` — `<header>` 追加
- Modify: `assets/css/main.css` — ヘッダースタイル追加
- Modify: `assets/js/main.js` — `initHeader()` 実装

- [ ] **Step 1: index.html に `<header>` を追加する**

```html
<header class="site-header" id="site-header">
  <div class="header-inner">
    <a href="/" class="header-logo">
      <img src="assets/images/logo.svg" alt="グリットコーチング・ジャパン株式会社" height="40">
    </a>
    <nav class="header-nav">
      <a href="#mission">Mission</a>
      <a href="#business">Business</a>
      <a href="#blog">Blog</a>
      <a href="#company">Company</a>
      <a href="#contact">Contact</a>
    </nav>
    <a href="#contact" class="header-cta">無料体験申込</a>
    <button class="header-menu-btn" aria-label="メニュー">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
```

- [ ] **Step 2: main.css にヘッダースタイルを追加する**

```css
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  padding: 20px 5%;
  transition: background var(--transition), padding var(--transition);
}

.site-header.scrolled {
  background: var(--color-main);
  padding: 12px 5%;
}

.header-inner {
  display: flex;
  align-items: center;
  gap: 40px;
}

.header-logo {
  flex-shrink: 0;
}

.header-nav {
  display: flex;
  gap: 32px;
  margin-left: auto;
}

.header-nav a {
  font-family: var(--font-en);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--color-white);
  letter-spacing: 0.05em;
  transition: color var(--transition);
}

.header-nav a:hover {
  color: var(--color-accent);
}

.header-cta {
  font-size: 0.8rem;
  font-weight: 700;
  padding: 10px 20px;
  background: var(--color-accent);
  color: var(--color-white);
  border-radius: var(--border-radius);
  white-space: nowrap;
  transition: opacity var(--transition);
}

.header-cta:hover {
  opacity: 0.85;
}

.header-menu-btn {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
}

.header-menu-btn span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--color-white);
}

@media (max-width: 768px) {
  .header-nav {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--color-main);
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 40px;
  }

  .header-nav.open {
    display: flex;
  }

  .header-nav a {
    font-size: 1.2rem;
  }

  .header-cta {
    display: none;
  }

  .header-menu-btn {
    display: flex;
    margin-left: auto;
    position: relative;
    z-index: 1001;
  }
}
```

- [ ] **Step 3: main.js に `initHeader()` を実装する**

```js
function initHeader() {
  const header = document.getElementById('site-header');
  const menuBtn = header.querySelector('.header-menu-btn');
  const nav = header.querySelector('.header-nav');

  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 50);
  });

  menuBtn.addEventListener('click', () => {
    nav.classList.toggle('open');
  });

  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => nav.classList.remove('open'));
  });
}
```

- [ ] **Step 4: ブラウザで確認する**
  - ヘッダーが画面上部に固定されている
  - スクロール後に背景が #000032 になる
  - モバイル幅（375px）でハンバーガーメニューが動作する

- [ ] **Step 5: コミットする**

```bash
git add .
git commit -m "feat: add fixed header with scroll behavior and mobile menu"
```

---

### Task 3: ヒーローセクション

**Files:**
- Modify: `index.html` — `<section class="hero">` 追加
- Modify: `assets/css/main.css` — ヒーロースタイル追加
- Modify: `assets/js/main.js` — `initScrollFade()` 実装

- [ ] **Step 1: index.html にヒーローセクションを追加する（`<header>` の直後）**

```html
<section class="hero" id="hero">
  <div class="hero-bg" style="background-image: url('assets/images/hero.jpg')"></div>
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <p class="hero-sub">スポーツを通じて、人生を切り拓く力を育む。</p>
    <h1 class="hero-title">やり抜く力と正しい努力で<br>才能を凌駕する</h1>
    <div class="hero-actions">
      <a href="#contact" class="btn-primary">無料体験を申し込む</a>
      <a href="#business" class="btn-secondary">サービスを見る</a>
    </div>
  </div>
</section>
```

- [ ] **Step 2: main.css にヒーロースタイルを追加する**

```css
.hero {
  position: relative;
  height: 100vh;
  min-height: 600px;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  transform: scale(1.05);
  transition: transform 0.1s linear;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 50, 0.6);
}

.hero-content {
  position: relative;
  z-index: 1;
  padding: 0 5%;
  max-width: 800px;
  color: var(--color-white);
}

.hero-sub {
  font-size: 1rem;
  letter-spacing: 0.1em;
  margin-bottom: 16px;
  opacity: 0.85;
}

.hero-title {
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 900;
  line-height: 1.2;
  margin-bottom: 40px;
  font-family: var(--font-ja);
}

.hero-actions {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.btn-primary {
  display: inline-block;
  padding: 16px 32px;
  background: var(--color-accent);
  color: var(--color-white);
  font-weight: 700;
  font-size: 0.95rem;
  border-radius: var(--border-radius);
  transition: opacity var(--transition);
}

.btn-primary:hover {
  opacity: 0.85;
}

.btn-secondary {
  display: inline-block;
  padding: 16px 32px;
  color: var(--color-white);
  font-weight: 600;
  font-size: 0.95rem;
  border-bottom: 2px solid var(--color-white);
  transition: border-color var(--transition);
}

.btn-secondary:hover {
  border-color: var(--color-accent);
}
```

- [ ] **Step 3: main.js の `initScrollFade()` を実装する（視差効果）**

```js
function initScrollFade() {
  const heroBg = document.querySelector('.hero-bg');
  const heroContent = document.querySelector('.hero-content');

  if (!heroBg) return;

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const heroHeight = document.querySelector('.hero').offsetHeight;
    if (scrollY < heroHeight) {
      heroBg.style.transform = `scale(1.05) translateY(${scrollY * 0.3}px)`;
      heroContent.style.opacity = 1 - (scrollY / heroHeight) * 1.5;
    }
  });
}
```

- [ ] **Step 4: ブラウザで確認する**
  - ヒーローが画面高さ100%表示されている
  - スクロール時に背景が視差効果で動き、テキストがフェードアウトする
  - CTAボタンが赤（#ee0044）で表示されている

- [ ] **Step 5: コミットする**

```bash
git add .
git commit -m "feat: add hero section with parallax scroll effect"
```

---

### Task 4: Missionセクション

**Files:**
- Modify: `index.html`
- Modify: `assets/css/main.css`

- [ ] **Step 1: index.html にMissionセクションを追加する**

```html
<section class="mission" id="mission">
  <div class="mission-inner">
    <div class="mission-text">
      <span class="section-label">MISSION</span>
      <h2 class="section-title" style="color: var(--color-white);">ミッション</h2>
      <p class="mission-body">
        私たちは、スポーツを通じて人材育成と社会貢献を実現することをミッションとしています。<br><br>
        やり抜く力（GRIT）と正しい努力で、すべての子どもたちが才能の壁を超えられると信じています。<br><br>
        コーチングの力で、グラウンドの外でも輝ける人間を育てていきます。
      </p>
    </div>
    <div class="mission-photo">
      <img src="assets/images/mission.jpg" alt="代表の写真">
    </div>
  </div>
</section>
```

- [ ] **Step 2: main.css にMissionスタイルを追加する**

```css
.mission {
  background: var(--color-main);
  padding: var(--section-padding);
}

.mission-inner {
  display: grid;
  grid-template-columns: 6fr 4fr;
  gap: 60px;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.mission-text {
  color: var(--color-white);
}

.mission-text .section-title {
  margin: 8px 0 32px;
}

.mission-body {
  font-size: 1rem;
  line-height: 1.9;
  color: rgba(255, 255, 255, 0.85);
}

.mission-photo {
  position: relative;
}

.mission-photo::before {
  content: '';
  position: absolute;
  bottom: -16px;
  right: -16px;
  width: 70%;
  height: 70%;
  border-bottom: 4px solid var(--color-accent);
  border-right: 4px solid var(--color-accent);
}

.mission-photo img {
  position: relative;
  z-index: 1;
  width: 100%;
  object-fit: cover;
  aspect-ratio: 3/4;
}

@media (max-width: 768px) {
  .mission-inner {
    grid-template-columns: 1fr;
  }

  .mission-photo {
    max-width: 320px;
    margin: 0 auto;
  }
}
```

- [ ] **Step 3: ブラウザで確認する**
  - ネイビー背景に白テキスト2カラムレイアウト
  - 写真右下に#ee0044のL字フレームが表示されている
  - モバイルで縦積みになっている

- [ ] **Step 4: コミットする**

```bash
git add .
git commit -m "feat: add mission section"
```

---

### Task 5: コーチ紹介セクション

**Files:**
- Modify: `index.html`
- Modify: `assets/css/main.css`

- [ ] **Step 1: index.html にコーチ紹介セクションを追加する**

```html
<section class="coach" id="coach">
  <div class="coach-inner">
    <div class="coach-photo-wrap">
      <div class="coach-photo-bg"></div>
      <img src="assets/images/coach.jpg" alt="コーチの写真" class="coach-photo">
    </div>
    <div class="coach-profile">
      <span class="section-label">COACH</span>
      <h2 class="section-title">コーチ紹介</h2>
      <h3 class="coach-name">
        <span class="coach-name-ja">矢玖 佳幸</span>
        <span class="coach-name-en">Yoshiyuki Yagyu</span>
      </h3>
      <div class="coach-divider"></div>
      <p class="coach-role">代表取締役 / ヘッドコーチ</p>
      <p class="coach-credentials">UEFA B ライセンス保持 / メンタルコーチング認定</p>
      <p class="coach-bio">
        ここにコーチのプロフィール本文が入ります。経歴、指導歴、指導哲学などを4〜6行で記述します。
        スポーツを通じた人材育成への想いや、これまでの実績についても触れてください。
      </p>
      <div class="coach-sns">
        <a href="https://www.instagram.com/" target="_blank" rel="noopener" class="coach-sns-link">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          Instagram
        </a>
        <a href="https://www.youtube.com/" target="_blank" rel="noopener" class="coach-sns-link">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23.495 6.205a3.007 3.007 0 0 0-2.088-2.088c-1.87-.501-9.396-.501-9.396-.501s-7.507-.01-9.396.501A3.007 3.007 0 0 0 .527 6.205a31.247 31.247 0 0 0-.522 5.805 31.247 31.247 0 0 0 .522 5.783 3.007 3.007 0 0 0 2.088 2.088c1.868.502 9.396.502 9.396.502s7.506 0 9.396-.502a3.007 3.007 0 0 0 2.088-2.088 31.247 31.247 0 0 0 .5-5.783 31.247 31.247 0 0 0-.5-5.805zM9.609 15.601V8.408l6.264 3.602z"/></svg>
          YouTube
        </a>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: main.css にコーチスタイルを追加する**

```css
.coach {
  background: var(--color-white);
  padding: var(--section-padding);
}

.coach-inner {
  display: grid;
  grid-template-columns: 4fr 6fr;
  gap: 60px;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.coach-photo-wrap {
  position: relative;
}

.coach-photo-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 60%;
  height: 80%;
  background: var(--color-main);
}

.coach-photo {
  position: relative;
  z-index: 1;
  width: 100%;
  object-fit: cover;
  aspect-ratio: 3/4;
  margin: 20px 20px 0 20px;
  max-width: calc(100% - 20px);
}

.coach-name {
  margin: 16px 0 20px;
}

.coach-name-ja {
  display: block;
  font-size: 1.8rem;
  font-weight: 700;
}

.coach-name-en {
  display: block;
  font-family: var(--font-en);
  font-size: 1rem;
  font-weight: 400;
  color: #666;
  margin-top: 4px;
}

.coach-divider {
  width: 48px;
  height: 3px;
  background: var(--color-accent);
  margin-bottom: 16px;
}

.coach-role {
  font-weight: 700;
  margin-bottom: 4px;
}

.coach-credentials {
  font-size: 0.85rem;
  color: #666;
  margin-bottom: 24px;
}

.coach-bio {
  line-height: 1.9;
  margin-bottom: 32px;
}

.coach-sns {
  display: flex;
  gap: 20px;
}

.coach-sns-link {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--color-main);
  transition: color var(--transition);
}

.coach-sns-link:hover {
  color: var(--color-accent);
}

@media (max-width: 768px) {
  .coach-inner {
    grid-template-columns: 1fr;
  }

  .coach-photo-wrap {
    max-width: 280px;
    margin: 0 auto;
  }
}
```

- [ ] **Step 3: ブラウザで確認する**
  - 写真左上に#000032のL字帯が表示されている
  - 名前下に#ee0044のアクセントラインがある
  - SNSリンクが並んでいる

- [ ] **Step 4: コミットする**

```bash
git add .
git commit -m "feat: add coach profile section"
```

---

### Task 6: 事業内容セクション

**Files:**
- Modify: `index.html`
- Modify: `assets/css/main.css`

- [ ] **Step 1: index.html に事業内容セクションを追加する**

```html
<section class="business" id="business">
  <div class="business-inner">
    <div class="business-header">
      <span class="section-label">BUSINESS</span>
      <h2 class="section-title" style="color: var(--color-white);">事業内容</h2>
    </div>
    <div class="business-grid">
      <div class="business-card">
        <div class="business-icon">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/><path d="M2 12h20"/></svg>
        </div>
        <h3 class="business-name">サッカースクール</h3>
        <p class="business-desc">子どもたちの個性を活かした指導で、技術と人間力を同時に育みます。</p>
        <a href="#" class="business-link">詳しく見る →</a>
      </div>
      <div class="business-card">
        <div class="business-icon">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 12l2 2 4-4"/><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2z"/></svg>
        </div>
        <h3 class="business-name">メンタルスキル</h3>
        <p class="business-desc">GRITの哲学に基づいたメンタルコーチングで、やり抜く力を引き出します。</p>
        <a href="#" class="business-link">詳しく見る →</a>
      </div>
      <div class="business-card">
        <div class="business-icon">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
        </div>
        <h3 class="business-name">選手マネジメント</h3>
        <p class="business-desc">選手のキャリアを長期的な視点でサポートし、夢の実現を共に目指します。</p>
        <a href="#" class="business-link">詳しく見る →</a>
      </div>
      <div class="business-card">
        <div class="business-icon">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
        </div>
        <h3 class="business-name">イベント企画</h3>
        <p class="business-desc">スポーツの力で人々をつなぐイベントを企画・運営します。</p>
        <a href="#" class="business-link">詳しく見る →</a>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: main.css に事業内容スタイルを追加する**

```css
.business {
  background: var(--color-main);
  padding: var(--section-padding);
}

.business-inner {
  max-width: 1200px;
  margin: 0 auto;
}

.business-header {
  margin-bottom: 48px;
}

.business-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: rgba(255,255,255,0.1);
}

.business-card {
  padding: 40px 32px;
  background: var(--color-main);
  transition: background var(--transition);
}

.business-card:hover {
  background: rgba(255,255,255,0.05);
}

.business-icon {
  color: var(--color-white);
  margin-bottom: 20px;
}

.business-name {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--color-white);
  margin-bottom: 12px;
}

.business-desc {
  font-size: 0.9rem;
  color: var(--color-gray-text);
  line-height: 1.7;
  margin-bottom: 20px;
}

.business-link {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--color-accent);
  transition: opacity var(--transition);
}

.business-link:hover {
  opacity: 0.8;
}

@media (max-width: 1024px) {
  .business-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .business-grid {
    grid-template-columns: 1fr;
  }
}
```

- [ ] **Step 3: ブラウザで確認する**
  - 4カラムグリッドでカードが並んでいる
  - カード間に薄いセパレーターが入っている
  - 「詳しく見る」リンクが#ee0044

- [ ] **Step 4: コミットする**

```bash
git add .
git commit -m "feat: add business section with 4-column grid"
```

---

### Task 7: コース紹介セクション

**Files:**
- Modify: `index.html`
- Modify: `assets/css/main.css`

- [ ] **Step 1: index.html にコース紹介セクションを追加する（事業内容の直後）**

```html
<section class="course" id="course">
  <div class="course-inner">
    <div class="course-header">
      <span class="section-label">COURSE</span>
      <h2 class="section-title">コース紹介</h2>
    </div>
    <div class="course-grid">
      <div class="course-card">
        <div class="course-accent-bar"></div>
        <div class="course-card-body">
          <h3 class="course-name">ジュニアコース</h3>
          <p class="course-target">対象：小学1年生〜6年生</p>
          <p class="course-desc">
            基礎技術の習得とチームプレーを通じて、サッカーの楽しさと自立心を育みます。
            週2回の練習で確実なスキルアップを目指します。
          </p>
          <p class="course-price"><span class="course-price-num">¥8,800</span><span class="course-price-unit"> / 月（税込）</span></p>
          <a href="#contact" class="btn-primary">無料体験を申し込む</a>
        </div>
      </div>
      <div class="course-card">
        <div class="course-accent-bar"></div>
        <div class="course-card-body">
          <h3 class="course-name">メンタルコーチングコース</h3>
          <p class="course-target">対象：中学生以上・大人</p>
          <p class="course-desc">
            GRITの哲学に基づき、やり抜く力・集中力・自己管理能力を個別セッションで引き出します。
            スポーツ・学業・ビジネスあらゆる場面に活かせます。
          </p>
          <p class="course-price"><span class="course-price-num">¥22,000</span><span class="course-price-unit"> / 月（税込）</span></p>
          <a href="#contact" class="btn-primary">無料体験を申し込む</a>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: main.css にコース紹介スタイルを追加する**

```css
.course {
  background: var(--color-white);
  padding: var(--section-padding);
}

.course-inner {
  max-width: 1200px;
  margin: 0 auto;
}

.course-header {
  margin-bottom: 48px;
}

.course-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px;
}

.course-card {
  border: 1px solid #e8e8e8;
  border-radius: 8px;
  overflow: hidden;
  transition: box-shadow var(--transition);
}

.course-card:hover {
  box-shadow: 0 8px 32px rgba(0, 0, 50, 0.1);
}

.course-accent-bar {
  height: 4px;
  background: var(--color-accent);
}

.course-card-body {
  padding: 36px;
}

.course-name {
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 8px;
}

.course-target {
  font-size: 0.85rem;
  color: #666;
  margin-bottom: 16px;
}

.course-desc {
  line-height: 1.8;
  margin-bottom: 24px;
}

.course-price {
  margin-bottom: 28px;
}

.course-price-num {
  font-size: 2rem;
  font-weight: 700;
  color: var(--color-accent);
  font-family: var(--font-en);
}

.course-price-unit {
  font-size: 0.9rem;
  color: #666;
}

@media (max-width: 768px) {
  .course-grid {
    grid-template-columns: 1fr;
  }
}
```

- [ ] **Step 3: ブラウザで確認する**
  - カード上部に#ee0044のアクセントバーがある
  - 料金が#ee0044の大きな数字で表示されている
  - 「無料体験を申し込む」ボタンが各カードにある

- [ ] **Step 4: コミットする**

```bash
git add .
git commit -m "feat: add course section with 2 course cards"
```

---

### Task 8: 保護者・選手の声セクション

**Files:**
- Modify: `index.html`
- Modify: `assets/css/main.css`
- Modify: `assets/js/main.js` — `initCarousel()` 実装

- [ ] **Step 1: index.html に保護者・選手の声セクションを追加する**

```html
<section class="voice" id="voice">
  <div class="voice-inner">
    <div class="voice-header">
      <span class="section-label">VOICE</span>
      <h2 class="section-title" style="color: var(--color-white);">保護者・選手の声</h2>
    </div>
    <div class="voice-carousel" id="voiceCarousel">
      <div class="voice-track" id="voiceTrack">
        <div class="voice-card">
          <div class="voice-quote">"</div>
          <p class="voice-text">息子がサッカーを始めて半年。技術だけでなく、諦めない心が育ったと感じています。練習に行くのを毎回楽しみにしています。</p>
          <div class="voice-author">
            <img src="assets/images/voice-1.jpg" alt="保護者の写真" class="voice-avatar">
            <div>
              <p class="voice-name">Aさん（保護者）</p>
              <p class="voice-meta">小学3年生のお子様</p>
            </div>
          </div>
        </div>
        <div class="voice-card">
          <div class="voice-quote">"</div>
          <p class="voice-text">メンタルコーチングを受けて、試合でのプレッシャーへの対処法が変わりました。自分の強みを活かせるようになってきました。</p>
          <div class="voice-author">
            <img src="assets/images/voice-2.jpg" alt="選手の写真" class="voice-avatar">
            <div>
              <p class="voice-name">Bさん（中学2年生）</p>
              <p class="voice-meta">メンタルコーチングコース</p>
            </div>
          </div>
        </div>
        <div class="voice-card">
          <div class="voice-quote">"</div>
          <p class="voice-text">コーチの熱意と丁寧な指導に感謝しています。子どもが自ら練習するようになり、親としてとても嬉しいです。</p>
          <div class="voice-author">
            <img src="assets/images/voice-3.jpg" alt="保護者の写真" class="voice-avatar">
            <div>
              <p class="voice-name">Cさん（保護者）</p>
              <p class="voice-meta">小学5年生のお子様</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="voice-dots" id="voiceDots">
      <button class="voice-dot active" data-index="0"></button>
      <button class="voice-dot" data-index="1"></button>
      <button class="voice-dot" data-index="2"></button>
    </div>
  </div>
</section>
```

- [ ] **Step 2: main.css に保護者の声スタイルを追加する**

```css
.voice {
  background: var(--color-main);
  padding: var(--section-padding);
}

.voice-inner {
  max-width: 1200px;
  margin: 0 auto;
}

.voice-header {
  margin-bottom: 48px;
}

.voice-carousel {
  overflow: hidden;
}

.voice-track {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  transition: transform 0.4s ease;
}

.voice-card {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  padding: 36px;
  border-radius: 8px;
}

.voice-quote {
  font-size: 4rem;
  line-height: 1;
  color: var(--color-accent);
  font-family: serif;
  margin-bottom: 16px;
}

.voice-text {
  color: rgba(255,255,255,0.85);
  line-height: 1.8;
  margin-bottom: 28px;
}

.voice-author {
  display: flex;
  align-items: center;
  gap: 16px;
}

.voice-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
  background: rgba(255,255,255,0.1);
}

.voice-name {
  font-weight: 700;
  color: var(--color-white);
  font-size: 0.9rem;
}

.voice-meta {
  font-size: 0.8rem;
  color: var(--color-gray-text);
}

.voice-dots {
  display: none;
  justify-content: center;
  gap: 8px;
  margin-top: 24px;
}

.voice-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,0.3);
  border: none;
  cursor: pointer;
  transition: background var(--transition);
}

.voice-dot.active {
  background: var(--color-accent);
}

@media (max-width: 768px) {
  .voice-track {
    grid-template-columns: 100%;
  }

  .voice-carousel {
    touch-action: pan-y;
  }

  .voice-dots {
    display: flex;
  }
}
```

- [ ] **Step 3: main.js に `initCarousel()` を実装する**

```js
function initCarousel() {
  const track = document.getElementById('voiceTrack');
  const dots = document.querySelectorAll('.voice-dot');

  if (!track || window.innerWidth > 768) return;

  let currentIndex = 0;
  let startX = 0;
  let isDragging = false;

  function goTo(index) {
    currentIndex = Math.max(0, Math.min(index, dots.length - 1));
    track.style.transform = `translateX(-${currentIndex * 100}%)`;
    dots.forEach((dot, i) => dot.classList.toggle('active', i === currentIndex));
  }

  dots.forEach(dot => {
    dot.addEventListener('click', () => goTo(parseInt(dot.dataset.index)));
  });

  track.addEventListener('touchstart', e => {
    startX = e.touches[0].clientX;
    isDragging = true;
  });

  track.addEventListener('touchend', e => {
    if (!isDragging) return;
    const diff = startX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) goTo(currentIndex + (diff > 0 ? 1 : -1));
    isDragging = false;
  });
}
```

- [ ] **Step 4: ブラウザで確認する**
  - PCで3カラムのカードが並んでいる
  - モバイルでスワイプカルーセルが動作する
  - クォートマーク「"」が#ee0044で表示されている

- [ ] **Step 5: コミットする**

```bash
git add .
git commit -m "feat: add voice section with mobile carousel"
```

---

### Task 9: ブログ/お知らせセクション

**Files:**
- Modify: `index.html`
- Modify: `assets/css/main.css`

- [ ] **Step 1: index.html にブログセクションを追加する**

```html
<section class="blog" id="blog">
  <div class="blog-inner">
    <div class="blog-header">
      <span class="section-label">BLOG / NEWS</span>
      <h2 class="section-title">ブログ・お知らせ</h2>
    </div>
    <div class="blog-grid">
      <article class="blog-card">
        <a href="#">
          <div class="blog-thumb">
            <img src="assets/images/blog-1.jpg" alt="記事1">
          </div>
          <div class="blog-card-body">
            <span class="blog-tag">お知らせ</span>
            <h3 class="blog-title">皆様へのご挨拶</h3>
            <p class="blog-date">2024.04.15</p>
          </div>
        </a>
      </article>
      <article class="blog-card">
        <a href="#">
          <div class="blog-thumb">
            <img src="assets/images/blog-2.jpg" alt="記事2">
          </div>
          <div class="blog-card-body">
            <span class="blog-tag">ブログ</span>
            <h3 class="blog-title">GRITとは何か？やり抜く力について</h3>
            <p class="blog-date">2024.05.01</p>
          </div>
        </a>
      </article>
      <article class="blog-card">
        <a href="#">
          <div class="blog-thumb">
            <img src="assets/images/blog-3.jpg" alt="記事3">
          </div>
          <div class="blog-card-body">
            <span class="blog-tag">ブログ</span>
            <h3 class="blog-title">子どもの潜在能力を引き出すコーチングとは</h3>
            <p class="blog-date">2024.05.20</p>
          </div>
        </a>
      </article>
    </div>
    <div class="blog-more">
      <a href="/blog" class="blog-more-link">すべての記事を見る →</a>
    </div>
  </div>
</section>
```

- [ ] **Step 2: main.css にブログスタイルを追加する**

```css
.blog {
  background: var(--color-white);
  padding: var(--section-padding);
}

.blog-inner {
  max-width: 1200px;
  margin: 0 auto;
}

.blog-header {
  margin-bottom: 48px;
}

.blog-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  margin-bottom: 40px;
}

.blog-card a {
  display: block;
  color: inherit;
}

.blog-thumb {
  overflow: hidden;
  aspect-ratio: 16/9;
  background: var(--color-gray-light);
}

.blog-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.blog-card:hover .blog-thumb img {
  transform: scale(1.05);
}

.blog-card-body {
  padding: 20px 0;
}

.blog-tag {
  display: inline-block;
  padding: 3px 10px;
  background: var(--color-accent);
  color: var(--color-white);
  font-size: 0.75rem;
  font-weight: 700;
  margin-bottom: 10px;
  border-radius: 2px;
}

.blog-title {
  font-size: 1rem;
  font-weight: 700;
  line-height: 1.5;
  margin-bottom: 8px;
  transition: color var(--transition);
}

.blog-card:hover .blog-title {
  color: var(--color-accent);
}

.blog-date {
  font-size: 0.8rem;
  color: #999;
  font-family: var(--font-en);
}

.blog-more {
  text-align: right;
}

.blog-more-link {
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--color-accent);
  transition: opacity var(--transition);
}

.blog-more-link:hover {
  opacity: 0.8;
}

@media (max-width: 768px) {
  .blog-grid {
    grid-template-columns: 1fr;
  }
}
```

- [ ] **Step 3: ブラウザで確認する**
  - 3カラムグリッドでカードが並んでいる
  - カテゴリタグが#ee0044背景で表示されている
  - 「すべての記事を見る」リンクが右寄せで#ee0044

- [ ] **Step 4: コミットする**

```bash
git add .
git commit -m "feat: add blog/news section with 3-column grid"
```

---

### Task 10: CTAセクション＋フッター

**Files:**
- Modify: `index.html`
- Modify: `assets/css/main.css`

- [ ] **Step 1: index.html にCTAセクションを追加する**

```html
<section class="cta" id="contact">
  <div class="cta-inner">
    <h2 class="cta-title">まずは無料体験から</h2>
    <p class="cta-sub">お子さまの可能性を、一緒に広げましょう。</p>
    <div class="cta-actions">
      <a href="mailto:info@gritcoaching.co.jp" class="cta-btn-primary">無料体験を申し込む</a>
      <a href="mailto:info@gritcoaching.co.jp" class="cta-btn-secondary">お問い合わせ</a>
    </div>
  </div>
</section>
```

- [ ] **Step 2: index.html にフッターを追加する**

```html
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="assets/images/logo.svg" alt="グリットコーチング" height="36">
      <p class="footer-tagline">やり抜く力と正しい努力で才能を凌駕する。</p>
    </div>
    <nav class="footer-nav">
      <a href="#mission">Mission</a>
      <a href="#business">Business</a>
      <a href="#blog">Blog</a>
      <a href="#company">Company</a>
      <a href="#contact">Contact</a>
    </nav>
    <div class="footer-sns">
      <a href="https://www.instagram.com/" target="_blank" rel="noopener" aria-label="Instagram">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
      </a>
      <a href="https://www.youtube.com/" target="_blank" rel="noopener" aria-label="YouTube">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23.495 6.205a3.007 3.007 0 0 0-2.088-2.088c-1.87-.501-9.396-.501-9.396-.501s-7.507-.01-9.396.501A3.007 3.007 0 0 0 .527 6.205a31.247 31.247 0 0 0-.522 5.805 31.247 31.247 0 0 0 .522 5.783 3.007 3.007 0 0 0 2.088 2.088c1.868.502 9.396.502 9.396.502s7.506 0 9.396-.502a3.007 3.007 0 0 0 2.088-2.088 31.247 31.247 0 0 0 .5-5.783 31.247 31.247 0 0 0-.5-5.805zM9.609 15.601V8.408l6.264 3.602z"/></svg>
      </a>
    </div>
  </div>
  <div class="footer-bottom">
    <p>© 2024 グリットコーチング・ジャパン株式会社</p>
    <a href="/privacy">プライバシーポリシー</a>
  </div>
</footer>
```

- [ ] **Step 3: main.css にCTAとフッタースタイルを追加する**

```css
/* CTA */
.cta {
  background: linear-gradient(135deg, var(--color-accent), #bb0033);
  padding: 100px 5%;
  text-align: center;
}

.cta-inner {
  max-width: 700px;
  margin: 0 auto;
}

.cta-title {
  font-size: clamp(1.8rem, 4vw, 3rem);
  font-weight: 900;
  color: var(--color-white);
  margin-bottom: 16px;
}

.cta-sub {
  font-size: 1.1rem;
  color: rgba(255,255,255,0.9);
  margin-bottom: 48px;
}

.cta-actions {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

.cta-btn-primary {
  display: inline-block;
  padding: 18px 40px;
  background: var(--color-white);
  color: var(--color-main);
  font-weight: 700;
  font-size: 1rem;
  border-radius: var(--border-radius);
  transition: opacity var(--transition);
}

.cta-btn-primary:hover {
  opacity: 0.9;
}

.cta-btn-secondary {
  display: inline-block;
  padding: 18px 40px;
  border: 2px solid var(--color-white);
  color: var(--color-white);
  font-weight: 700;
  font-size: 1rem;
  border-radius: var(--border-radius);
  transition: background var(--transition);
}

.cta-btn-secondary:hover {
  background: rgba(255,255,255,0.1);
}

/* Footer */
.site-footer {
  background: var(--color-main);
  padding: 60px 5% 0;
}

.footer-inner {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 60px;
  align-items: start;
  max-width: 1200px;
  margin: 0 auto;
  padding-bottom: 40px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.footer-tagline {
  font-size: 0.85rem;
  color: rgba(255,255,255,0.5);
  margin-top: 12px;
}

.footer-nav {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-nav a {
  font-family: var(--font-en);
  font-size: 0.85rem;
  font-weight: 600;
  color: rgba(255,255,255,0.7);
  letter-spacing: 0.05em;
  transition: color var(--transition);
}

.footer-nav a:hover {
  color: var(--color-white);
}

.footer-sns {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.footer-sns a {
  color: var(--color-accent);
  transition: opacity var(--transition);
}

.footer-sns a:hover {
  opacity: 0.8;
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0;
  max-width: 1200px;
  margin: 0 auto;
  font-size: 0.8rem;
  color: rgba(255,255,255,0.4);
}

.footer-bottom a {
  color: rgba(255,255,255,0.4);
  transition: color var(--transition);
}

.footer-bottom a:hover {
  color: var(--color-white);
}

@media (max-width: 768px) {
  .footer-inner {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .footer-nav {
    flex-direction: row;
    flex-wrap: wrap;
  }

  .footer-sns {
    flex-direction: row;
  }

  .footer-bottom {
    flex-direction: column;
    gap: 8px;
    text-align: center;
  }
}
```

- [ ] **Step 4: ブラウザで確認する**
  - CTAセクションが#ee0044背景でグラデーション
  - ボタン2つが横並びで中央寄せ
  - フッターが3カラムレイアウト
  - フッターSNSアイコンが#ee0044

- [ ] **Step 5: コミットする**

```bash
git add .
git commit -m "feat: add CTA section and footer"
```

---

### Task 11: 最終確認・レスポンシブ調整

**Files:**
- Modify: `assets/css/main.css` — 微調整
- Modify: `index.html` — 会社概要セクション追加（id="company"）

- [ ] **Step 1: index.html にシンプルな会社概要セクションを追加する（フッターの直前）**

```html
<section class="company" id="company">
  <div class="company-inner">
    <span class="section-label">COMPANY</span>
    <h2 class="section-title">会社概要</h2>
    <table class="company-table">
      <tr><th>会社名</th><td>グリットコーチング・ジャパン株式会社</td></tr>
      <tr><th>代表取締役</th><td>（代表者名）</td></tr>
      <tr><th>取締役</th><td>（取締役名）</td></tr>
      <tr><th>所在地</th><td>（住所）</td></tr>
      <tr><th>設立</th><td>（設立年月）</td></tr>
    </table>
  </div>
</section>
```

- [ ] **Step 2: main.css に会社概要スタイルを追加する**

```css
.company {
  background: var(--color-white);
  padding: var(--section-padding);
}

.company-inner {
  max-width: 800px;
  margin: 0 auto;
}

.company-inner .section-title {
  margin: 8px 0 40px;
}

.company-table {
  width: 100%;
  border-collapse: collapse;
}

.company-table tr {
  border-bottom: 1px solid #e8e8e8;
}

.company-table th,
.company-table td {
  padding: 16px 0;
  text-align: left;
  font-size: 0.95rem;
}

.company-table th {
  width: 160px;
  font-weight: 700;
  color: var(--color-main);
}

.company-table td {
  color: #555;
}

@media (max-width: 480px) {
  .company-table th,
  .company-table td {
    display: block;
    width: 100%;
  }

  .company-table th {
    padding-bottom: 4px;
  }

  .company-table td {
    padding-top: 0;
  }
}
```

- [ ] **Step 3: 全セクションをPC・タブレット（768px）・モバイル（375px）で確認する**
  - ヘッダー固定＋スクロール変化
  - ヒーロー視差効果
  - 全セクションのレイアウト崩れなし
  - モバイルカルーセルのスワイプ動作

- [ ] **Step 4: 最終コミット**

```bash
git add .
git commit -m "feat: add company section and final responsive polish"
```

---

## 注意事項

- **画像ファイル：** `assets/images/` に実素材を配置してから確認してください。画像がない状態ではアスペクト比確保のためグレー背景が表示されます。
- **コーチ情報・コース料金：** プレースホルダーテキストを実際の情報に差し替えてください。
- **SNSリンク：** 実際のInstagram/YouTubeのURLに変更してください。
- **お問い合わせリンク：** 実際のフォームURLに変更してください（現在は `mailto:` を使用）。
- **ブログ連携：** 現在は静的なHTMLカードです。CMSと連携する場合はサーバーサイドのテンプレート化が別途必要です。
