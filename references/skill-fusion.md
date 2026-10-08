# 融合来源、环境发现与能力补齐

2026-10-07 核对来源；阅读范围逐项注明。以下是方法提炼与路由，不是 vendored 脚本；本仓库没有复制上游实现。使用上游工具时读取当前版本说明、许可及实际 CLI，不把作者机器路径或宿主专用约束写成通用规则。

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

## v4：先选赛道与采购任务，再选标杆

以下专业方法用于 [前置发现](benchmark-discovery.md)、[原创迁移](traffic-and-originality.md) 和 [通用 Skill 优化](skill-optimization.md)。来源观点不是目标企业事实；示例域名只是待验证种子，不作为固定榜单。

| 来源/核对版本 | 阅读范围与提炼 | 适用边界 |
| --- | --- | --- |
| [cnproduct/b2b-limestone-geo-site-builder](https://github.com/cnproduct/b2b-limestone-geo-site-builder/tree/408fa215057a82a2bd7ec8af4be8449642e7c7f8) · MIT | `references/benchmark-discovery-methodology.md` 全文；`SKILL.md` 发现、命名、工程、GEO及RFQ相关段；README。先发现再复刻，技术/视觉/长尾分工，文化命名、图实匹配与跨行业迁移 | 用户提供的三会话整理是历史材料，本次未逐条复核原始私有会话。保留工作方法，不把排名、溢价、产能、认证、固定爬虫/端点数及“全行业100%成功”升级为事实；改名/改图不自动证明权利 |
| [every-app/open-seo](https://github.com/every-app/open-seo/tree/deb44913c2e345ec29ce6fb066a94ca428ebc681) · MIT | `plugins/openseo/skills/competitive-landscape/SKILL.md`、`competitor-analysis/SKILL.md` 全文。查询集发现市场、区分搜索与业务竞争者、相关入口/主题/外链、由市场到单站深读 | 本项目扩为十站比较，再精选深读。不继承 OpenSEO 项目写回、收费调用、报告插件硬依赖；工具名须在实际环境发现 |
| [seranking/seo-skills](https://github.com/seranking/seo-skills/tree/fd6d1408f2e6a06454d81c07c29e0f04342eb9ba) · MIT | `skills/seo-competitor-gap-analysis/SKILL.md` 全文。竞争词集交叉、意图/主题分组、原始数据与页面行动关联 | 不默认美国、不强制 MCP；出现于多家竞品不等于适合目标企业；内容薄弱不能只靠字数/URL判断；不沿用固定积分/机会数或自动创建跟踪项目 |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/f719a8079c694e3267d47b6b60a62aa926055f2c) · MIT | `skills/competitor-profiling/SKILL.md` 全文；`product-marketing`、`content-strategy`、`free-tools` 的定位/角色、内容决策与工具原则相关段。可比较档案、观察/推断/行动分层、采购委员会与有用工具 | 不强制 Firecrawl/DataForSEO；本任务默认深研，覆盖全部候选的证据表后再深读精选站。公开客户数不能由流量“验证”，需独立事实；未知流量不自行估算 |
| [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills/tree/1b5a524ebb95e9497fa3f25002d8b8ec528d4444) | `skills/jobs-to-be-done/SKILL.md` 核心任务、痛点/收益与研究限制段 | 提炼功能/情绪/社会任务；没有真实访谈不能称需求已验证。方法提炼，不复制实现，代码复用时另核许可 |
| [liangdabiao/exa-research-mcp-skill](https://github.com/liangdabiao/exa-research-mcp-skill/tree/6a345be5df349e00c7c468e5d5d09ac7bf8d09b1) | `skills/foreign-trade-research/SKILL.md` 市场/本地语言/渠道与证据相关段 | 提炼产品×国家与贸易研究；不继承固定 TOP20 配额、报告字数和 Exa 依赖 |
| [anthropics/skills](https://github.com/anthropics/skills/tree/683bc88e56f3e09ba94f7055977f3d3aa499f202) | `skills/frontend-design/SKILL.md` 行业、受众、视觉方向与审视相关段；`skill-creator/SKILL.md` 创建/评测段另于 2026-10-07 读取 main | 提炼行业驱动设计、实际案例迭代；不批量复制提示词、强制框架或工具。逐 skill 许可分别核对 |
| [samber/cc-skills](https://github.com/samber/cc-skills/tree/123cb155f5ab5751fc13c8027fbfa5eb0d3773c6) | `skills/frontend-design-deslop/SKILL.md` 本机版本；`skills/deep-research/SKILL.md` 证据/综合/审视段 | 策略→设计系统→实现→审视；不继承固定字体禁用、全量提示词或强制多 agent 数量 |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/b482f7a970abb98c4108d4a9f761e458c64cefc8) · MIT | `skills/taste-skill/SKILL.md` brief、variation/motion/density与审视相关段，非全量加载 | v2 标为 experimental；提炼情境化取舍，不强制动效库、图标依赖或所有页面高动态 |

本机 `renwork-site-audit-optimizer` 的品类/季节采购反推、`skill-creator` 的渐进披露与行为检查、`renwork-smart-skills-creator` 的 observed/derived 与证据回写已阅读并提炼。执行时发现真实路径，不写死本机安装位置，不强制安装这些 skills。流程保持自包含。

## Hugging Face：专业资源分类使用

- [huggingface/skills](https://github.com/huggingface/skills/tree/ca0325bb20b2d0a1b2efa893670c4c72f79e707b)：已读 `skills/huggingface-datasets/SKILL.md` 的 Viewer/只读检索与分页，及 `huggingface-community-evals/SKILL.md` 的模型评测段。数据集检查和模型评测是可选能力，不证明网站采购洞察或 Skill 行为改善。逐资源另核许可；不默认上传私密轨迹、租 GPU 或训练模型。
- [SALT-NLP/Design2Code](https://huggingface.co/datasets/SALT-NLP/Design2Code)：已读数据卡，HTML/截图布局评测；原图被占位图替换，适用于还原检查，不用作品牌影像质量或买家需求证据。
- [knguyennguyen/pattern2code](https://huggingface.co/datasets/knguyennguyen/pattern2code)：已读数据卡与任务说明，借鉴“保留重复布局中的真实例外”检查；研究数据中原网站的权利不能由数据集许可替代。
- [HuggingFaceM4/WebSight](https://huggingface.co/datasets/HuggingFaceM4/WebSight)：已读合成数据说明，未纳入默认创造参考；合成网页不证明真实行业审美或采购需求。

以上仅核对资源与提炼方法，本仓库未运行这些模型/数据集基准。使用时记录实际 revision/配置、样本、许可、条件与结果，不能把外部模型分数写成本 Skill 分数。

## 从这次优化得到的通用方法

`用户目标/已证实问题 → 选择专业参考 → 读取实际规则与边界 → 找出缺口 → 按职责组合 → 小范围实施 → 同条件验证 → 只沉淀可复用结论`。

v3 的工具回归与可审阅代码是已有本地实现证据；v4 的前置战略、专业来源融合与通用优化在本次形成指令能力，其真实网站增长效果仍须实际项目验证。历史建议、计划和来源宣传不记为成功结果；版本升级与 GitHub 同步不等于客户网站上线。

## v4.2 合并记录

合并远端 `0045c77` 的买家/贸易与创意深研、历史发现案例、两份项目模板、RFQ/Turnstile 说明及资产检查。入口按需链接这些能力，前置选择统一以十站候选与分维度证据为准。模板中的固定企业数字与预设许可改为待填事实；历史品牌保留为种子；RFQ说明匹配本仓库实际边缘模板和外接服务边界。上游不存在的工具、无依据许可/认证/成功率与私人会话标识不作为执行契约。
