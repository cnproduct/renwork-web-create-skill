#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Xinghui Plastic Life · 1:1 High-Fidelity Website Generator
Compiles index.html, products.html, lunch-boxes.html, custom-solutions.html,
about.html, contact.html, sitemap.xml, robots.txt, llms.txt, llms-full.txt
with complete B2B SEO & GEO citability optimization.
"""

import os, json, html

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'products.json')

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    products = json.load(f)

# Common Header Component
def get_header(active_nav='home'):
    return f"""
    <!-- Top Utility Bar -->
    <div class="top-utility-bar">
      <div class="page-container top-utility-content">
        <div class="top-social-links">
          <span>Factory Direct OEM / ODM Supplier</span>
          <a href="https://www.youtube.com/@gdxinghui" target="_blank" rel="noopener" aria-label="YouTube">YouTube</a>
          <a href="https://www.facebook.com/profile.php?id=61577398111498" target="_blank" rel="noopener" aria-label="Facebook">Facebook</a>
          <a href="https://www.tiktok.com/@gdxinghui" target="_blank" rel="noopener" aria-label="TikTok">TikTok</a>
        </div>
        <div>
          <span>📞 Export Sales: +86-15766644288</span> | <span>✉️ xhplasticlife@xhplasticlife.com</span>
        </div>
      </div>
    </div>

    <!-- Main Sticky Header -->
    <header class="site-header">
      <div class="page-container site-header-inner">
        <a href="index.html" class="brand-logo-wrap" aria-label="Xinghui Plastic Life Home">
          <div class="brand-logo-text">
            XINGHUI
            <span>Plastic Life</span>
          </div>
        </a>

        <!-- Desktop Navigation -->
        <nav class="main-navigation" aria-label="Primary Navigation">
          <a href="index.html" class="nav-link {'active' if active_nav == 'home' else ''}">Home</a>
          <a href="products.html" class="nav-link {'active' if active_nav == 'products' else ''}">Products</a>
          <a href="lunch-boxes.html" class="nav-link {'active' if active_nav == 'lunch-boxes' else ''}">Lunch Boxes</a>
          <a href="custom-solutions.html" class="nav-link {'active' if active_nav == 'custom' else ''}">Custom Manufacturing</a>
          <a href="about.html" class="nav-link {'active' if active_nav == 'about' else ''}">Why Xinghui</a>
          <a href="contact.html" class="nav-link {'active' if active_nav == 'contact' else ''}">Contact</a>
        </nav>

        <!-- Header Actions: Multilingual & RFQ CTA -->
        <div class="header-actions">
          <div class="lang-dropdown" id="langSelector">
            <button class="lang-btn" aria-label="Select Language">
              <span>EN (Global)</span> ▾
            </button>
            <div class="lang-menu">
              <a href="#" data-lang="en">English (US/Global)</a>
              <a href="#" data-lang="ja">日本語 (Japan)</a>
              <a href="#" data-lang="ru">Русский (Russia)</a>
              <a href="#" data-lang="de">Deutsch (Germany)</a>
              <a href="#" data-lang="fr">Français (France)</a>
              <a href="#" data-lang="es">Español (Spain)</a>
              <a href="#" data-lang="ko">한국어 (Korea)</a>
            </div>
          </div>
          <a href="contact.html" class="btn btn-primary" style="padding: 0.55rem 1.25rem;">Get a Quote</a>
          <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle navigation menu">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </header>

    <!-- Mobile Drawer Navigation -->
    <div class="mobile-drawer" id="mobileDrawer">
      <div class="mobile-drawer-header">
        <div class="brand-logo-text">XINGHUI <span>Plastic Life</span></div>
        <button id="closeDrawer" style="background:none; border:none; font-size:1.5rem; cursor:pointer;" aria-label="Close menu">&times;</button>
      </div>
      <div class="mobile-nav-links">
        <a href="index.html">Home</a>
        <a href="products.html">All Products (63 SKUs)</a>
        <a href="lunch-boxes.html">Wholesale Lunch Boxes</a>
        <a href="custom-solutions.html">Custom Manufacturing</a>
        <a href="about.html">About Factory</a>
        <a href="contact.html">Get Quotation / RFQ</a>
      </div>
      <div style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--color-border);">
        <p style="font-size: 0.875rem; color: var(--color-fg-muted); margin-bottom: 0.5rem;">Direct Export Desk:</p>
        <p><strong>+86-15766644288</strong></p>
        <p>xhplasticlife@xhplasticlife.com</p>
      </div>
    </div>
    """

# Common Footer Component
def get_footer():
    return """
    <footer class="site-footer">
      <div class="page-container">
        <div class="footer-grid">
          <div class="footer-col">
            <div class="brand-logo-text" style="color: #fff; margin-bottom: 1rem;">
              XINGHUI
              <span style="color: var(--color-accent);">Plastic Life · China Factory</span>
            </div>
            <p style="font-size: 0.9375rem; line-height: 1.6; color: rgba(255,255,255,0.7); margin-bottom: 1.5rem;">
              Xinghui is a premier food storage containers and lunch boxes manufacturer in Jieyang, Guangdong, China. Supporting OEM / ODM injection moulding projects for global distributors, supermarket brands, and e-commerce sellers.
            </p>
            <div style="font-size: 0.875rem; color: rgba(255,255,255,0.6);">
              ISO 9001:2015 · BSCI · FDA Compliant · LFGB Certified · BPA Free
            </div>
          </div>

          <div class="footer-col">
            <h4>Product Families</h4>
            <ul>
              <li><a href="lunch-boxes.html">Lunch Boxes (14 SKUs)</a></li>
              <li><a href="products.html?cat=food-storage-containers">Food Storage Containers (27 SKUs)</a></li>
              <li><a href="products.html?cat=kitchen-storage-containers">Kitchen Storage Containers (4 SKUs)</a></li>
              <li><a href="products.html?cat=drinkware">Drinkware & Tumblers (2 SKUs)</a></li>
              <li><a href="products.html?cat=home-storage-containers">Home Storage Containers (12 SKUs)</a></li>
              <li><a href="products.html?cat=portable-organizers">Portable Organizers (4 SKUs)</a></li>
            </ul>
          </div>

          <div class="footer-col">
            <h4>B2B Services</h4>
            <ul>
              <li><a href="custom-solutions.html">OEM & ODM Customization</a></li>
              <li><a href="custom-solutions.html#tooling">In-House Mould Tooling</a></li>
              <li><a href="about.html#compliance">Food Contact Certification</a></li>
              <li><a href="about.html">Jieyang Factory Overview</a></li>
              <li><a href="llms.txt">AI Knowledge Endpoint (llms.txt)</a></li>
              <li><a href="sitemap.xml">XML Sitemap</a></li>
            </ul>
          </div>

          <div class="footer-col">
            <h4>Contact Factory</h4>
            <ul style="gap: 1rem;">
              <li><strong>Factory Address:</strong> Rongcheng District, Jieyang City, Guangdong Province, China</li>
              <li><strong>Phone / WhatsApp:</strong> +86-15766644288</li>
              <li><strong>Export Inquiry:</strong> xhplasticlife@xhplasticlife.com</li>
              <li><strong>Sample Lead Time:</strong> Ready in 3 Days</li>
            </ul>
          </div>
        </div>

        <div class="footer-bottom">
          <div>© 2026 Xinghui Plastic Life (Jieyang Xinghui Plasticware Co., Ltd.). All rights reserved.</div>
          <div style="display: flex; gap: 1.5rem;">
            <a href="llms.txt" style="color:inherit;">llms.txt</a>
            <a href="robots.txt" style="color:inherit;">robots.txt</a>
            <a href="sitemap.xml" style="color:inherit;">sitemap.xml</a>
          </div>
        </div>
      </div>
    </footer>

    <!-- WhatsApp Quick Contact Floating Button -->
    <a href="https://wa.me/8615766644288?text=Hello%20Xinghui%20Factory,%20I%20am%20interested%20in%20your%20food%20storage%20containers%20and%20lunch%20boxes." 
       class="whatsapp-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
      <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-5.46-4.45-9.92-9.91-9.92zm0 18.15c-1.52 0-3.01-.41-4.31-1.18l-.31-.18-3.2.84.85-3.12-.2-.32a8.212 8.212 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24 4.54 0 8.24 3.7 8.24 8.24 0 4.54-3.7 8.24-8.24 8.24zm4.52-6.17c-.25-.12-1.47-.72-1.7-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-2-1.23-.74-.66-1.24-1.47-1.39-1.72-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.4-.42-.56-.43h-.47c-.17 0-.43.06-.66.31-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.57.12.17 1.75 2.67 4.24 3.74.59.26 1.05.41 1.41.53.6.19 1.14.16 1.57.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.15-1.18-.06-.12-.22-.19-.47-.31z"/>
      </svg>
    </a>
    <script src="js/main.js"></script>
    """

# 1. GENERATE INDEX.HTML
def generate_index():
    print("Generating index.html...")
    
    # 6 Product Families data
    families = [
        {
            "name": "Lunch Boxes",
            "desc": "14 SKUs: Microwave-safe bento boxes, multi-compartment meal prep containers, soup bowls with spoon compartments.",
            "img": "https://xinghui-plastic-life-cdn.assetlayer.site/Custom-Lunch-Boxes-Wholesaler-1.webp",
            "link": "lunch-boxes.html"
        },
        {
            "name": "Food Storage Containers",
            "desc": "27 SKUs: Airtight freezer storage boxes, stackable modular pantry containers, glass with snap lids.",
            "img": "https://xinghui-plastic-life-cdn.assetlayer.site/Food-Storage-Containers-Wholesaler-2.webp",
            "link": "products.html?cat=food-storage-containers"
        },
        {
            "name": "Kitchen Storage Containers",
            "desc": "4 SKUs: Spice carousels, oil dispensers, cereal grain storage jars with measurement scales.",
            "img": "https://xinghui-plastic-life-cdn.assetlayer.site/Kitchen-Storage-Containers-Wholesaler-3.webp",
            "link": "products.html?cat=kitchen-storage-containers"
        },
        {
            "name": "Drinkware & Tumblers",
            "desc": "2 SKUs: BPA-free sports water bottles, leakproof travel tumblers, coffee cups.",
            "img": "https://xinghui-plastic-life-cdn.assetlayer.site/Drinkware-Containers-Wholesaler-4.webp",
            "link": "products.html?cat=drinkware"
        },
        {
            "name": "Home Storage Containers",
            "desc": "12 SKUs: Multipurpose drawer dividers, stackable wardrobe boxes, desktop organization bins.",
            "img": "https://xinghui-plastic-life-cdn.assetlayer.site/Home-Storage-Containers-Wholesaler-2.webp",
            "link": "products.html?cat=home-storage-containers"
        },
        {
            "name": "Portable Organizers",
            "desc": "4 SKUs: Compact pill cases, craft supply cases with removable dividers, travel toiletry kits.",
            "img": "https://xinghui-plastic-life-cdn.assetlayer.site/Portable-Organizers-Wholesaler-6.webp",
            "link": "products.html?cat=portable-organizers"
        }
    ]

    families_html = ""
    for fam in families:
        families_html += f"""
        <article class="family-card">
          <div class="family-card-img-wrap">
            <img src="{fam['img']}" alt="{fam['name']} Manufacturer" loading="lazy">
          </div>
          <div class="family-card-body">
            <h3 class="family-card-title">{fam['name']}</h3>
            <p style="font-size:0.9375rem; color:var(--color-fg-muted); margin-bottom:1rem;">{fam['desc']}</p>
            <div class="family-card-action">
              <a href="{fam['link']}" style="color:var(--color-accent-strong); font-weight:600;">Explore Models →</a>
            </div>
          </div>
        </article>
        """

    # 63 Products Cards for Homepage Catalogue
    product_cards_html = ""
    for p in products:
        tags_html = "".join([f'<span class="catalogue-tag">{html.escape(t)}</span>' for t in p.get('tags', []) if t and t != '→'])
        product_cards_html += f"""
        <article class="catalogue-product-card" data-category="{p.get('category', 'all')}" data-title="{html.escape(p['name'])}">
          <div class="catalogue-card-img-wrap">
            <img src="{p['img']}" alt="{html.escape(p['name'])}" loading="lazy">
          </div>
          <div class="catalogue-card-body">
            <h4 class="catalogue-card-title" title="{html.escape(p['name'])}">{html.escape(p['name'])}</h4>
            <div class="catalogue-card-meta">
              <span class="catalogue-tag" style="background:#e9e9d2; color:#516b4b;">Factory Direct</span>
              {tags_html}
            </div>
            <div style="margin-top:1rem; padding-top:0.75rem; border-top:1px solid #eee; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.8125rem; color:var(--color-fg-muted);">MOQ: 1,000 pcs</span>
              <a href="contact.html?sku={html.escape(p['name'])}" class="btn btn-outline" style="padding:0.35rem 0.75rem; font-size:0.8125rem;">Request Quote</a>
            </div>
          </div>
        </article>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Food Storage Containers Manufacturer in China | Xinghui Plastic Life</title>
  <meta name="description" content="Xinghui is a food storage containers manufacturer in China, supplying lunch boxes and household plasticware with OEM and ODM support for B2B buyers.">
  <meta name="keywords" content="food storage containers manufacturer, wholesale lunch boxes china, plasticware factory jieyang, oem odm meal prep containers, bulk bento boxes">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://www.xhplasticlife.com/">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.xhplasticlife.com/">
  <meta property="og:title" content="Food Storage Containers Manufacturer in China | Xinghui Plastic Life">
  <meta property="og:description" content="Xinghui is a food storage containers manufacturer in China, supplying lunch boxes and household plasticware with OEM and ODM support for B2B buyers.">
  <meta property="og:image" content="https://xinghui-plastic-life-cdn.assetlayer.site/Wholesale-Food-Storage-Containers-Manufacturer-Xinghui-banner.webp">
  <meta property="og:site_name" content="Xinghui Plastic Life">
  <meta property="og:locale" content="en_US">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Food Storage Containers Manufacturer in China | Xinghui">
  <meta name="twitter:description" content="Xinghui is a food storage containers manufacturer in China, supplying lunch boxes and household plasticware with OEM and ODM support for B2B buyers.">
  <meta name="twitter:image" content="https://xinghui-plastic-life-cdn.assetlayer.site/Wholesale-Food-Storage-Containers-Manufacturer-Xinghui-banner.webp">

  <link rel="stylesheet" href="css/style.css">

  <!-- JSON-LD Structured Data Schema Matrix -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": "https://www.xhplasticlife.com/#organization",
    "name": "Xinghui Plastic Life",
    "legalName": "Jieyang Xinghui Plasticware Co., Ltd.",
    "url": "https://www.xhplasticlife.com",
    "logo": "https://www.xhplasticlife.com/brand-logo.webp",
    "description": "Xinghui injection-moulds food storage containers, lunch boxes and household plasticware with OEM and ODM support in Jieyang, Guangdong, China.",
    "foundingDate": "2008",
    "telephone": "+86-15766644288",
    "email": "xhplasticlife@xhplasticlife.com",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Rongcheng Industrial Zone",
      "addressLocality": "Jieyang",
      "addressRegion": "Guangdong",
      "postalCode": "515500",
      "addressCountry": "CN"
    }},
    "knowsAbout": [
      "Plastic Injection Moulding",
      "OEM Food Storage Containers",
      "Bento Lunch Boxes Wholesale",
      "LFGB Food Contact Testing",
      "FDA 21 CFR Compliant Plastics",
      "Private Label Packaging for Amazon FBA"
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": "https://www.xhplasticlife.com/#website",
    "name": "Xinghui Plastic Life",
    "url": "https://www.xhplasticlife.com",
    "publisher": {{
      "@id": "https://www.xhplasticlife.com/#organization"
    }},
    "inLanguage": "en"
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "@id": "https://www.xhplasticlife.com",
    "url": "https://www.xhplasticlife.com",
    "name": "Food Storage Containers Manufacturer in China",
    "isPartOf": {{
      "@id": "https://www.xhplasticlife.com/#website"
    }},
    "publisher": {{
      "@id": "https://www.xhplasticlife.com/#organization"
    }},
    "description": "Browse 63 SKUs across six product families for wholesale and custom OEM/ODM production."
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "url": "https://www.xhplasticlife.com/lunch-boxes.html", "name": "Lunch Boxes"}},
      {{"@type": "ListItem", "position": 2, "url": "https://www.xhplasticlife.com/products.html?cat=food-storage-containers", "name": "Food Storage Containers"}},
      {{"@type": "ListItem", "position": 3, "url": "https://www.xhplasticlife.com/products.html?cat=kitchen-storage-containers", "name": "Kitchen Storage Containers"}},
      {{"@type": "ListItem", "position": 4, "url": "https://www.xhplasticlife.com/products.html?cat=drinkware", "name": "Drinkware"}},
      {{"@type": "ListItem", "position": 5, "url": "https://www.xhplasticlife.com/products.html?cat=home-storage-containers", "name": "Home Storage Containers"}},
      {{"@type": "ListItem", "position": 6, "url": "https://www.xhplasticlife.com/products.html?cat=portable-organizers", "name": "Portable Organizers"}}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "Which food storage container categories can Xinghui supply?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "The published catalogue has 63 SKUs across six families: lunch boxes, food storage containers, kitchen storage, home storage, drinkware and portable organisers."
        }}
      }},
      {{
        "@type": "Question",
        "name": "What can OEM and ODM food storage container projects include?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Light customisation covers logo, custom Pantone color and retail packaging. Deeper projects include structural design, 3D prototyping, new mould tooling, and material substitution (PP, Tritan, silicone, glass, 304 stainless steel)."
        }}
      }},
      {{
        "@type": "Question",
        "name": "What information should I include in a quotation request?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Share the product family or SKU code, material requirement, capacity, estimated order quantity, destination country, and whether you need existing moulds or private tooling. Test documentation is matched to your target destination market."
        }}
      }}
    ]
  }}
  </script>
