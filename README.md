# RenWork Web Create Skill · 4.0.0

**先选赛道与买家，再从行业 Top 10 中选对标。** 比较 SEO、GEO、可比流量、设计与技术采购能力，深读各自领先者，复现关键页和有效机制，再创造目标企业的独特网站。最终交付可运行代码、预览和证据。另有内置通用模式：从本机、GitHub、Hugging Face 发现专业方法，优化指定的任意 Skill。

## 两种模式

- **建站**：行业/贸易机会 → 采购需求 → Top 10 候选 → 分维度择优 → 关键页与机制蒸馏 → 原创设计 → SEO/GEO与采购验收。
- **优化 Skill**：真实任务/失败 → 能力缺口 → 专业资源发现 → 机制蒸馏 → 最小改动 → 前后验证 → 经验回写。

建站前必须先形成选择依据。Top 10 是相关候选池；“流量最高”须有同口径数据，“GEO 最好”须有问题集与平台采样。未知数据保留未知，不把内部评分当排名。

## 这次融合了什么

| 来源 | 核心方法 | 实际落点 |
| --- | --- | --- |
| limestone site builder | 先发现再复刻，技术/视觉/长尾分工，文化命名和图实匹配 | 阶段零选型与原创机制；历史品牌是待验证种子 |
| OpenSEO / SE Ranking / competitor-profiling | 查询集发现竞争格局、可比档案、关键词与入口缺口 | Top 10 候选、分榜择优、相关高流量入口深读 |
| JTBD / product-marketing / 外贸研究 | 买家任务、采购委员会、产品×国家与贸易情景 | 赛道决定、买家决策图与内容行动 |
| frontend-design / taste / deslop | 行业驱动的视觉方向、节奏与精选动效 | 三个原创方向择优、统一设计与移动体验 |
| Hugging Face / 本机 Skill 创建与沉淀 | 资源分类、评测思路、证据回写 | 按需发现与通用优化；不默认模型训练 |
| Jane web-clone | 真源码、技术分流、证据分级、设计 DNA、RAW REPLAY | 基线取证与复杂特效分支 |
| Nolan skills | computed styles/组件状态、可验证目标、迭代停止与状态 | DESIGN、完成契约、缺口驱动换 skill |
| PixelClone | 布局蓝图、视觉/业务真相分离、控件与素材边缘 QA | 保真基线和现有业务契约 |
| OpenDesign web-clone | 真浏览器采集、字体/图像落地、网络/交互与 strict 审计 | 完整资源和同状态对照 |
| boyang website-rebuild | 只读镜像、哈希账本、溯源移植、确定性门 | 动效/压缩源码/冷启动验收 |
| 本地审计与 GitHub marketingskills | 事实投影、crawl/index、信息架构、AI 可引用内容、schema | 流量图→原创页面→独立测量 |

来源文件、版本、许可、适用边界和组合选择见 [融合矩阵](references/skill-fusion.md)。本仓库提炼方法，没有打包复制上游脚本；上游工具按需发现，核心流程无强制第三方 skill 依赖。

## 典型调用

```text
用 renwork-web-create-skill，基于 /path/to/company 的真实产品和履约能力，
先研究细分赛道、目标市场和海外买家采购需求，筛选行业 Top 10 网站候选；
分别选出 SEO、GEO、可比流量、设计与技术采购方面值得深读的标杆，说明依据。
把高价值入口、设计与采购机制融合，在 /path/to/project 创造目标品牌的原创站。
交付选型与标杆表、代码、预览和验收；不能凭知名度或估算声称全球第一。
```

```text
用 renwork-web-create-skill 优化 /path/to/target-skill（也可给仓库地址）。
先检查真实任务和失败，再从本机、GitHub、Hugging Face 寻找专业能力，
蒸馏适用方法并实施最小改动，验证新旧行为，交付改动、来源与剩余缺口。
```

只要求忠实复刻/局部优化/只读分析时保持该范围。公开发布按已有授权，不因调用本 skill 自动发布或向第三方发询盘。

## 工作流与结果

