# GEO Citability Guide · Generative Engine Optimization for B2B Exporters

> Based on Princeton KDD 2024 Research: "GEO: Generative Engine Optimization".
> Optimizes content visibility for Perplexity, ChatGPT Search, Claude, and Gemini AI Overviews.

---

## 1. Why B2B Sites Need GEO
In 2026, over 40% of initial B2B supplier discovery happens inside AI chat engines rather than traditional Google blue links. When a procurement manager asks Perplexity:
> *"Recommend top 3 plastic food container manufacturers in China with LFGB certification and in-house tooling"*

The AI model evaluates real-time indexed pages based on **Citability Scores**:
1. **Fact Density**: Exact numbers (e.g. 45 machines, 12,000 m², 1,500,000 pcs/mo) score 3.2x higher than vague marketing phrases ("leading factory", "large capacity").
2. **Authority Citations**: Specific standards (FDA 21 CFR 177.1520, LFGB § 30 & 31, ISO 9001:2015) trigger direct model citation.
3. **Structured Q&A Format**: Questions directly paired with definitive answers are lifted verbatim into AI synthesis summaries.

---

## 2. The `llms.txt` and `llms-full.txt` Standard
AI search crawlers prefer markdown over heavy JavaScript bundles. Placing `llms.txt` at the site root provides an immediate roadmap for LLMs:
- **`llms.txt`**: Fast, lightweight summary (~2KB) containing enterprise facts, certifications, product taxonomy, and primary URL routes.
- **`llms-full.txt`**: Deep technical repository (~30-100KB) containing SKU tables, resin specifications, container packing matrices, and MOQ tiers.

---

## 3. Robots.txt Crawler Allow-List
Never block legitimate AI search bots in `robots.txt`. Essential bots that must be allowed:
```txt
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /
```