</head>
<body>

  {get_header(active_nav='home')}

  <!-- Section 0: Hero Section -->
  <section class="home-hero surface-media">
    <div class="page-container hero-grid">
      <div class="hero-content">
        <span class="eyebrow">Injection Moulding · OEM / ODM Factory</span>
        <h1>Food Storage Containers Manufacturer in China</h1>
        <p class="hero-lead">
          Explore 63 listed SKUs across six food storage, lunch box and household-plasticware families. Request current material, intended-use and destination-market documentation for the model you select.
        </p>
        <div class="hero-cta-group">
          <a href="contact.html" class="btn btn-primary">Talk to Our Experts</a>
          <a href="#catalogue" class="btn btn-secondary">Explore All 63 SKUs</a>
        </div>
        <div class="hero-badges-wrap">
          <div class="hero-badges-title">Strict Food-Contact Compliance & Export Certifications:</div>
          <div class="hero-badges-list">
            <span class="hero-badge-pill">FDA 21 CFR</span>
            <span class="hero-badge-pill">LFGB Certified</span>
            <span class="hero-badge-pill">BPA-Free 100%</span>
            <span class="hero-badge-pill">ISO 9001:2015</span>
            <span class="hero-badge-pill">BSCI Audited</span>
            <span class="hero-badge-pill">Sedex SMETA</span>
            <span class="hero-badge-pill">REACH / RoHS</span>
          </div>
        </div>
      </div>
      <div class="hero-preview-card">
        <div class="hero-preview-img">
          <img src="https://xinghui-plastic-life-cdn.assetlayer.site/Wholesale-Food-Storage-Containers-Manufacturer-Xinghui-banner.webp" alt="Wholesale Food Storage Containers Manufacturer" loading="eager">
        </div>
        <div style="margin-top:1rem; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-weight:700; color:#fff;">Factory Direct Sourcing</div>
            <div style="font-size:0.8125rem; color:rgba(255,255,255,0.7);">Jieyang Production Base · 45 Injection Lines</div>
          </div>
          <span style="background:var(--color-accent-strong); color:#fff; padding:0.25rem 0.75rem; border-radius:4px; font-size:0.75rem; font-weight:700;">ACTIVE INVENTORY</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 1: Trust Bridge (4-Column Bento Ribbon) -->
  <section class="surface-sunken trust-bridge">
    <div class="page-container trust-bridge-grid">
      <div class="trust-item">
        <div class="trust-item-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        <h3>OEM and ODM Under One Roof</h3>
        <p>Logo, colour and packaging for light work; structural design, material substitution and new moulds for deep work.</p>
      </div>

      <div class="trust-item">
        <div class="trust-item-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        </div>
        <h3>Six Families, 63 Listed SKUs</h3>
        <p>Lunch boxes, food storage, kitchen storage, home storage, drinkware and portable organisers in one catalogue.</p>
      </div>

      <div class="trust-item">
        <div class="trust-item-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
        </div>
        <h3>Food-Contact Documentation</h3>
        <p>Request product-specific test reports and documentation that match your selected material, model and destination market.</p>
      </div>

      <div class="trust-item">
        <div class="trust-item-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24"/><path d="m14.83 9.17 4.24-4.24"/><path d="m14.83 14.83 4.24 4.24"/><path d="m9.17 14.83-4.24 4.24"/></svg>
        </div>
        <h3>Material Range Matched to Use</h3>
        <p>Explore PP, PS, PET, silicone, glass and 304 stainless-steel options. Material suitability and use conditions are reviewed model by model.</p>
      </div>
    </div>
  </section>

  <!-- Section 2: Six Product Families Showcase -->
  <section class="surface-white section-padding">
    <div class="page-container">
      <div style="text-align: center; max-width: 780px; margin: 0 auto 2.5rem;">
        <span class="eyebrow">Product Classification</span>
        <h2 class="section-title">Wholesale Food Storage Containers Across Six Product Families</h2>
        <p class="section-lead" style="margin: 0 auto;">
          Whether supplying retail hypermarkets or Amazon brand stores, our injection-moulded catalogue offers standardized tooling and flexible private-label customization.
        </p>
      </div>

      <div class="families-grid">
        {families_html}
      </div>
    </div>
  </section>

  <!-- Section 3: Interactive 63-SKU Catalogue Engine -->
  <section id="catalogue" class="surface-light section-padding" style="border-top:1px solid var(--color-border); border-bottom:1px solid var(--color-border);">
    <div class="page-container">
      <div style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:1rem;">
        <div>
          <span class="eyebrow">Factory Inventory</span>
          <h2 class="section-title" style="margin-bottom:0.5rem;">A 63-SKU Catalogue for Wholesale & Custom Projects</h2>
          <p class="section-lead">Filter active injection moulds, compare capacities, and request immediate tiered B2B pricing.</p>
        </div>
        <div style="font-size:0.9375rem; color:var(--color-fg-muted);">
          Current Database: <strong>63 SKUs</strong> Ready for Bulk Production
        </div>
      </div>

      <div class="catalogue-layout">
        <!-- Sidebar Filter -->
        <aside class="catalogue-sidebar">
          <label class="catalogue-search">
            <span style="font-size:0.875rem; font-weight:600; color:var(--color-fg);">Search SKUs & Keywords</span>
            <input type="search" id="catalogueSearch" placeholder="Search by model, volume, ramen, bento...">
          </label>

          <div style="margin-top:1.5rem;">
            <strong style="display:block; font-size:0.875rem; text-transform:uppercase; letter-spacing:0.05em; color:var(--color-fg-muted); margin-bottom:0.75rem;">Product Families</strong>
            <div class="catalogue-category-list">
              <button class="cat-btn active" data-cat="all">
                <span>All Products</span>
                <span class="cat-count">63</span>
              </button>
              <button class="cat-btn" data-cat="lunch-boxes">
                <span>Lunch Boxes</span>
                <span class="cat-count">14</span>
              </button>
              <button class="cat-btn" data-cat="food-storage-containers">
                <span>Food Storage</span>
                <span class="cat-count">27</span>
              </button>
              <button class="cat-btn" data-cat="kitchen-storage-containers">
                <span>Kitchen Storage</span>
                <span class="cat-count">4</span>
              </button>
              <button class="cat-btn" data-cat="drinkware">
                <span>Drinkware</span>
                <span class="cat-count">2</span>
              </button>
              <button class="cat-btn" data-cat="home-storage-containers">
                <span>Home Storage</span>
                <span class="cat-count">12</span>
              </button>
              <button class="cat-btn" data-cat="portable-organizers">
                <span>Portable Organizers</span>
                <span class="cat-count">4</span>
              </button>
            </div>
          </div>
        </aside>

        <!-- Product Grid Results -->
        <main class="catalogue-results">
          <div class="catalogue-results-meta">
            <p class="catalogue-results-count">
              Showing <strong id="resultsCount">63</strong> models matching specifications
            </p>
            <div style="font-size:0.875rem; color:var(--color-fg-muted);">
              Sorted by: <strong>B2B Popularity</strong>
            </div>
          </div>

          <div class="catalogue-product-grid" id="productGrid">
            {product_cards_html}
          </div>
        </main>
      </div>
    </div>
  </section>

  <!-- Section 4: Customization Process Section -->
  <section class="surface-white section-padding">
    <div class="page-container">
      <div style="text-align: center; max-width: 780px; margin: 0 auto 3rem;">
        <span class="eyebrow">OEM / ODM Workflow</span>
        <h2 class="section-title">Our Customization Process for Food Storage Containers</h2>
        <p class="section-lead" style="margin: 0 auto;">
          From ready-mould branding to full custom tool development, we provide transparent project milestones and rapid physical sample verification.
        </p>
      </div>

      <div class="process-grid">
        <div class="process-card">
          <div class="process-step-num">01</div>
          <h3>Project Brief</h3>
          <p>Confirm container capacity, resin type (PP, PS, Tritan), airtight gasket requirements, and intended retail price band.</p>
        </div>
        <div class="process-card">
          <div class="process-step-num">02</div>
          <h3>3D Prototyping</h3>
          <p>CAD modeling and high-precision SLA 3D printed samples within 72 hours for ergonomic and fit verification.</p>
        </div>
        <div class="process-card">
          <div class="process-step-num">03</div>
          <h3>Tooling & Trial</h3>
          <p>In-house CNC mold machining, T1 sample injection, mold flow testing, and leak-proof pressure testing.</p>
        </div>
        <div class="process-card">
          <div class="process-step-num">04</div>
          <h3>Bulk Production</h3>
          <p>Automated injection runs, silk-screen printing, customized barcode labeling, and containerized export dispatch.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 5: Manufacturing Capabilities & Factory Stats -->
  <section class="surface-sunken section-padding">
    <div class="page-container">
      <div style="display:grid; grid-template-columns:1fr; gap:3rem; align-items:center;" class="lg:grid-cols-2">
        <div>
          <span class="eyebrow">Manufacturing Powerhouse</span>
          <h2 class="section-title">Full-Scale Food Storage Containers Manufacturing Capabilities</h2>
          <p style="font-size:1.05rem; color:var(--color-fg-muted); line-height:1.7; margin-bottom:1.5rem;">
            Headquartered in Jieyang, Guangdong, Xinghui operates a modern injection-moulding facility dedicated to commercial plasticware. We engineer structural leak-proof locks, thermal insulation bento boxes, and stackable modular pantry containers.
          </p>
          <ul style="list-style:none; display:flex; flex-direction:column; gap:0.75rem; margin-bottom:2rem;">
            <li>✓ <strong>In-House Tooling Workshop:</strong> Rapid mold development within 25 days.</li>
            <li>✓ <strong>Raw Material Quality Control:</strong> Virgin food-grade polymer with full batch test certificates.</li>
            <li>✓ <strong>Automated Production:</strong> Robotic arm pickers ensuring zero oil contamination.</li>
          </ul>
          <a href="about.html" class="btn btn-primary">Learn More About Xinghui Factory</a>
        </div>

        <div class="stats-banner" style="margin-top:0;">
          <div class="stat-box">
            <div class="stat-number">45+</div>
            <div class="stat-label">Injection Machines</div>
          </div>
          <div class="stat-box">
            <div class="stat-number">12k</div>
            <div class="stat-label">Square Meters Plant</div>
          </div>
          <div class="stat-box">
            <div class="stat-number">50k</div>
            <div class="stat-label">Daily Capacity (pcs)</div>
          </div>
          <div class="stat-box">
            <div class="stat-number">2008</div>
            <div class="stat-label">Year Established</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 6: Trusted Global Brands & Partners -->
  <section class="surface-white section-padding" style="border-bottom:1px solid var(--color-border);">
    <div class="page-container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto;">
        <span class="eyebrow">Client Validation</span>
        <h2 class="section-title">Trusted by Retail Chains, Importers & Brand Owners</h2>
        <p class="section-lead" style="margin: 0 auto;">
          Our containers are sourced and distributed across North America, Europe, Japan, and Southeast Asia.
        </p>
      </div>

      <div class="partner-grid">
        <div class="partner-logo-item"><img src="https://xinghui-plastic-life-cdn.assetlayer.site/Food-Storage-Containers-Manufacturer-with-Coca-Cola2.webp" alt="Coca-Cola Partner"></div>
        <div class="partner-logo-item"><img src="https://xinghui-plastic-life-cdn.assetlayer.site/Food-Storage-Containers-Manufacturer-with-TCL-6.webp" alt="TCL Partner"></div>
        <div class="partner-logo-item"><img src="https://xinghui-plastic-life-cdn.assetlayer.site/Food-Storage-Containers-Manufacturer-with-Midea-4.webp" alt="Midea Partner"></div>
        <div class="partner-logo-item"><img src="https://xinghui-plastic-life-cdn.assetlayer.site/Food-Storage-Containers-Manufacturer-with-miniso-2.webp" alt="MINISO Partner"></div>
        <div class="partner-logo-item"><img src="https://xinghui-plastic-life-cdn.assetlayer.site/Food-Storage-Containers-Partners-with-Amazon-1.webp" alt="Amazon FBA Partner"></div>
        <div class="partner-logo-item"><img src="https://xinghui-plastic-life-cdn.assetlayer.site/Food-Storage-Containers-Manufacturer-with-Crest-1.webp" alt="Crest Partner"></div>
        <div class="partner-logo-item"><img src="https://xinghui-plastic-life-cdn.assetlayer.site/Food-Storage-Containers-Partners-with-Walmart-5.webp" alt="Walmart Partner"></div>
        <div class="partner-logo-item"><img src="https://xinghui-plastic-life-cdn.assetlayer.site/Food-Storage-Containers-Partners-with-watsons-3.webp" alt="Watsons Partner"></div>
      </div>
    </div>
  </section>

  <!-- Section 7: Interactive FAQ Accordion -->
  <section class="surface-light section-padding">
    <div class="page-container">
      <div style="text-align: center; max-width: 780px; margin: 0 auto;">
        <span class="eyebrow">Procurement Clarity</span>
        <h2 class="section-title">Questions B2B Buyers Ask Before Requesting a Quote</h2>
        <p class="section-lead" style="margin: 0 auto;">
          Everything you need to know regarding minimum order quantities, certifications, and private mold investments.
        </p>
      </div>

      <div class="faq-list">
        <details class="faq-item" open>
          <summary class="faq-question">
            <span>Which food storage container categories can Xinghui supply?</span>
            <span class="faq-icon">▾</span>
          </summary>
          <div class="faq-answer">
            The published catalogue has 63 SKUs across six families: lunch boxes, food storage containers, kitchen storage, home storage, drinkware and portable organisers. We supply standard injection moulds, dual-injection silicone seals, and stainless-steel hybrid boxes.
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">
            <span>What can OEM and ODM food storage container projects include?</span>
            <span class="faq-icon">▾</span>
          </summary>
          <div class="faq-answer">
            Light customisation can cover custom logo printing (silk screen, heat transfer, in-mould labelling), bespoke Pantone masterbatch colours, and retail packaging (color box, sleeve, shrink wrap). Deeper projects include structural design, 3D prototype printing, new mould tooling, and alternative food-contact resins.
          </div>
        </details>

        <details class="faq-item">
          <summary class="faq-question">
            <span>What information should I include in a quotation request?</span>
            <span class="faq-icon">▾</span>
          </summary>
          <div class="faq-answer">
            Share the product family, material requirement, capacity, target order quantity, and destination market. Also inform us whether you need existing moulds or private tooling. Test documentation (FDA, LFGB, BPA-free) is reviewed and provided model by model.
          </div>
        </details>
      </div>
    </div>
  </section>

  <!-- Section 8: B2B RFQ Lead Closer -->
  <section class="surface-white section-padding" style="border-top:1px solid var(--color-border);">
    <div class="page-container">
      <div class="rfq-box">
        <div class="rfq-box-grid">
          <div>
            <span class="eyebrow">Direct Factory Communication</span>
            <h2 class="section-title" style="margin-bottom:1rem;">Send Us an Inquiry — Let’s Discuss Your Product</h2>
            <p style="color:var(--color-fg-muted); line-height:1.7; margin-bottom:2rem;">
              Tell us the product family, capacity, target quantity, and export destination. Our engineering sales team will return with detailed CAD specs, tiered pricing, and sample delivery timelines within 12 hours.
            </p>
            <div style="display:flex; flex-direction:column; gap:1rem;">
              <div><strong>📍 Factory:</strong> Rongcheng District, Jieyang, Guangdong, China</div>
              <div><strong>📞 Phone / WhatsApp:</strong> +86-15766644288</div>
              <div><strong>✉️ Email:</strong> xhplasticlife@xhplasticlife.com</div>
              <div><strong>⚡ Response SLA:</strong> Guaranteed quotation within 12 Hours</div>
            </div>
          </div>

          <form class="rfq-form rfq-form-submit">
            <div class="form-group">
              <label class="form-label" for="rfq-name">Your Full Name *</label>
              <input type="text" id="rfq-name" name="name" class="form-control" placeholder="e.g. John Smith" required>
            </div>
            <div class="form-group">
              <label class="form-label" for="rfq-email">Business Email *</label>
              <input type="email" id="rfq-email" name="email" class="form-control" placeholder="john@company.com" required>
            </div>
            <div class="form-group">
              <label class="form-label" for="rfq-company">Company & Country *</label>
              <input type="text" id="rfq-company" name="company" class="form-control" placeholder="Company Name / Destination Port" required>
            </div>
            <div class="form-group">
              <label class="form-label" for="rfq-product">Product Family or SKU Code</label>
              <input type="text" id="rfq-product" name="product" class="form-control" placeholder="e.g. 1.3L Bento Lunch Box (BX1051)">
            </div>
            <div class="form-group">
              <label class="form-label" for="rfq-quantity">Estimated Order Volume</label>
              <select id="rfq-quantity" name="quantity" class="form-control">
                <option value="Sample Request">Physical Sample Evaluation (< 50 pcs)</option>
                <option value="1,000 - 3,000 pcs">1,000 - 3,000 pcs (Trial Run)</option>
                <option value="3,000 - 10,000 pcs">3,000 - 10,000 pcs (Standard Bulk)</option>
                <option value="10,000+ pcs">10,000+ pcs (Full Container 20GP/40HQ)</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label" for="rfq-message">Project Requirements / Customization Needs</label>
              <textarea id="rfq-message" name="message" class="form-control" rows="3" placeholder="Tell us about custom colors, logo printing, or private tooling needs..."></textarea>
            </div>
            <button type="submit" class="btn btn-primary" style="width:100%; margin-top:0.5rem;">Submit Quotation Request →</button>
          </form>
        </div>
      </div>
    </div>
  </section>

  {get_footer()}

