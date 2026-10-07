# B2B SEO、真实页面与结构化数据

## 页面与路由

每个 TRAFFIC_MAP 意图对应真实可访问且有独特内容的页面：类别、SKU、应用、OEM、技术指南或工厂证据。不要自动对每种筛选组合生成可索引页面；无独立内容/路由的 `?sku=` 不是 SKU 详情页。内部链接让核心内容可发现，重要正文在可渲染 HTML 中，不只放 canvas、图片或 gated PDF。

实际目标域 canonical 与状态/redirect/正文一致；sitemap 仅列可索引 canonical URL，不含错误、noindex、redirect 或未实现语言。语言页面确实翻译并有相应产品/服务，hreflang 自引用且互返，x-default 只有真实回退页时添加。保留现有目标站有效 URL 与必要 301。

title、description、H1、面包屑、正文和图片 alt 为具体页面写；无隐藏关键词/关键词堆砌。联系表单携带真实选型上下文；成功/失败明确，必须确认接收服务，不能定时动画代替提交。

## Schema 按语义选择

| 类型 | 适用内容 | 边界 |
| --- | --- | --- |
| Organization / WebSite | 目标企业与网站 | 真实 name/url/contact/sameAs，稳定 @id，不复制参考身份；WebSite 不自动添加不存在的搜索 Action |
| WebPage / BreadcrumbList | 页面与可见层级 | URL、name、description、inLanguage 与该页一致；图谱引用可复用稳定实体 ID |
| Product / ItemList | 实际产品详情或可见列表 | 不虚构 offers/价格/库存/评分/评论/运输/退换；语义合法与 Google 产品富结果资格是不同判断 |
| Article / TechArticle / Person | 真实文章、作者或审核者 | 作者身份/专业资质与发布/修改时间需证据，不能“创建专家”增加权威 |
| FAQPage | 正文中真实可见问答，按需要 | 截至 2026-10-07 Google 已停止 FAQ 富结果，不把 FAQPage 做成所有 B2B 页必备或承诺问答折叠展示 |

JSON 解析、Schema.org 语义校验、平台支持/富结果资格与实际展示分别验证。Rich Results Test 只识别其支持的类型，不能要求所有 Organization/ItemList 都报告 Google 富结果成功。每次使用重新核对官方支持范围。

## SEO helper 配置契约

`geo_seo_engine.py` 只处理已经构建或导出的公开 HTML，不获取私有事实，不爬网络，不实现翻译，不修改源模板/head。默认 draft，release 须显式选择并完成下面的人工/浏览器复核。

```json
{
  "domain": "https://manufacturer.example",
  "brand_name": "Target Brand",
  "company_name": "Verified Target Company",
  "mode": "draft",
  "pages": [
    {"path": "/", "file": "index.html", "title": "Target Brand", "description": "Verified visible description", "lang": "en"},
    {"path": "/products/", "file": "products/index.html", "title": "Actual products", "description": "Visible product scope", "lang": "en"}
  ],
  "generate_llms": false
}
```

所有身份/路由/title/lang 显式提供，无默认参考品牌。`pages[].alternates` 可选，如 `{"en":"/products/","de":"/de/products/"}`，对应两页必须在 pages 内、HTML 存在且 lang 与映射相符，两页使用相同映射且包含自身；工具不凭 languages 列表猜 URL。`file` 是构建目录内相对路径。

输出 `robots.txt`、`sitemap.xml`、`seo-pages.json`（逐页 canonical、robots、hreflang 和最小 Organization/WebSite/WebPage 图谱）。`generate_llms: true` 时仅把配置页标题/描述投影为可选导航索引；不合成能力/认证，不生成 llms-full 或 AI 端点全家桶。存在输出默认拒绝覆盖，显式 `--overwrite` 前检查差异；不会替用户合并现有复杂 robots 规则；关闭可选 llms 索引时若旧文件仍存在，先审查并移除旧投影再运行，防止残留上一品牌/版本内容。

逐页 SEO 数据需要由代理应用到实际共享模板并重建，再运行原始 HTML与浏览器检查。draft 必须在真实页面或 HTTP 响应配置 noindex；robots Disallow 不是替代品。release 工具拒绝输入中的 noindex、缺失/错误语言和不同域 canonical，但这只是本地静态预检，不能证明线上状态或平台收录。

## 官方来源（本次 2026-10-07 核对）

- [Google AI features](https://developers.google.com/search/docs/appearance/ai-features)：可索引、可显示 snippet 的基本要求；无专属 schema/AI 文件要求。
- [Google AI optimization](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)：原创有用内容与搜索基础，使用前重核。
- [Google updates](https://developers.google.com/search/updates)：2026-05-07 停止 FAQ 富结果；2026-06-15 删除其文档，明确 llms 文件不影响 Google 可见度/排名。
- [多语言页面](https://developers.google.com/search/docs/specialty/international/localized-versions)、[canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)、[结构化数据规则](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)：对应实现逐项核对。
