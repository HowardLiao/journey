import os

OUTPUT_DIR = "/Users/howardliao/Desktop/HermesAgent/PortFilio/journey"
HTML_PATH = os.path.join(OUTPUT_DIR, "index.html")
README_PATH = os.path.join(OUTPUT_DIR, "README.md")

html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>組織從零到一的降維突圍實戰報告 ｜ Howard Liao Ph.D.</title>
  <meta name="description" content="一場在「隕石開發」與「老臣防衛」夾縫中的組織救贖心路歷程與治理復盤 · 報告人 Howard Liao Ph.D.">
  <link rel="icon" href="assets/howard-liao-avatar-256.png" type="image/png">
  <style>
    :root {
      --bg-primary: #FFFFFF;
      --bg-warm: #FFFBEB;
      --bg-alt: #F8FAFC;
      --border-color: #E2E8F0;
      --text-primary: #2D3748;
      --text-muted: #718096;
      --rust: #A83212;
      --warm-orange: #DE5814;
      --amber: #D97706;
      --charcoal: #2D3748;
      --font-sans: -apple-system, BlinkMacSystemFont, "PingFang TC", "Helvetica Neue", Arial, sans-serif;
      --font-mono: Menlo, Monaco, Consolas, "Courier New", monospace;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }
    body {
      font-family: var(--font-sans);
      background-color: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.6;
      padding-bottom: 90px;
      overflow-x: hidden;
    }
    .watermark-overlay {
      position: fixed !important;
      top: 0 !important;
      left: 0 !important;
      width: 100vw !important;
      height: 100vh !important;
      pointer-events: none !important;
      z-index: 999999 !important;
      opacity: 0.045 !important;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='260' height='140' viewBox='0 0 260 140'%3E%3Ctext x='20' y='75' fill='%231C1917' font-family='Arial' font-weight='700' font-size='14' transform='rotate(-22 130 75)' letter-spacing='2'%3EHoward Liao Ph.D.%3C/text%3E%3C/svg%3E") !important;
    }
    header.masthead {
      border-bottom: 2px solid var(--warm-orange);
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 1000;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .masthead-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--rust);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .masthead-nav {
      display: flex;
      gap: 12px;
      align-items: center;
    }
    .nav-btn {
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      color: var(--text-primary);
      background: var(--bg-alt);
      border: 1px solid var(--border-color);
      transition: all 0.2s ease;
    }
    .nav-btn:hover, .nav-btn.active {
      background: var(--warm-orange);
      color: #FFF;
      border-color: var(--warm-orange);
    }
    .hero {
      padding: 48px 24px 36px;
      max-width: 1040px;
      margin: 0 auto;
      text-align: center;
    }
    .badge-label {
      display: inline-block;
      padding: 4px 12px;
      background: var(--bg-warm);
      border: 1px solid var(--amber);
      color: var(--rust);
      font-size: 0.82rem;
      font-weight: 700;
      border-radius: 16px;
      margin-bottom: 16px;
      letter-spacing: 0.5px;
    }
    .hero h1 {
      font-size: 2.3rem;
      color: var(--rust);
      font-weight: 800;
      line-height: 1.25;
      margin-bottom: 14px;
    }
    .hero p.lead {
      font-size: 1.15rem;
      color: var(--charcoal);
      max-width: 820px;
      margin: 0 auto 20px;
      line-height: 1.5;
    }
    .author-strip {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin-top: 18px;
    }
    .author-avatar {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      border: 2px solid var(--warm-orange);
    }
    .author-text {
      text-align: left;
      font-size: 0.88rem;
    }
    .author-name {
      font-weight: 700;
      color: var(--rust);
    }
    .author-role {
      color: var(--text-muted);
      font-size: 0.8rem;
    }

    .container {
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 20px 40px;
    }
    .section-title {
      font-size: 1.5rem;
      color: var(--rust);
      font-weight: 800;
      margin: 40px 0 16px;
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 1.5px solid var(--border-color);
      padding-bottom: 8px;
    }
    .callout {
      background-color: var(--bg-warm);
      border-left: 4.5px solid var(--warm-orange);
      padding: 16px 20px;
      border-radius: 0 8px 8px 0;
      margin: 20px 0;
    }
    .callout-title {
      font-weight: 700;
      color: var(--rust);
      font-size: 1.05rem;
      margin-bottom: 6px;
    }
    .callout p {
      font-size: 0.95rem;
      color: var(--charcoal);
      line-height: 1.6;
    }

    .bento-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin: 24px 0;
    }
    .bento-card {
      background: var(--bg-alt);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .bento-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    }
    .bento-num {
      font-size: 2.1rem;
      font-weight: 800;
      color: var(--warm-orange);
      font-family: var(--font-mono);
      text-align: right;
      line-height: 1;
      margin-bottom: 8px;
    }
    .bento-label {
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--rust);
      margin-bottom: 4px;
    }
    .bento-desc {
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.4;
    }

    .timeline {
      position: relative;
      margin: 30px 0;
      padding-left: 28px;
      border-left: 3px solid var(--warm-orange);
    }
    .timeline-node {
      position: relative;
      margin-bottom: 32px;
    }
    .timeline-node::before {
      content: "";
      position: absolute;
      left: -35.5px;
      top: 4px;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--bg-primary);
      border: 3px solid var(--rust);
    }
    .timeline-node.highlight::before {
      background: var(--warm-orange);
    }
    .node-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--rust);
      margin-bottom: 4px;
    }
    .node-tag {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      background: var(--bg-warm);
      color: var(--amber);
      border: 1px solid var(--amber);
      padding: 2px 8px;
      border-radius: 12px;
      margin-bottom: 8px;
    }
    .node-body {
      font-size: 0.92rem;
      color: var(--charcoal);
      line-height: 1.6;
    }

    .table-scroll-wrap {
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin: 20px 0;
      border-radius: 8px;
      border: 1px solid var(--border-color);
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }
    th {
      background: var(--charcoal);
      color: #FFF;
      padding: 10px 14px;
      text-align: left;
      font-weight: 700;
      white-space: nowrap;
    }
    td {
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-color);
      vertical-align: top;
    }
    tr:nth-child(even) td {
      background-color: var(--bg-alt);
    }
    .text-right {
      text-align: right;
      font-family: var(--font-mono);
      font-weight: 700;
    }

    .doc-card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 18px;
      margin: 24px 0;
    }
    .doc-card {
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 20px;
      background: var(--bg-primary);
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .doc-icon {
      font-size: 2rem;
      margin-bottom: 8px;
    }
    .doc-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--rust);
      margin-bottom: 6px;
    }
    .doc-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 16px;
      line-height: 1.4;
    }
    .doc-actions {
      display: flex;
      gap: 10px;
    }
    .btn-download {
      flex: 1;
      text-align: center;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      text-decoration: none;
      color: #FFF;
      background: var(--warm-orange);
      transition: background 0.2s;
    }
    .btn-download:hover {
      background: var(--rust);
    }

    .mobile-bottom-dock {
      position: fixed !important;
      bottom: 0 !important;
      left: 0 !important;
      right: 0 !important;
      z-index: 2147483647 !important;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(20px);
      border-top: 1px solid var(--border-color);
      display: flex;
      justify-content: space-around;
      align-items: center;
      padding: 8px 12px;
      box-shadow: 0 -4px 16px rgba(0,0,0,0.06);
    }
    .dock-btn {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-decoration: none;
      color: var(--text-muted);
      font-size: 0.72rem;
      font-weight: 600;
      gap: 2px;
    }
    .dock-btn.active, .dock-btn:hover {
      color: var(--warm-orange);
    }

    footer.site-footer {
      border-top: 1px solid var(--border-color);
      padding: 30px 20px;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
      background: var(--bg-alt);
    }

    @media (max-width: 768px) {
      .hero h1 { font-size: 1.7rem; }
      .hero p.lead { font-size: 1rem; }
      .masthead-nav { display: none; }
    }
  </style>