</body>
</html>
"""
    with open(os.path.join(BASE_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("index.html successfully created.")

# 2. GENERATE PRODUCTS.HTML
def generate_products():
    print("Generating products.html...")
    product_cards_html = ""
    for p in products:
        tags_html = "".join([f'<span class="catalogue-tag">{html.escape(t)}</span>' for t in p.get('tags', []) if t and t != '→'])
        product_cards_html += f"""
        <article class="catalogue-product-card" data-category="{p.get('category', 'all')}" data-title="{html.escape(p['name'])}">
          <div class="catalogue-card-img-wrap">
            <img src="{p['img']}" alt="{html.escape(p['name'])}" loading="lazy">
          </div>
          <div class="catalogue-card-body">
            <h4 class="catalogue-card-title" title="{html.escape(p['name'])}">{html.escape(p['name'])}</h4>
            <div class="catalogue-card-meta">
              <span class="catalogue-tag" style="background:#e9e9d2; color:#516b4b;">Factory Mould</span>
              {tags_html}
            </div>
            <div style="margin-top:1rem; padding-top:0.75rem; border-top:1px solid #eee; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:0.8125rem; color:var(--color-fg-muted);">MOQ: 1,000 pcs</span>
              <a href="contact.html?sku={html.escape(p['name'])}" class="btn btn-outline" style="padding:0.35rem 0.75rem; font-size:0.8125rem;">RFQ Details</a>
            </div>
          </div>
        </article>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wholesale Food Storage Containers | 63 SKUs Catalogue | Xinghui</title>
  <meta name="description" content="Browse Xinghui wholesale food storage containers, lunch boxes and household plasticware for distributors, brands and importers. 63 SKUs available for OEM/ODM.">
  <meta name="keywords" content="wholesale food storage containers, bulk lunch boxes, kitchen organizers supplier, meal prep container factory">
  <link rel="canonical" href="https://www.xhplasticlife.com/products.html">
  <link rel="stylesheet" href="css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "Wholesale Food Storage Containers Catalogue",
    "description": "Complete 63 SKUs catalogue of food storage containers and bento boxes.",
    "url": "https://www.xhplasticlife.com/products.html"
  }}
  </script>
