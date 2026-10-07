# RenWork Web Create Skill 🌐

[![Version](https://img.shields.io/badge/version-2.0.0-516b4b.svg)](https://github.com/cnproduct/renwork-web-create-skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![B2B-SEO](https://img.shields.io/badge/SEO-5--in--1%20Schema-green.svg)](#)
[![GEO-Citability](https://img.shields.io/badge/GEO-Princeton%20KDD%202024-blue.svg)](#)

> **High-Fidelity 1:1 Website Reverse Engineering & B2B SEO/GEO Citability Engine**  
> 企业级出海独立站 1:1 深度复刻与生成式 AI 搜索引擎 (GEO) 流量引力场构建技能。

---

## 📖 Introduction (项目简介)

`renwork-web-create-skill` 沉淀自中国制造业头部出海独立站的实战复刻工程（如 `xhplasticlife.com` 等）。它将顶级海外竞品站的视觉美学、产品目录架构与全网获客灵魂一比一完整还原，不仅复刻其“形”（1:1 源码与像素级视觉系统），更复刻其“神”——**Google 商业意图词 SEO 与 AI 搜索引擎（ChatGPT Search / Perplexity / Claude / Gemini）的 GEO 流量引力场**。

---

## 🏛️ Heritage & Core Principles (理论渊源与核心军规)

本技能集大成融合了以下顶尖开源与本地工程体系：
- **`claude-skill-web-clone` & `open-design/web-clone`**: 真源码证据第一原则，拒绝 AI 臆测代码，覆盖静态/动态/动效三大技术决策分支。
- **`website-to-design-md`**: 深度抽取真实网站的调色板、Typography、间距网格与 Surface 分层，沉淀出版级 `DESIGN.md`。
- **`PixelClone-Skill`**: 像素级复刻与绝对业务契约，确保真实输入、真筛选与无障碍交互 100% 落地。
- **`website-rebuild-skill`**: 证据驱动管线与量化验证闸门。
- **`B2B Portal Builder with Sitemaps`**: 静态 CMS 编译器、63-SKU 目录自动化编译、高转化 RFQ 漏斗。
- **`geo-optimizer-skill`**: 基于 Princeton KDD 2024 研究的 GEO 生成式引擎优化，全量输出 `llms.txt` / `llms-full.txt` 与开放型 `robots.txt`。
- **`Layout & Typography Auditor`**: 全自动排版对齐、防溢出与移动端合规审计。

---

## 🚀 Quick Start (快速开始)

### 1. 探测目标网站与提取证据链
```bash
python3 scripts/site_forensics.py https://www.xhplasticlife.com/ ./evidence
```

### 2. 自动抽取设计系统生成 DESIGN.md
```bash
python3 scripts/extract_design_tokens.py ./evidence/css/bundle_0.css ./design.md
```

### 3. 生成全套 SEO 结构化数据与 GEO 知识端点
```bash
python3 scripts/geo_seo_engine.py ./my-clone-site/
```

### 4. 运行排版与质量合规审计
```bash
python3 scripts/layout_typography_auditor.py ./my-clone-site/
```

### 5. 启动本地热重载开发服务器
```bash
python3 scripts/dev_server.py 8080 ./my-clone-site/
```

---

## 📦 Directory Structure (目录结构)

```text
renwork-web-create-skill/
├── SKILL.md                          # 核心技能指令与端到端决策树
├── README.md                         # 技能使用手册与架构解析
├── scripts/
│   ├── site_forensics.py             # 目标站点深度探针与 DOM/CSS/SKU 提取
│   ├── extract_design_tokens.py      # CSS 令牌解析与 DESIGN.md 自动生成
│   ├── geo_seo_engine.py             # 5合1 Schema、Sitemap、robots.txt、llms.txt 编译器
│   ├── layout_typography_auditor.py  # 排版对齐、容器溢出与图片无障碍全域审计
│   └── dev_server.py                 # 轻量本地静态预览与 RFQ API 收集服务
├── references/
│   ├── b2b-design-tokens.md          # 国际高转化 B2B 视觉语言规范
│   ├── geo-citability-guide.md       # Princeton KDD 2024 GEO 白皮书
│   ├── b2b-seo-schema-spec.md        # 5合1 结构化数据 Schema 黄金标准
│   └── pixel-clone-contract.md       # 像素级复刻与绝对业务契约指南
└── templates/
    └── b2b-factory-starter/          # 开箱即用的工业出海官网组件套件
```

---

## 📄 License
MIT © 2026 [cnproduct](https://github.com/cnproduct) · RenWork AI Innovation Team