</head>
<body>
<div class="watermark-overlay"></div>

<header class="masthead">
  <div class="masthead-title">
    <span>🧭 組織突圍實戰庫</span>
    <span style="font-size: 0.8rem; font-weight: 400; color: var(--text-muted);">Howard Liao Ph.D.</span>
  </div>
  <nav class="masthead-nav">
    <a href="#expert" class="nav-btn">達人觀點</a>
    <a href="#phases" class="nav-btn">九大階段</a>
    <a href="#teams" class="nav-btn">三大團隊</a>
    <a href="#tools" class="nav-btn">武器庫</a>
    <a href="#downloads" class="nav-btn">報告下載</a>
  </nav>
</header>

<main>
  <section class="hero">
    <div class="badge-label">EXECUTIVE TURNAROUND WHITE PAPER ｜ MILAN WARM AMBER</div>
    <h1>組織從零到一的降維突圍實戰報告</h1>
    <p class="lead">
      一場在「隕石開發」與「老臣防衛」夾縫中，以極簡工具給團隊穿上防彈衣的心路歷程與治理復盤
    </p>
    <div class="author-strip">
      <img src="assets/howard-liao-avatar-256.png" alt="Howard Liao Ph.D." class="author-avatar" onerror="this.style.display='none'">
      <div class="author-text">
        <div class="author-name">報告人：Howard Liao Ph.D.</div>
        <div class="author-role">前進部署型戰時高管 · 企業架構與組織教練</div>
      </div>
    </div>
  </section>

  <div class="container">
    <!-- Quote -->
    <div class="callout" id="expert">
      <div class="callout-title">【達人精闢評析】Ben Horowitz × John Kotter 實戰高管哲學</div>
      <p>
        <strong>「不是什麼光榮厲害的升級，單純就是他們是 0，隨便加都有效。」</strong><br>
        在承平時期，管理者談願景、談優雅架構、談大一統 4in1 藍圖；但在戰時，面對的是隨時砸過來的隕石、互相猜忌的老臣與只會討好老闆的傳話筒。此時任何高調都是空談，唯一有效的是「0.1% DAU 對賭算盤」爭取生存沙盒，用「三好一支援」與「指標字典」給基層穿上防彈衣，並以極具政治智慧的「組織絕緣層」隔離老闆情緒風暴，完成從 0 到 1 的防禦型落地。
      </p>
    </div>

    <!-- Bento Grid Metrics -->
    <div class="bento-grid">
      <div class="bento-card">
        <div class="bento-num">+0.1%</div>
        <div class="bento-label">DAU 商業對賭指標</div>
        <div class="bento-desc">H1 增加 150 人，月營收增益 NT$ 2,475,000，打平 35 人工程開銷。</div>
      </div>
      <div class="bento-card">
        <div class="bento-num">35 人</div>
        <div class="bento-label">跨職能組織突圍</div>
        <div class="bento-desc">涵蓋企劃營運 10 人、前端 9 人、後端與 DBA 14 人全體定位。</div>
      </div>
      <div class="bento-card">
        <div class="bento-num">3 波次</div>
        <div class="bento-label">加權決策推進</div>
        <div class="bento-desc">14 項提案以「影響度×急迫性×成本×風險」精準排程驗證。</div>
      </div>
      <div class="bento-card">
        <div class="bento-num">0 ➔ 1</div>
        <div class="bento-label">體質防禦再造</div>
        <div class="bento-desc">告別隕石開發與傳話政治，落實 JD 職務說明書與指標字典閉環。</div>
      </div>
    </div>

    <!-- Timeline of 9 Phases -->
    <h2 class="section-title" id="phases">📍 九大階段心路歷程全景復盤</h2>
    <div class="timeline">
      <div class="timeline-node">
        <div class="node-title">階段 1：宏觀藍圖的挫敗（維度不對稱的提案）</div>
        <span class="node-tag">69 頁系統分析簡報</span>
        <div class="node-body">
          依據中階轉述，產出 69 頁高規格白皮書，盤點僵化 DB、4in1 只改 UI 沒改本質、60% 代理商靠爬蟲抓數據、人工風控等痛點，並提出 14 項決策矩陣與 AI PM 系統。然而，中階傳話失真，老闆只想看立竿見影的賺錢功能，雙方頻率完全錯位。
        </div>
      </div>

      <div class="timeline-node">
        <div class="node-title">階段 2：降維聚焦與第三次失焦（傳話筒政治下的辭呈）</div>
        <span class="node-tag">105 頁商業算盤簡報</span>
        <div class="node-body">
          將架構語言降維成老闆最懂的硬數據：35 人團隊月薪 2,625,000 NTD ｜ 只要提升 0.1% DAU（+150人），即可創造 2,475,000 NTD 月營收，完全打平工程人事成本！但傳話人回饋老闆又改口，前後三次對不上，深知硬磨合只會淪為討好，毅然遞出辭呈。創辦人與人資長強力挽留。
        </div>
      </div>

      <div class="timeline-node highlight">
        <div class="node-title">階段 3：直球對決與信任對賭（掀開「房間裡的大象」）</div>
        <span class="node-tag">22 頁直球攤牌文件</span>
        <div class="node-body">
          面對創辦人與人資長一張一張投影攤牌：直指「大家都在講老闆想聽的話」的虛偽文化，揭露三條產線潛規則（需求揣測、遊戲介接照單全收、無效益檢視），立下軍令狀：<strong>【信任（自主）】＋【授權（調配）】＋【授責（0.1% DAU）】，期限 2027.1.22，未達標離開</strong>。獲全力支持，成立獨立試驗小組。
        </div>
      </div>

      <div class="timeline-node">
        <div class="node-title">階段 4：沙盒孵化（專案試驗組的快步破局）</div>
        <span class="node-tag">72 頁試驗組 Kick-off</span>
        <div class="node-body">
          彼得杜拉克名言破題，樂高動手拼「成就感」，導入「我的使用說明書」對齊團隊性格（風格、地雷、盲點、肯定方式），建立情境領導四象限。雙軌推進：維護線穩住基本盤，試驗線每 3 週一個 MVP（埋點、Web Push 推播、防屏蔽 APK、指標戰情室），小勝利累積信任。
        </div>
      </div>

      <div class="timeline-node">
        <div class="node-title">階段 5：急躁的反撲與大哉問（再度提出辭職，承諾引導完再走）</div>
        <span class="node-tag">高管擔當與善後承諾</span>
        <div class="node-body">
          試驗 1 個月正處扎根期，老闆急躁病發作想收回主導權，向各組拋出大哉問：「自己討論各自價值，證明給我看！」架構師清醒抽離再度提辭，但給出高管承諾：<strong>不留爛攤子！走之前協助各組引導完價值討論與 KPI 作業，幫團隊站穩再走。</strong>
        </div>
      </div>

      <div class="timeline-node highlight">
        <div class="node-title">階段 6：分組引導會議（差異化破局：企劃營運、前端、後端+DBA）</div>
        <span class="node-tag">三組差異化實戰工作坊</span>
        <div class="node-body">
          企劃營運組導入「三好一支援」與 5 大指標字典；前端組用「抽卡牌」破冰、規劃 6 大路線與九宮格破除組長單點壟斷；後端組以「如果一年後更差是因為什麼」逆向提問，用 ORID 焦點法化解 18 年老臣的地位、利益與關係防衛，確立 9 大技術路線。
        </div>
      </div>

      <div class="timeline-node">
        <div class="node-title">階段 7：自證其價與高層公告</div>
        <span class="node-tag">組織調整正式公告</span>
        <div class="node-body">
          在有框架的引導下，各組拿出前所未有的高質量產出（流程圖、指標字典、個人 Q4 任務、JD）。老闆親眼看見結構化價值，怒氣平息，正式發布全體組織調整與年度目標公告，確立變革合法性。
        </div>
      </div>

      <div class="timeline-node">
        <div class="node-title">階段 8：落地深耕與制度閉環</div>
        <span class="node-tag">逐一面談與工作重配</span>
        <div class="node-body">
          拿著九宮格狀態與 Q4 KPI 進行逐一面談，重新定位角色、重配工作（消除過載與閒置）、建立例會節奏、補充人力缺口。把最基本的管理制度從 0 加到 1，印證「隨便加都有效」。
        </div>
      </div>

      <div class="timeline-node highlight">
        <div class="node-title">階段 9：戰略隔離（Decoupling）與冷靜收尾</div>
        <span class="node-tag">組織絕緣層策略</span>
        <div class="node-body">
          「目前依然跟老闆不對頻，透過創辦人與 HR 轉達，還不想跟他溝通(laugh Moon)」。極致成熟的架構解耦——讓具備情感紐帶的高層去當避震器，自己專注把骨架紮牢，系統自主運轉，功成不必在我。
        </div>
      </div>
    </div>

    <!-- Teams Breakdown -->
    <h2 class="section-title" id="teams">👥 三大團隊差異化痛點與突圍對照</h2>
    <div class="table-scroll-wrap">
      <table>
        <thead>
          <tr>
            <th style="width: 14%;">團隊組別</th>
            <th style="width: 28%;">真實痛點與心理防線</th>
            <th style="width: 28%;">專屬引導工具與流程</th>
            <th style="width: 30%;">核心產出與指標字典</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>企劃營運組</strong><br><span style="color:var(--rust); font-weight:700;">10 人規模</span></td>
            <td>長期接老闆隕石需求，無KPI；成熟產品無事做，新創產品天天救火；老闆眼中「一個很亂一個能力不到位」；內部孤島。</td>
            <td>• 「三好一支援」工作坊<br>• 需求全盤點<br>• 週三分段例會機制 (需求單週/競品雙週/遊戲三週/數據月會)</td>
            <td>• 5大構面指標字典 (企劃/營運/行銷/介接/PM)<br>• Kai 營運企劃職務說明書 (JD)<br>• 沉睡玩家召回機制 Q4 任務</td>
          </tr>
          <tr>
            <td><strong>前端工程組</strong><br><span style="color:var(--warm-orange); font-weight:700;">9 人規模</span></td>
            <td>組長待6年無主管素養、常擋需求、擅長向上管理；組員有樣學樣；小團體林立、禁止交流、工作負載極度不均。</td>
            <td>• 抽卡牌破冰＋優勢卡對齊<br>• 6大職涯路線 (Leadership/效能/產品/架構/Delivery/技術影響力)<br>• 前端人才九宮格定位</td>
            <td>• Jack, Ian, Liv, Zoe 潛力座標確立<br>• 突破組長單點壟斷，授權潛力星挑大樑<br>• 獨立主責 1 項中型 Feature 上線 KPI</td>
          </tr>
          <tr>
            <td><strong>後端與DBA組</strong><br><span style="color:var(--amber); font-weight:700;">14 人規模</span></td>
            <td>1/3為16~18年開國元老 (如John)；無明確技術長；深層防禦心極強：地位防衛、利益防衛、關係防衛；各自為政。</td>
            <td>• 『一年後團隊更差是因為什麼』逆向提問<br>• ORID 焦點討論法化解心防<br>• 9大技術發展路線 (A語言深度至I工程管理)</td>
            <td>• 達成『承認能力、同意問題、建立公平規則』<br>• 資深後端 John 標準職務說明書 (JD)<br>• 流程優化與重構提案落地</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Core Toolset -->
    <h2 class="section-title" id="tools">🛠️ 組織突圍的核心武器庫</h2>
    <div class="bento-grid">
      <div class="bento-card">
        <div class="bento-label" style="font-size:1.05rem;">① 三好一支援契約</div>
        <div class="bento-desc">每人盤點「3 個強項 ＋ 2 個能支援別人 ＋ 1 個需要團隊支援」，打破防衛與猜忌，織成互相補位的協作網。</div>
      </div>
      <div class="bento-card">
        <div class="bento-label" style="font-size:1.05rem;">② 五大構面指標字典</div>
        <div class="bento-desc">徹底根除「憑感覺工作」。涵蓋企劃（重工率/前置時間）、營運（召回率/準時率）、介接（測試成功率/商業價值）等數十項具體指標。</div>
      </div>
      <div class="bento-card">
        <div class="bento-label" style="font-size:1.05rem;">③ 技術雙軌職涯路線</div>
        <div class="bento-desc">破除「當主管才能升遷」魔咒。前端開闢 6 大跑道、後端開闢 9 大路線，讓老臣重拾專業尊嚴，年輕人看見成長階梯。</div>
      </div>
      <div class="bento-card">
        <div class="bento-label" style="font-size:1.05rem;">④ 心理說明書與 ORID</div>
        <div class="bento-desc">用使用說明書對齊性格地雷；逆向提問「一年後更差是因為什麼」，倒逼老員工自發說出對整合的需求。</div>
      </div>
    </div>

    <!-- Download Center -->
    <h2 class="section-title" id="downloads">📥 官方米蘭風格交付報告下載</h2>
    <div class="doc-card-grid">
      <div class="doc-card">
        <div>
          <div class="doc-icon">📄</div>
          <div class="doc-title">Word 戰略白皮書 (.docx)</div>
          <div class="doc-desc">標準米蘭暖琥珀排版，收錄完整九大階段復盤、加權評分決策表、三組病灶對照及實戰工具說明書。</div>
        </div>
        <div class="doc-actions">
          <a href="組織從零到一的降維突圍實戰報告_米蘭風格.docx" class="btn-download" download>下載 DOCX 報告</a>
        </div>
      </div>

      <div class="doc-card">
        <div>
          <div class="doc-icon">📊</div>
          <div class="doc-title">高階簡報 (.pptx)</div>
          <div class="doc-desc">16:9 寬螢幕米蘭暖色系設計，包含 0.1% DAU 損益模型、九大階段時間軸、人才九宮格與各組引導卡片。</div>
        </div>
        <div class="doc-actions">
          <a href="組織從零到一的降維突圍實戰報告_米蘭風格.pptx" class="btn-download" download>下載 PPTX 簡報</a>
        </div>
      </div>

      <div class="doc-card">
        <div>
          <div class="doc-icon">📕</div>
          <div class="doc-title">高解析向量報告 (.pdf)</div>
          <div class="doc-desc">Chrome Headless 高清向量轉印，配置專屬微型浮水印（Howard Liao Ph.D.），支援跨平台即時審閱與列印。</div>
        </div>
        <div class="doc-actions">
          <a href="組織從零到一的降維突圍實戰報告_米蘭風格.pdf" class="btn-download" download>下載 PDF 報告</a>
        </div>
      </div>
    </div>
  </div>