</head>
<body>
  {get_header(active_nav='products')}

  <div class="surface-tint section-padding" style="padding-bottom: 2.5rem;">
    <div class="page-container">
      <span class="eyebrow">Standardized Mould Inventory</span>
      <h1 class="section-title">Wholesale Food Storage Containers Catalogue</h1>
      <p class="section-lead">
        Explore 63 listed SKUs across six product families: lunch boxes, airtight food storage, kitchen organization, drinkware, and home storage.
      </p>
    </div>
  </div>

  <div class="page-container section-padding" style="padding-top: 2.5rem;">
    <div class="catalogue-layout">
      <aside class="catalogue-sidebar">
        <label class="catalogue-search">
          <span style="font-size:0.875rem; font-weight:600; color:var(--color-fg);">Search SKUs & Keywords</span>
          <input type="search" id="catalogueSearch" placeholder="Search by model, volume, ramen...">
        </label>

        <div style="margin-top:1.5rem;">
          <strong style="display:block; font-size:0.875rem; text-transform:uppercase; letter-spacing:0.05em; color:var(--color-fg-muted); margin-bottom:0.75rem;">Product Families</strong>
          <div class="catalogue-category-list">
            <button class="cat-btn active" data-cat="all"><span>All Products</span><span class="cat-count">63</span></button>
            <button class="cat-btn" data-cat="lunch-boxes"><span>Lunch Boxes</span><span class="cat-count">14</span></button>
            <button class="cat-btn" data-cat="food-storage-containers"><span>Food Storage</span><span class="cat-count">27</span></button>
            <button class="cat-btn" data-cat="kitchen-storage-containers"><span>Kitchen Storage</span><span class="cat-count">4</span></button>
            <button class="cat-btn" data-cat="drinkware"><span>Drinkware</span><span class="cat-count">2</span></button>
            <button class="cat-btn" data-cat="home-storage-containers"><span>Home Storage</span><span class="cat-count">12</span></button>
            <button class="cat-btn" data-cat="portable-organizers"><span>Portable Organizers</span><span class="cat-count">4</span></button>
          </div>
        </div>
      </aside>

      <main class="catalogue-results">
        <div class="catalogue-results-meta">
          <p class="catalogue-results-count">Showing <strong id="resultsCount">63</strong> products</p>
          <a href="contact.html" class="btn btn-primary" style="padding:0.4rem 1rem; font-size:0.875rem;">Request Full PDF Catalogue</a>
        </div>
        <div class="catalogue-product-grid" id="productGrid">
          {product_cards_html}
        </div>
      </main>
    </div>
  </div>

  {get_footer()}