1. 复用企业事实，比较细分赛道、市场与趋势，按行业识别采购角色和痛点。
2. 全球发现并筛选十个相关独立域名，逐项记录来源、口径、设计和采购证据。
3. 分维度选择通常 3–5 个互补标杆，形成 `BUYER_STRATEGY.md`，再进入复刻。
4. 对约定关键页/机制取证与复现；明确要求完整复刻时覆盖完整范围。
5. 建立 `TRAFFIC_MAP.md`，将查询、入口、内容、内链、证明与采购动作迁移到目标页面。
6. 根据真实产品、行业语言与买家任务提出三个视觉方向，择优形成统一原创站和 `ORIGINALITY.md`。
7. 验证设计、图实匹配、交互、采购路径与工程状态，独立记录索引、引用和询盘结果。

网站交付包括代码/预览、路由与资产台账、BUYER_STRATEGY、TRAFFIC_MAP、ORIGINALITY、WORKLOG 和 design-qa。小项目可以合并报告，结论仍有可定位证据。选型记录是工作产物，不增加重复审批。无法量化流量/GEO时可暂定实施，但不得宣称已选出其冠军。

通用优化交付目标 Skill 的可审阅改动与 `SKILL_OPTIMIZATION.md`；按目标领域评测，不对所有 Skill 套用网站标准。[完整流程](references/skill-optimization.md)

## 自带工具

Python 3.10+，仅标准库；无需为这些助手安装浏览器或第三方包。完整复刻仍需实际可用的浏览器能力，缺失时明确未测范围。

在本仓库/已安装 skill 根目录运行：

```bash
# 单页 HTTP 原始证据、类型/sha256 台账；不执行 JS，不爬全站
python3 scripts/site_forensics.py https://example.com/ /path/to/new-empty-evidence
# CSS 候选；实际角色/布局由浏览器测量核实
python3 scripts/extract_design_tokens.py /path/to/evidence/css/bundle_0.css /path/to/DESIGN.md
# 真实已存在 HTML + 显式配置；默认 draft，拒绝覆盖现有输出
python3 scripts/geo_seo_engine.py /path/to/public-build --config /path/to/site-config.json
# 递归 HTML 静态检查，失败返回非零；不判视觉或生产 readiness
python3 scripts/layout_typography_auditor.py /path/to/public-build
# 仅本地预览，RFQ 返回未连接，不收集/打印个人询盘内容
python3 scripts/dev_server.py 8080 /path/to/public-build
# 无网络/无第三方依赖回归检查（本机临时 HTTP fixture）
python3 scripts/test_tools.py
```

SEO 配置与真实边界见 [SEO/schema 契约](references/b2b-seo-schema-spec.md)：输出 robots、sitemap、待应用的 seo-pages.json；可选 llms 索引仅投影公开页面，不虚构企业事实或语言 URL。应用逐页数据到源模板并重建后仍要做浏览器与线上验证；工具准备数据不是修改网站完成。

## 参考资料与模板

- [行业选型、采购洞察与 Top 10 标杆发现](references/benchmark-discovery.md)
- [通用 Skill 优化与蒸馏](references/skill-optimization.md)
- [行为评测场景](references/evaluation-scenarios.md)
- [复刻/原创验收](references/pixel-clone-contract.md)
- [流量来源和原创迁移](references/traffic-and-originality.md)
- [SEO 与 schema](references/b2b-seo-schema-spec.md)
- [GEO 可引用内容](references/geo-citability-guide.md)
- [设计 token 示例](references/b2b-design-tokens.md)
- [行业采购组件](references/procurement-components.md)
- [默认站点防护](references/site-protection.md) 与 [边缘 Worker 模板](templates/edge-worker.mjs)

`assets/industries.json` 是行业问题/字段提示，标准名称不证明目标企业认证。`templates/b2b-factory-starter/` 保留历史 Xinghui 演示，内容与素材未由本 skill 证明，已标演示、noindex、禁爬、无生产询盘；不能直接作为任何目标企业的事实源或公开发布包。不承诺固定 SKU 数、七语站、FAQ 富结果、精确装柜配载或 AI 引用率。

[SKILL.md](SKILL.md) 是运行入口。[MIT License](LICENSE) 适用于本仓库自有内容，不授予第三方品牌、网站素材或参考代码的权利。