</main>

<nav class="mobile-bottom-dock">
  <a href="#expert" class="dock-btn">
    <span>💡</span>
    <span>達人觀點</span>
  </a>
  <a href="#phases" class="dock-btn">
    <span>📍</span>
    <span>九大階段</span>
  </a>
  <a href="#teams" class="dock-btn">
    <span>👥</span>
    <span>三大團隊</span>
  </a>
  <a href="#tools" class="dock-btn">
    <span>🛠️</span>
    <span>武器庫</span>
  </a>
  <a href="#downloads" class="dock-btn active">
    <span>📥</span>
    <span>報告下載</span>
  </a>
</nav>

<footer class="site-footer">
  <p><strong>組織從零到一的降維突圍實戰報告</strong> ｜ 戰略治理白皮書 · Milan Editorial Standard</p>
  <p style="margin-top: 4px;">報告人：Howard Liao Ph.D. ｜ 版權所有 · 轉載請註明出處</p>
</footer>
</body>
</html>
"""

readme_content = """# 組織從零到一的降維突圍實戰報告 (Journey)

> **一場在「隕石開發」與「老臣防衛」夾縫中的組織救贖心路歷程與治理復盤**  
> **報告人：Howard Liao Ph.D.**  
> **評析視角：Ben Horowitz（《跨越艱困時刻》戰時管理）× John Kotter（領導變革大師）**