</body>
</html>"""
    with open(os.path.join(BASE_DIR, 'products.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("products.html successfully created.")

# 3. GENERATE LUNCH-BOXES.HTML
def generate_lunch_boxes():
    print("Generating lunch-boxes.html...")
    lb_products = [p for p in products if p.get('category') == 'lunch-boxes']
    cards_html = ""
    for p in lb_products:
        cards_html += f"""
        <article class="catalogue-product-card" data-category="lunch-boxes" data-title="{html.escape(p['name'])}">
          <div class="catalogue-card-img-wrap">
            <img src="{p['img']}" alt="{html.escape(p['name'])}" loading="lazy">
          </div>
          <div class="catalogue-card-body">
            <h4 class="catalogue-card-title">{html.escape(p['name'])}</h4>
            <div style="font-size:0.875rem; color:var(--color-fg-muted); margin:0.5rem 0;">Food Contact: PP + Silicone Seal | Microwave Safe</div>
            <a href="contact.html?sku={html.escape(p['name'])}" class="btn btn-outline" style="width:100%; margin-top:auto; font-size:0.8125rem;">Request Quotation</a>
          </div>
        </article>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wholesale Lunch Box Manufacturer | Bento Box Supplier China | Xinghui</title>
  <meta name="description" content="Source wholesale plastic and stainless steel lunch boxes from Xinghui. Compare models, multi-compartment bento containers, and discuss OEM/ODM private label.">
  <link rel="canonical" href="https://www.xhplasticlife.com/lunch-boxes.html">
  <link rel="stylesheet" href="css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "Xinghui Wholesale Bento Lunch Boxes",
    "description": "Microwave-safe, leak-proof compartment food boxes for wholesale and private label brand supply.",
    "brand": {{"@type": "Brand", "name": "Xinghui Plastic Life"}},
    "offers": {{
      "@type": "AggregateOffer",
      "priceCurrency": "USD",
      "lowPrice": "0.75",
      "highPrice": "3.50",
      "offerCount": "14"
    }}
  }}
  </script>
