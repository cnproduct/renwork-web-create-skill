# GEO：可检索、可理解、可核验的内容

GEO 的工程目标是帮助目标买家和检索系统正确理解真实企业信息；排名、推荐与引用来自外部系统，不能由本地评分保证。Google AI 搜索沿用搜索基础，不要求 llms.txt、特定 schema、固定答案字数或 WebMCP。研究中观察的提升不能当成客户站保底成功率。

## 内容精华

- 直接回答实际问题，再给范围、限制、单位、测量条件、真实型号与下一步选型。答案应能脱离上一段理解，但字数由问题复杂度决定，不机械凑 100–150 词。
- 用可见规格表、原创测试/工艺记录、真实应用案例、产品差异、图/视频及配套文字代替“领先/优质/全球认可”。独特事实先由企业资料确认，不能为引用编造统计、专家或证书。
- 对行业标准注明是适用参考、测试依据还是目标 SKU 已取得的证据；不能将 ASTM/CE/FDA 等一律当认证，更不能把行业常识写成企业资质。
- 引用应链接到实际支持该断言的原始来源，说明日期/对象/限制。官方同一实体资料保持名称/联系一致；sameAs 仅链接真实对应身份，不强制 Wikipedia/Wikidata/Crunchbase 凑数量。
- 多语言同步公共事实与单位/采购语境；没有对应译文不生成语言标签。版本更新时间反映实际维护，不每日刷 dateModified。
- 可选 llms/Markdown/JSON 投影与公开网页同源，不能暴露私人报价、客户名单、未发布规格或出现正文没有的承诺。代理操作端点/WebMCP 仅在明确场景与当前浏览器支持核实后采用，不能设 toolautosubmit 自动代客下单或询盘。

## 访问控制按目的区分

按平台最新官方说明核对 crawler 的搜索发现、用户发起抓取、训练/其他 grounding 用途与 IP 校验。OAI-SearchBot 用于搜索，GPTBot 用于训练，ChatGPT-User 用于用户请求；不是“AI bot 全允许”一个开关。Google Search 的 AI features 受 Googlebot 与搜索预览控制影响，Google-Extended 有另一用途；不要以为允许后者就是打开 Google AI 搜索。

robots 是抓取策略，不是鉴权；CDN/WAF/挑战、错误状态、JS 渲染和资源可达也要检查。不能只改 UA 伪装测试后声称真实官方 bot 已访问，也不能为放行 AI 绕过后台和询盘安全。

## 测量

TRAFFIC_MAP 中固定高价值问题集；记录平台、模型/界面、日期、语言/国家、问题、完整可保留的结果证据、品牌提及、引用目标 URL 和准确性。同条件重复采样，报告样本数；答案波动与平台变动影响结论。引用并不等于点击，品牌提及不等于引文，referral 不等于合格询盘。Bing AI Performance 可在权限与可用范围内提供引用/grounding insights，不能代替其他平台报告。

上线检查内容可读与事实一致；收录、引用、流量、询盘需后续各自证据。没有权限、数据或真实采样时写 UNKNOWN/NOT_RUN，不输出“AI 引用率 95%”或“100 分全平台推荐”。

## 依据与方法来源

- [Google AI features](https://developers.google.com/search/docs/appearance/ai-features) 与 [Google AI optimization](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)：搜索基础、有用原创内容与可达性。
- [Google 文档更新](https://developers.google.com/search/updates)：2026-06-15 llms 澄清；不把可选索引描述为 Google 排名信号。
- [OpenAI bots](https://developers.openai.com/api/docs/bots)：三类用途独立控制，核对最新身份/IP。
- [Bing AI Performance 公告](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/)：平台引用洞察范围，不代表排名或点击。
- [GEO 原始研究](https://arxiv.org/abs/2311.09735)：作为内容证据、统计/引用等策略的研究线索；实验环境与特定指标不能推广为任何生产平台保证。使用其具体数字前读原文并标实验条件。

每次项目执行刷新官方易变规则，社区 skill 与本地旧规则冲突时以当前官方文档和直接实验为准。
