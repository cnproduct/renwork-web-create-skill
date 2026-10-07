# RenWork Web Create Skill · 3.0.0

先通过真实证据建立参考站复刻基线，拆解其 SEO/GEO 与采购转化机制，再为目标企业创造自己的独立站。最终交付可运行代码、预览和证据；首页相似、换色换名或研究报告均不能替代完整结果。

## 这次融合了什么

| 来源 | 核心方法 | 实际落点 |
| --- | --- | --- |
| Jane web-clone | 真源码、技术分流、证据分级、设计 DNA、RAW REPLAY | 基线取证与复杂特效分支 |
| Nolan skills | computed styles/组件状态、可验证目标、迭代停止与状态 | DESIGN、完成契约、缺口驱动换 skill |
| PixelClone | 布局蓝图、视觉/业务真相分离、控件与素材边缘 QA | 保真基线和现有业务契约 |
| OpenDesign web-clone | 真浏览器采集、字体/图像落地、网络/交互与 strict 审计 | 完整资源和同状态对照 |
| boyang website-rebuild | 只读镜像、哈希账本、溯源移植、确定性门 | 动效/压缩源码/冷启动验收 |
| 本地审计与 GitHub marketingskills | 事实投影、crawl/index、信息架构、AI 可引用内容、schema | 流量图→原创页面→独立测量 |

来源文件、版本、许可、适用边界和组合选择见 [融合矩阵](references/skill-fusion.md)。本仓库提炼方法，没有打包复制上游脚本；上游工具按需发现，核心流程无强制第三方 skill 依赖。

## 典型调用

```text
用 renwork-web-create-skill，先完整复刻参考站 https://reference.example 的约定页面与交互，
分析目标国家/语言的 SEO/GEO 入口、内链、引用与采购路径，再用 /path/to/company 的真实资料
在 /path/to/project 创造目标品牌的新站。一种 skill 不够就按未通过的检查组合其他能力；
交付源码、预览、流量迁移图、原创变化表和分层验收，不把未知流量、收录、引用或收件写成成功。
```

只要求忠实复刻/局部优化/只读分析时保持该范围。公开发布按已有授权，不因调用本 skill 自动发布或向第三方发询盘。

## 工作流与结果

1. 确定实际目标、企业资料、路由/产品/语言/发布范围及完成标准。
2. 采集源码/部署资源、浏览器 DOM/styles、网络与状态；建立全站覆盖清单和只读证据。
3. 按能力缺口换用或组合 skills，修复并同范围复测，交付可运行复刻基线。
4. 建立查询→入口页→内容集群→内链→信任→CTA→询盘的 `TRAFFIC_MAP.md`，区分实测、观察、估算和假设。
5. 用目标事实兑现 `ORIGINALITY.md`，实施独特品牌叙事、应用组织、构图、影像和选型内容。
6. 将 SEO/GEO 写入共享模板和真实路由，验证 build、浏览器、公开状态，再独立验证索引、引用与询盘。

项目结果包括代码/预览、路由与资产台账、WORKLOG、TRAFFIC_MAP、ORIGINALITY 和 design-qa。小项目可以合并报告，但每个结论仍有范围、状态和可定位证据。

复刻与原创分别验收；原创不以像素等同参考为门槛。公开竞争站数据不证明真实流量，内部得分不证明搜索排名。没有后台权限可以完成公开研究与代码，流量归因保持 UNKNOWN。

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

- [复刻/原创验收](references/pixel-clone-contract.md)
- [流量来源和原创迁移](references/traffic-and-originality.md)
- [SEO 与 schema](references/b2b-seo-schema-spec.md)
- [GEO 可引用内容](references/geo-citability-guide.md)
- [设计 token 示例](references/b2b-design-tokens.md)
- [行业采购组件](references/procurement-components.md)
- [默认站点防护](references/site-protection.md) 与 [边缘 Worker 模板](templates/edge-worker.mjs)

`assets/industries.json` 是行业问题/字段提示，标准名称不证明目标企业认证。`templates/b2b-factory-starter/` 保留历史 Xinghui 演示，内容与素材未由本 skill 证明，已标演示、noindex、禁爬、无生产询盘；不能直接作为任何目标企业的事实源或公开发布包。不承诺固定 SKU 数、七语站、FAQ 富结果、精确装柜配载或 AI 引用率。

[SKILL.md](SKILL.md) 是运行入口。[MIT License](LICENSE) 适用于本仓库自有内容，不授予第三方品牌、网站素材或参考代码的权利。