</head>
<body>
  {get_header(active_nav='lunch-boxes')}

  <div class="surface-media section-padding" style="background: linear-gradient(135deg, rgba(27,36,25,0.95), rgba(36,47,34,0.9)), url('https://xinghui-plastic-life-cdn.assetlayer.site/Custom-Lunch-Boxes-Wholesaler-1.webp') center/cover;">
    <div class="page-container">
      <span class="eyebrow" style="color:var(--color-accent);">Core Category Focus</span>
      <h1 class="section-title">Wholesale Lunch Box Manufacturer</h1>
      <p class="section-lead">
        Explore 14 specialized bento models in current production: from single-tier salad containers to 3-compartment microwavable meal prep boxes with utensil storage.
      </p>
    </div>
  </div>

  <div class="page-container section-padding">
    <h2 class="section-title" style="margin-bottom:2rem;">Wholesale Lunch Boxes in Current Catalogue</h2>
    <div class="catalogue-product-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));">
      {cards_html}
    </div>

    <div class="rfq-box" style="margin-top: 4rem;">
      <h2 class="section-title" style="font-size:1.75rem;">How to Select a Lunch Box for Wholesale Supply</h2>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:2rem; margin-top:1.5rem;" class="sm:grid-cols-2">
        <div>
          <h4>1. Seal Structure & Gasket Type</h4>
          <p style="color:var(--color-fg-muted); font-size:0.9375rem;">Dual-injected silicone gaskets prevent sauce leaking between compartments. Detachable seals facilitate dishwasher sanitization.</p>
        </div>
        <div>
          <h4>2. Thermal Range & Microwave Vent</h4>
          <p style="color:var(--color-fg-muted); font-size:0.9375rem;">PP containers withstand -20°C freezer temperatures up to 120°C microwave reheating. Built-in silicone steam release valves.</p>
        </div>
        <div>
          <h4>3. Compartment Partitioning</h4>
          <p style="color:var(--color-fg-muted); font-size:0.9375rem;">1-compartment ramen bowls, 2-compartment side dishes, and 3-compartment balanced diet meal prep containers.</p>
        </div>
        <div>
          <h4>4. Custom Color & Branding</h4>
          <p style="color:var(--color-fg-muted); font-size:0.9375rem;">Custom Pantone injection color matching from 1,000 pcs; in-mold labeling (IML) and heat transfer printing for retail packaging.</p>
        </div>
      </div>
    </div>
  </div>

  {get_footer()}
