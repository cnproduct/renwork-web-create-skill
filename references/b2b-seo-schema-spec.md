# B2B SEO Schema Specification · Five-in-One Structured Data Architecture

> Standard operating procedure for Google Rich Results & Bing B2B rich snippets.

---

## 1. Five Mandatory Schemas
Every high-ranking B2B manufacturing website must implement the following 5 JSON-LD schemas in `<head>`:

### 1.1 Organization Schema
Establishes corporate entity, location, contact points, and domain expertise:
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.example.com/#organization",
  "name": "Xinghui Plastic Life",
  "legalName": "Jieyang Xinghui Plasticware Co., Ltd.",
  "url": "https://www.example.com",
  "foundingDate": "2008",
  "telephone": "+86-15766644288",
  "email": "sales@example.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rongcheng Industrial Zone",
    "addressLocality": "Jieyang",
    "addressRegion": "Guangdong",
    "postalCode": "515500",
    "addressCountry": "CN"
  },
  "knowsAbout": [
    "Plastic Injection Moulding",
    "Food Contact Plasticware OEM",
    "LFGB / FDA Certification"
  ]
}
```

### 1.2 FAQPage Schema
Enables interactive Q&A rich dropdown snippets directly on the Google search results page. Must match visible on-page content word-for-word.

### 1.3 ItemList Schema
Indexes all listed product families or core SKUs with explicit positions and direct landing URLs.

### 1.4 WebSite & WebPage Schemas
Maintains canonical relationship, publisher attribution, and site language.

### 1.5 BreadcrumbList Schema
Displays hierarchical path (Home > Products > Lunch Boxes) instead of raw URLs in search SERPs.