---

## 📌 核心自白
> **「不是什麼光榮厲害的升級，單純就是他們是 0，隨便加都有效。」**

在非成熟治理土壤中，當老闆深陷即興「隕石式開發」焦慮、中間層退化為只會迎合的「傳話筒」、開國老臣山頭盤據且充滿防衛心理、基層工程與企劃陷入集體茫然時，任何高大上的學院派架構或敏捷儀式都是徒勞。

唯一的生還之道：
1. **硬核商業對賭**：拿出「0.1% DAU 打平 35 人人事成本」的露骨算盤爭取沙盒空間；
2. **極簡防護工具**：用「三好一支援」、「指標字典」與「職務說明書（JD）」給基層穿上防彈衣；
3. **戰略絕緣層（Decoupling & Buffer）**：既然跟老闆不對頻，透過創辦人與 HR 當避震器，自己專注於骨架搭建，成就團隊，功成不必在我。

---

## 📍 九大階段心路歷程全景

```
[階段 1] 宏觀藍圖 (69頁)  ──> 講太深、老闆看不懂、傳話失真
     ↓
[階段 2] 降維算盤 (105頁) ──> 0.1% DAU損益打平，傳話筒再度變調，提辭呈
     ↓
[階段 3] 直球對決 (22頁)  ──> 掀開「房間裡的大象」，簽署信任與DAU 0.1%對賭契約
     ↓
[階段 4] 沙盒快跑 (72頁)  ──> 成立「專案試驗組」，樂高破冰、使用說明書、雙軌MVP
     ↓
[階段 5] 老闆心急 (大哉問) ──> 老闆急躁欲收回主導權；再次提辭，承諾引導完再走
     ↓
[階段 6] 引導突圍 (三大組) ──> 企劃營運(三好一支援)、前端(九宮格)、後端(瓦解防衛/ORID)
     ↓
[階段 7] 老闆看懂 (發公告) ──> 各組拿出結構化價值，老闆怒氣消散，全體公告背書
     ↓
[階段 8] 制度閉環 (落地跑) ──> 逐一面談定位、工作重配、制度建立、人才補缺 (0到1)
     ↓
[階段 9] 戰略隔離 (避風港) ──> 與老闆保持安全距離，由創辦人/HR轉達，安靜護航
```