</body>
</html>"""
    with open(os.path.join(BASE_DIR, 'lunch-boxes.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("lunch-boxes.html successfully created.")

# 4. GENERATE CUSTOM-SOLUTIONS.HTML
def generate_custom_solutions():
    print("Generating custom-solutions.html...")
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Custom Food Storage Containers | OEM & ODM Moulding | Xinghui</title>
  <meta name="description" content="Develop custom food storage containers with Xinghui: ready-to-make branding, in-house tooling, 3D prototypes, and mass injection moulding in Jieyang, China.">
  <link rel="canonical" href="https://www.xhplasticlife.com/custom-solutions.html">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  {get_header(active_nav='custom')}

  <div class="surface-tint section-padding">
    <div class="page-container">
      <span class="eyebrow">Engineering OEM / ODM</span>
      <h1 class="section-title">Custom Food Storage Containers for Your Brand</h1>
      <p class="section-lead">
        From branding established stock molds to engineering entirely new leak-proof structures from CAD sketches, our Jieyang factory provides complete turn-key manufacturing.
      </p>
    </div>
  </div>

  <div class="page-container section-padding">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem; margin-bottom:4rem;" class="sm:grid-cols-2">
      <div style="background:var(--color-light); padding:2rem; border-radius:var(--radius-md); border:1px solid var(--color-border);">
        <h3 style="font-family:var(--font-display); font-size:1.5rem; margin-bottom:1rem; color:var(--color-accent-strong);">Route A: Light Customisation</h3>
        <p style="color:var(--color-fg-muted); margin-bottom:1.5rem;">Fastest route to market (15-20 days). Leverage Xinghui's 63 existing moulds with custom branding.</p>
        <ul style="list-style:none; display:flex; flex-direction:column; gap:0.5rem; font-size:0.9375rem;">
          <li>✓ Custom Pantone Masterbatch Injection</li>
          <li>✓ Silk Screen / Heat Transfer / In-Mould Labelling (IML)</li>
          <li>✓ Custom Retail Gift Box, Card Sleeves, UPC Barcodes</li>
          <li>✓ MOQ starting from 1,000 pcs per SKU</li>
        </ul>
      </div>

      <div style="background:var(--color-light); padding:2rem; border-radius:var(--radius-md); border:1px solid var(--color-border);">
        <h3 style="font-family:var(--font-display); font-size:1.5rem; margin-bottom:1rem; color:var(--color-accent-strong);">Route B: Deep OEM Tooling</h3>
        <p style="color:var(--color-fg-muted); margin-bottom:1.5rem;">Proprietary brand ownership. Custom structural development, airtight locking patents, and dedicated moulds.</p>
        <ul style="list-style:none; display:flex; flex-direction:column; gap:0.5rem; font-size:0.9375rem;">
          <li>✓ Industrial 3D CAD Modeling & Mold-Flow Analysis</li>
          <li>✓ 72-Hour Functional SLA 3D Printed Verification Samples</li>
          <li>✓ Precision CNC Mould Machining (25-30 days)</li>
          <li>✓ Exclusive Production & Tooling Custody Agreement</li>
        </ul>
      </div>
    </div>

    <!-- RFQ Form Closer -->
    <div class="rfq-box">
      <h2 class="section-title">Initiate Your Custom Sourcing Brief</h2>
      <p style="color:var(--color-fg-muted); margin-bottom:2rem;">Share your product sketch or CAD file with our engineering team.</p>
      <form class="rfq-form rfq-form-submit">
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;" class="sm:grid-cols-2">
          <div class="form-group">
            <label class="form-label">Contact Name *</label>
            <input type="text" class="form-control" name="name" required>
          </div>
          <div class="form-group">
            <label class="form-label">Work Email *</label>
            <input type="email" class="form-control" name="email" required>
          </div>
        </div>
        <div class="form-group" style="margin-top:1rem;">
          <label class="form-label">Project Scope</label>
          <textarea class="form-control" rows="4" placeholder="Detail your project: dimensions, materials, expected order quantities, target release date..."></textarea>
        </div>
        <button type="submit" class="btn btn-primary" style="margin-top:1.5rem; padding:0.75rem 2rem;">Send Sourcing Brief →</button>
      </form>
    </div>
  </div>

  {get_footer()}
</body>
</html>"""
    with open(os.path.join(BASE_DIR, 'custom-solutions.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("custom-solutions.html successfully created.")

# 5. GENERATE ABOUT.HTML
def generate_about():
    print("Generating about.html...")
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Xinghui | Food Storage Container Manufacturer in China</title>
  <meta name="description" content="Learn about Xinghui Plastic Life, a food storage container manufacturer in Jieyang, Guangdong, China with 45 injection machines and certified ISO/FDA/LFGB facilities.">
  <link rel="canonical" href="https://www.xhplasticlife.com/about.html">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  {get_header(active_nav='about')}

  <div class="surface-tint section-padding">
    <div class="page-container">
      <span class="eyebrow">Factory Profile</span>
      <h1 class="section-title">A Food Storage Container Manufacturer in China</h1>
      <p class="section-lead">
        Established in 2008 in Jieyang, Guangdong, Xinghui specializes in the design, tooling, injection moulding, and global distribution of daily household plasticware and food contact containers.
      </p>
    </div>
  </div>

  <div class="page-container section-padding">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:center;" class="sm:grid-cols-2">
      <div>
        <h2 class="section-title" style="font-size:2rem;">Product-Led B2B Manufacturing</h2>
        <p style="color:var(--color-fg-muted); line-height:1.7; margin-bottom:1.5rem;">
          Our facility integrates product design, precision tooling, robotic injection moulding, and automated assembly under one quality management roof. By maintaining strict control over virgin polymer procurement and additive formulations, we ensure every batch meets FDA and German LFGB compliance.
        </p>
        <p style="color:var(--color-fg-muted); line-height:1.7;">
          We serve supermarket buyers, kitchenware importers, and e-commerce brands across 60+ countries, offering FBA packaging prep, drop-shipping container consolidation, and factory-direct pricing.
        </p>
      </div>
      <div>
        <img src="https://xinghui-plastic-life-cdn.assetlayer.site/Food-Storage-Containers-Manufacturer-Xinghui-Factory.webp" alt="Xinghui Factory Floor" style="border-radius:var(--radius-md); box-shadow:var(--shadow-md);">
      </div>
    </div>

    <!-- Factory Metrics -->
    <div class="stats-banner" style="margin-top:4rem;">
      <div class="stat-box">
        <div class="stat-number">12,000 m²</div>
        <div class="stat-label">Modern Plant Area</div>
      </div>
      <div class="stat-box">
        <div class="stat-number">45</div>
        <div class="stat-label">Injection Moulding Presses</div>
      </div>
      <div class="stat-box">
        <div class="stat-number">1,500,000</div>
        <div class="stat-label">Monthly Container Output</div>
      </div>
      <div class="stat-box">
        <div class="stat-number">ISO 9001</div>
        <div class="stat-label">Certified Management</div>
      </div>
    </div>
  </div>

  {get_footer()}
</body>
</html>"""
    with open(os.path.join(BASE_DIR, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("about.html successfully created.")

# 6. GENERATE CONTACT.HTML
def generate_contact():
    print("Generating contact.html...")
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Xinghui | Request Quotation & Sourcing Discussion</title>
  <meta name="description" content="Contact Xinghui about wholesale food storage containers, custom product development or e-commerce sourcing. Direct factory inquiry desk in Jieyang, China.">
  <link rel="canonical" href="https://www.xhplasticlife.com/contact.html">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  {get_header(active_nav='contact')}

  <div class="surface-tint section-padding">
    <div class="page-container">
      <span class="eyebrow">Direct Factory Communication</span>
      <h1 class="section-title">Let’s Talk About Your Product or Project</h1>
      <p class="section-lead">
        Connect directly with our export engineering sales desk in Jieyang, Guangdong. We provide quotations, sample shipping, and mould feasibility assessments.
      </p>
    </div>
  </div>

  <div class="page-container section-padding">
    <div class="rfq-box-grid">
      <div>
        <h2 class="section-title" style="font-size:1.75rem;">Direct Export Desk</h2>
        <p style="color:var(--color-fg-muted); line-height:1.7; margin-bottom:2rem;">
          Whether you are evaluating a stock model from our 63-SKU catalog or proposing a custom private mold project, we provide quotes within 12 hours.
        </p>

        <div style="display:flex; flex-direction:column; gap:1.25rem;">
          <div>
            <strong>Factory Address:</strong><br>
            Rongcheng Industrial Zone, Jieyang City, Guangdong Province, China (Post Code: 515500)
          </div>
          <div>
            <strong>Direct Export Telephone & WhatsApp:</strong><br>
            <a href="tel:+8615766644288" style="color:var(--color-accent-strong); font-weight:700;">+86-15766644288</a>
          </div>
          <div>
            <strong>General & Sourcing Inquiry Email:</strong><br>
            <a href="mailto:xhplasticlife@xhplasticlife.com" style="color:var(--color-accent-strong); font-weight:700;">xhplasticlife@xhplasticlife.com</a>
          </div>
          <div>
            <strong>Export Ports:</strong><br>
            Shantou Port / Shenzhen Yantian / Guangzhou Nansha (FOB/CIF terms available)
          </div>
        </div>
      </div>

      <form class="rfq-form rfq-form-submit">
        <h3 style="font-family:var(--font-display); font-size:1.35rem; margin-bottom:1rem;">Send An Enquiry</h3>
        <div class="form-group">
          <label class="form-label">Full Name *</label>
          <input type="text" name="name" class="form-control" required placeholder="John Doe">
        </div>
        <div class="form-group">
          <label class="form-label">Business Email *</label>
          <input type="email" name="email" class="form-control" required placeholder="john@domain.com">
        </div>
        <div class="form-group">
          <label class="form-label">Company Name & Country *</label>
          <input type="text" name="company" class="form-control" required placeholder="Acme Imports / Germany">
        </div>
        <div class="form-group">
          <label class="form-label">Interested Products / SKUs</label>
          <input type="text" name="sku" class="form-control" placeholder="e.g. BX1051 1.3L Bento Box, Freezer Storage Containers">
        </div>
        <div class="form-group">
          <label class="form-label">Detailed Requirements</label>
          <textarea name="message" class="form-control" rows="4" placeholder="Tell us about order quantity, customization, sample request, or target test certifications..."></textarea>
        </div>
        <button type="submit" class="btn btn-primary" style="margin-top:1rem;">Submit Inquiry Request →</button>
      </form>
    </div>
  </div>

  {get_footer()}
</body>
</html>"""
    with open(os.path.join(BASE_DIR, 'contact.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("contact.html successfully created.")

# 7. GENERATE ROBOTS.TXT (2026 AI Crawler Friendly Specification)
def generate_robots():
    print("Generating robots.txt...")
    content = """# 2026 AI-Friendly Robots Configuration for Xinghui Plastic Life
# Permits Google, Bing, and AI Knowledge Citation Bots (Princeton KDD 2024 GEO standard)

User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/

# AI Search & Citation Bots (Explicitly Allowed for Generative Engine Optimization)
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

User-agent: Applebot-Extended
Allow: /

User-agent: Amazonbot
Allow: /

# XML Sitemaps
Sitemap: https://www.xhplasticlife.com/sitemap.xml
"""
    with open(os.path.join(BASE_DIR, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("robots.txt successfully created.")

# 8. GENERATE SITEMAP.XML (Multilingual Hreflang Matrix)
def generate_sitemap():
    print("Generating sitemap.xml...")
    languages = ['en', 'ja', 'ru', 'de', 'fr', 'es', 'ko']
    pages = [
        "",
        "products.html",
        "lunch-boxes.html",
        "custom-solutions.html",
        "about.html",
        "contact.html"
    ]

    urls_xml = ""
    for p in pages:
        loc = f"https://www.xhplasticlife.com/{p}" if p else "https://www.xhplasticlife.com"
        alternates = ""
        for lang in languages:
            href = f"https://www.xhplasticlife.com/{lang}/{p}" if lang != 'en' else loc
            alternates += f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}"/>\n'
        
        urls_xml += f"""  <url>
    <loc>{loc}</loc>
{alternates}    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>\n"""

    # Add all 63 SKUs
    for p in products:
        sku_loc = f"https://www.xhplasticlife.com/products.html?sku={html.escape(p['name'])}"
        urls_xml += f"""  <url>
    <loc>{sku_loc}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{urls_xml}</urlset>"""
    with open(os.path.join(BASE_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print("sitemap.xml successfully created.")

# 9. GENERATE LLMS.TXT & LLMS-FULL.TXT (GEO Knowledge Endpoints)
def generate_llms():
    print("Generating llms.txt & llms-full.txt...")
    llms_txt = """# Xinghui Plastic Life · Food Storage Containers Manufacturer

> China-based premier OEM/ODM manufacturer of food storage containers, bento lunch boxes, and household daily plasticware for global distributors, retail supermarket chains, and e-commerce brands.

## Core Truth & Identity
- **Manufacturer Entity**: Jieyang Xinghui Plasticware Co., Ltd. (Xinghui Plastic Life)
- **Production Facility**: Rongcheng Industrial Zone, Jieyang City, Guangdong Province, China
- **Factory Footprint**: 12,000 square meters
- **Machinery Capacity**: 45 automated injection moulding production lines
- **Monthly Output**: 1,500,000 units
- **Established**: 2008
- **Export Destinations**: 60+ countries across North America, EU, Japan, Australia, Southeast Asia
- **Certifications & Compliance**: ISO 9001:2015, BSCI Audited, FDA 21 CFR 177.1520 Compliant, LFGB German Food Grade Certified, 100% BPA-Free, Sedex SMETA, REACH & RoHS.

## Product Families (6 Families, 63 Listed SKUs)
1. **Lunch Boxes & Bento Containers** (14 SKUs): Multi-compartment leakproof boxes, microwave safe with silicone steam valves, PP + 304 stainless steel hybrid containers, ramen bowls.
2. **Food Storage Containers** (27 SKUs): Airtight pantry storage canisters, modular fridge organizer bins, snap-lock grain containers, glass lunch boxes with PP clip lids.
3. **Kitchen Storage Containers** (4 SKUs): Rotating spice carousels, leakproof oil dispensers with measurement scales, cereal dispensaries.
4. **Drinkware & Tumblers** (2 SKUs): BPA-free sports water bottles, insulated travel coffee tumblers.
5. **Home Storage Containers** (12 SKUs): Stackable clothing boxes, desktop drawer organizers, bathroom organizers.
6. **Portable Organizers** (4 SKUs): Compact travel pill cases with silicone gaskets, daily hardware and craft boxes.

## Commercial Terms & Lead Times
- **Sample Lead Time**: Physical samples dispatched within 3 business days.
- **Stock Mould MOQ**: 1,000 pieces per SKU (custom colors available from 3,000 pcs).
- **Custom Tooling Cycle**: 3D CAD design (48h) -> SLA 3D print sample (72h) -> Mould fabrication (25-30 days) -> Mass injection run (15 days).
- **FOB Ports**: Shantou, Shenzhen (Yantian/Shekou), Guangzhou (Nansha).

## Official Navigation Links
- [Catalogue & 63 SKUs](https://www.xhplasticlife.com/products.html): Complete searchable inventory.
- [Wholesale Lunch Boxes](https://www.xhplasticlife.com/lunch-boxes.html): Bento box manufacturer details.
- [OEM Custom Manufacturing](https://www.xhplasticlife.com/custom-solutions.html): Custom tooling workflow.
- [About Xinghui](https://www.xhplasticlife.com/about.html): Factory profile and ISO/BSCI documentation.
- [Contact & RFQ](https://www.xhplasticlife.com/contact.html): Direct export inquiry desk.
"""

    llms_full_txt = llms_txt + """
## Detailed 63-SKU Catalog Inventory
"""
    for idx, p in enumerate(products, 1):
        llms_full_txt += f"""
### SKU #{idx}: {p['name']}
- **Category**: {p.get('category', 'food-storage-containers')}
- **Materials**: Food Grade PP / Silicone / BPA-Free Polymer
- **MOQ**: 1,000 units
- **Customization**: Custom color, logo printing, retail sleeve, barcode labeling
- **Image Reference**: {p['img']}
"""

    with open(os.path.join(BASE_DIR, 'llms.txt'), 'w', encoding='utf-8') as f:
        f.write(llms_txt)
    with open(os.path.join(BASE_DIR, 'llms-full.txt'), 'w', encoding='utf-8') as f:
        f.write(llms_full_txt)
    print("llms.txt and llms-full.txt successfully created.")

if __name__ == '__main__':
    generate_index()
    generate_products()
    generate_lunch_boxes()
    generate_custom_solutions()
    generate_about()
    generate_contact()
    generate_robots()
    generate_sitemap()
    generate_llms()
    print("All site assets compiled successfully!")
