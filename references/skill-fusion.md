# 技能融合与来源追踪台账 (Skill Fusion & Upstream Provenance)

> 记录本 Skill (RenWork Web Create Skill v4) 吸收提炼的所有专业开源库、论文与工程技能。  
> 采用“提炼方法、按缺口调用”原则，来源保留路径、许可、适用场景与验证状态。

---

## 1. 深度融合资源矩阵 (Resource Provenance Ledger)

| 资源名称 | 来源仓库 / 规范地址 | 许可协议 | 提炼的核心精华与机制 | 在本 Skill 中的调用场景 |
| :--- | :--- | :--- | :--- | :--- |
| **Jobs to Be Done (JTBD)** | `deanpeters/Product-Manager-Skills/skills/jobs-to-be-done` | MIT | 三维任务分析（功能/情绪/社会任务）、采购触发事件、痛点与替代方案 | 驱动 `BUYER_STRATEGY.md`，从“买家是谁”深入到“为什么现在采购、怎样判断成功” |
| **Product Marketing** | `coreyhaines31/marketingskills/skills/product-marketing` | MIT | 采购委员会4大角色（使用者/技术评估者/决策者/财务）、异议应对与证明需求 | 组织全站信息架构，为不同采购角色分别提供决策证据与测试报告 |
| **外贸市场研究 Skill** | `liangdabiao/exa-research-mcp-skill/skills/foreign-trade-research` | MIT | 细分品类×目标国研究、官方关税检索、事实与推断三层隔离 | 结合 WTO Tariff & EU Access2Markets 分析贸易格局与季节采购反推 |
| **Anthropic Frontend Design** | `anthropics/skills/skills/frontend-design` (17.5万+ ⭐) | MIT / Apache 2.0 | 反千篇一律与 AI Slop 军规、四大强制上下文约束、两轮设计规划法、大胆留一处克制留全局、功能性主动语态文案 | 驱动 Phase 4 原创视觉导演与前端开发，回答“怎么设计出具独特灵魂的界面”，杜绝 AI 泛化模板 |
| **Vercel Web Interface Guidelines** | `vercel-labs/agent-skills/skills/web-design-guidelines` (3.1万+ ⭐) | Apache 2.0 | 100+ 条 Web 规范、12 维界面体检清单（A11y、聚焦态、表单、动效、微排版、CLS、触控）、file:line 审计标准 | 驱动 Phase 7 上线前第二轮全域界面体检与质量门禁，回答“有没有明显问题”，执行自动化审计脚本 |
| **Taste Skill & cc-skills** | `Leonxlnx/taste-skill` & `samber/cc-skills` | Apache 2.0 | 构图留白、字体密度与呼吸感，设计系统严密审视迭代 | 结合本地排版审计工具，减少泛化模板和未经核实的推断 |
| **Free Tools** | `coreyhaines31/marketingskills/skills/free-tools` | MIT | 用轻量小工具解决真实买家决策问题 | 按需装配 20GP/40HQ 装柜测算器、材料耐温选型表或采购检查表 |
| **Pattern2Code & Design2Code** | Hugging Face NLP / Vision Datasets | Apache 2.0 | 布局还原评测、识别模型过度整齐化（过度对齐）的结构偏差 | 评测原创页面，保护 Hero SKU 与重点大图等“有意义的例外” |
| **b2b-limestone-geo-site-builder** | `cnproduct/b2b-limestone-geo-site-builder` | MIT | 全球标杆发现与三大巨头模型、文化双轨重命名、图实一致质检、Turnstile+Worker | 驱动阶段零标杆排查、去风险重构、询盘全链路与万能5步母模板 |
| **b2b-global-brand-site-master** | `cnproduct/b2b-global-brand-site-master` | MIT | 21 行业精选配置库、默认站点防护（CSP 防嵌套/蜜罐）、海运装柜测算器 | 驱动行业选型、默认边缘安全网关与整柜运费优化计算 |
| **claude-skill-web-clone** | `Jane-xiaoer/claude-skill-web-clone` | MIT | 头号铁律：真源码至上；静态/SSR/动效三大技术决策分支 | 用户明确要求 1:1 完整复刻时，提供严格的逆向取证路径 |
| **website-to-design-md** | `NolanSoloBuilder/skills/skills/website-to-design-md` | MIT | 深度抽取目标网站的 CSS Variables, Colors, Typography 并生成 DESIGN.md | 自动化提取任何标杆站的设计系统与 Surface 分层 |
| **PixelClone-Skill** | `bjvgukv25842-cmyk/PixelClone-Skill` | MIT | 绝对业务契约，保护表单、筛选、跳转等真实交互不被虚假截图化 | 确保复刻与原创页面具备 100% 真实可用的业务行为 |
| **website-rebuild-skill** | `boyang-hu/website-rebuild-skill` | MIT | 证据驱动管线（Evidence-driven pipeline）与量化验证闸门 | 提供可追溯的资产镜像与量化代码校验 |
| **geo-optimizer-skill** | Princeton KDD 2024 Research | 开放学术协议 | 全球 GEO 生成式 AI 引擎优化、47 种提升引用率手段、llms.txt 规范 | 打造面向 ChatGPT Search、Perplexity 等生成式引擎的流量引力场 |
| **Anthropic Skill Creator** | `anthropics/skills/skill-creator` | Apache 2.0 | Skill 结构规范、工作流诊断、两层差距分析与严谨的行为对照评估 | 驱动通用 Skill 优化模式，诊断能力缺口与清除冗余无用提示词 |
| **Hugging Face Skills** | `huggingface/skills` | Apache 2.0 | 数据集/模型安全沙箱边界与评测标准规范 | 驱动从 Hugging Face 发现专业资源，明确界定 Skill 与 Dataset/Model 的技术边界 |

---

## 2. 演进原则 (Evolution Rules)
1. **不整包堆叠外部提示词**：所有外部资源必须提炼为清晰的工作流规则或可执行代码，并在未安装外部工具时自动回退到本地已封装流程。
2. **严禁企业敏感数据外泄**：内部成本、底牌报价、受限测试报告绝对不作为公共数据集上传。
3. **回写经验条目**：每次真实交付后，记录哪些买家表达有效、哪些导致误解，沉淀为经验库。