---

## 👥 三大團隊差異化引導對照

| 團隊組別 | 真實痛點與心理防線 | 專屬引導工具與流程 | 核心交付成果與指標 |
| :--- | :--- | :--- | :--- |
| **企劃營運組**<br>(10人) | 長期接老闆隕石需求，無KPI；成熟產品無事做，新創產品天天救火；老闆眼中「一個很亂一個能力不到位」；內部孤島。 | • 「三好一支援」工作坊<br>• 需求全盤點<br>• 週三分段例會機制 (需求單週/競品雙週/遊戲三週/數據月會) | • 5大構面指標字典 (企劃/營運/行銷/介接/PM)<br>• Kai 營運企劃職務說明書 (JD)<br>• 沉睡玩家召回機制 Q4 任務 |
| **前端工程組**<br>(9人) | 組長待6年無主管素養、常擋需求、擅長向上管理；組員有樣學樣；小團體林立、禁止交流、工作負載極度不均。 | • 抽卡牌破冰＋優勢卡對齊<br>• 6大職涯路線 (Leadership/效能/產品/架構/Delivery/技術影響力)<br>• 前端人才九宮格定位 | • Jack, Ian, Liv, Zoe 潛力座標確立<br>• 突破組長單點壟斷，授權潛力星挑大樑<br>• 獨立主責 1 項中型 Feature 上線 KPI |
| **後端與DBA組**<br>(14人) | 1/3為16~18年開國元老 (如John)；無明確技術長；深層防禦心極強：**地位防衛、利益防衛、關係防衛**；各自為政。 | • 「如果一年後團隊更差是因為什麼」逆向提問<br>• ORID 焦點討論法化解心防<br>• 9大技術發展路線 (A語言深度至I工程管理) | • 達成「承認能力、同意問題、建立公平規則」<br>• 資深後端 John 標準職務說明書 (JD)<br>• 流程優化與重構提案落地 |

---

## 📥 交付文件庫 (米蘭暖琥珀風格)
- `組織從零到一的降維突圍實戰報告_米蘭風格.docx` (Word 完整版)
- `組織從零到一的降維突圍實戰報告_米蘭風格.pptx` (16:9 簡報)
- `組織從零到一的降維突圍實戰報告_米蘭風格.pdf` (出版級向量 PDF，帶微型浮水印)
- `index.html` (響應式行動端優化展示門戶)

---
*專案維護：Howard Liao Ph.D. ｜ 授權所有 · 未經許可請勿轉載*
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(readme_content)

# Touch .nojekyll
with open(os.path.join(OUTPUT_DIR, ".nojekyll"), "w", encoding="utf-8") as f:
    f.write("")

print("Portal files created successfully!")
