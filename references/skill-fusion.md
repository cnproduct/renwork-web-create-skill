# 融合来源、环境发现与能力补齐

2026-10-07 逐仓库阅读。以下是方法提炼与路由，不是 vendored 脚本；本仓库没有复制上游实现。使用上游工具时读取当前版本说明、许可及实际 CLI，不把作者机器路径或宿主专用约束写成通用规则。

## 五个指定来源

| 来源与核对版本 | 已读核心文件 | 融合到本 skill 的精华 | 使用场景与适用边界 |
| --- | --- | --- | --- |
| [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone/tree/0269e0e08a3783184ec641d341e7d57065d4a5f8) · MIT | `SKILL.md` | 真源码优先；静态/内容/SPA/复杂特效分流；SOURCE/PARTIAL/GUESS；最小 RAW REPLAY；设计 DNA；路由、交互、资源与前后报告 | 第一层侦察/实现。公开 bundle 是客户端部署源，不能证明取得后端；作者的绝对路径不适用其他电脑 |
| [NolanSoloBuilder/skills](https://github.com/NolanSoloBuilder/skills/tree/0c109f8d90d3be80a35b86c78c64333790c2475c) | `skills/website-to-design-md/SKILL.md`、`defining-goals/SKILL.md`、`designing-loops/SKILL.md` | 渲染 DOM/computed styles/主题/组件状态生成设计规则；终态与证据契约；防 Goodhart；有状态、停止条件的迭代 | 不是“整仓都是复刻工具”。借用目标与 loop 判断，不为单次建站强加调度器/自动化/多 Agent。仓库根无 LICENSE；逐 skill 许可单独核实，不直接复制分发 |
| [PixelClone-Skill](https://github.com/bjvgukv25842-cmyk/PixelClone-Skill/tree/91bca5dd9df9156eb6a4ee33ac7861695b93db70) | `skills/pixel-perfect-reference-ui-zh/SKILL.md` | 总图布局蓝图（section/列宽/包围盒/换行）；视觉与业务真相分开；保留真实控件、API/ref/状态；裁切边缘、z-index、焦点与多断点 QA | 适用于参考图及现有前端展示层。无源码时截图不能证明隐藏交互；“不自创视觉/不外部素材”限还原阶段，不能阻止原创站使用目标素材。根无 LICENSE，不直接复制代码/全文 |
| [nexu-io/open-design web-clone](https://github.com/nexu-io/open-design/tree/53231d40b778d88eba23f35547bf99485d3ae9fc/skills/web-clone) · 根 Apache-2.0 | `skills/web-clone/SKILL.md` | 复用现有浏览器/CDP；慢滚真实请求采集、字体/图片落地、URL manifest；computed 色与滚动状态；strict 审计；嵌套预览资源适配 | 与 Jane 同源，不伪称独立证据投票。在 OpenDesign 才使用 staged 路径、daemon 和 preview rewrite；其他环境先验证自己的 served URL，不能机械改所有路径 |
| [boyang-hu/website-rebuild-skill](https://github.com/boyang-hu/website-rebuild-skill/tree/830647fbe4e31cda85319df69b48514bd224ad79) · MIT | `skills/website-rebuild/SKILL.md` | 只读 mirror → 可追溯移植 → 可读 src；逐资源 sha/身份/引用闭包；bundle/source-map 坐标；冷启动、同状态像素/语义/数值门；差异台账 | 深度创意站/动效逆向。先 fingerprint，按静态客户端/公开输出/服务端能力分流；L1 镜像不等于 L2 可维护工程。不要对普通 B2B 页面套几十个逆向门，也不默认继承原站漏洞或复制业务后台 |

冲突按当前用户目标、目标事实、项目契约和所在阶段解决。复刻阶段保持参考一致性；原创阶段依据迁移表设计。没有直接使用上游源码，因此不把“上游全部源码已融合”写成结果；未来 vendoring 须保留对应许可与署名。

## 本机 SEO/GEO 搜索

先从运行时 skills catalog 与项目 `.agents/skills`、用户 `~/.codex/skills`、`~/.agents/skills` 定位 SKILL.md。用 `rg --files` 后按 seo/geo/audit/architecture/schema/content/trend 搜索文件路径，再读匹配项，不能只凭名称调用或扫描私人企业资料。

本次已核对：

- 本地 `renwork-site-audit-optimizer`：路由分层、基线→直接修复→同范围复测；GSC/Bing/表单与发布状态分开；内部得分不是平台排名分。
- 本地 `renwork-seo-geo-optimizer`：复用企业事实→页面/schema/机器投影的映射、选型/单位/技术证据组织；**不继承** 1.8%–2.2% 关键词密度、100–150 词答案、5000 词 llms、27 爬虫全部放行、虚构权威实体/认证/物流条款、“100 分即引用成功”等说法。知识库事实适用，但数字和平台效果必须独立证明。
- 本地 `renwork-web-design-master`：按目标框架复用 fluid layout、中文字体与断行、可访问性与实际浏览器检查；不强制统一字体/配色。

这些是可选能力而非硬依赖，本仓库的 references 足以执行核心流程。跨机器先发现真实路径，不复制本机用户目录。

## GitHub SEO/GEO 补充

已读 [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/5e721d73ac85be8ba917d6a9ca9cb5bc98f02b80)（MIT）的 `skills/seo-audit/SKILL.md`、`ai-seo/SKILL.md`、`site-architecture/SKILL.md` 和 `schema/SKILL.md`：

- `seo-audit`：先 crawl/index 再技术、页面、内容、权威；原始 HTML 没有 schema 时需检查渲染 DOM，不能判 JS 注入 schema 不存在。
- `site-architecture`：页面层次、导航、URL/内链与迁移关系；按业务组织，不把“3 click”或每千字链接数当排名公式。
- `ai-seo`：检索可达→答案可理解→证据可信；query fan-out、引用/提及/访问区别、按内容类型设计与重复采样；不用未经核验的比例或固定格式成功率。
- `schema`：匹配可见正文、按实体/页面选择类型、稳定 @id 和图谱一致；上游旧 FAQ 富结果建议须由当前 Google 文档覆盖。

仓库当前名称为 `schema`，不能照旧安装命令猜 `schema-markup`。搜索补充 skills 时核对作者源仓库、目录、SHA、LICENSE、依赖与真实脚本；优先只读/按需，不自动全机安装。若确需安装，遵循用户范围及技能安装器规则。

## 最小换 skill 记录

| gap_id | 失败检查与证据 | 已用 skill/版本/路径 | 替换/组合能力及理由 | 新产物 | 复测结果 | 剩余阻塞 |
| --- | --- | --- | --- | --- | --- | --- |
| FONT-01 | 移动标题换行错，字体 URL 返回 HTML | HTTP 初探 | OpenDesign browser harvest + PixelClone 文本蓝图 | 真字体 manifest/两侧截图 | 按原视口重测 | 如许可不明，原创用已授权目标字体 |

已通过的项保留，追加同一范围的复测，不靠缩减页面/功能/样本让门变绿。剩余 gap 为零且检查都有证据才称范围内完整；缺浏览器或素材时记录 BLOCKED 并完成其他模块。
