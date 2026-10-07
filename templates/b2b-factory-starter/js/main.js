/**
 * Xinghui Plastic Life · High-Fidelity Interactive Script
 * Handles: Live 63-SKU Filter, Mobile Drawer, Multilingual Selector, FAQ Accordion, RFQ Handling
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Drawer
  const mobileToggle = document.getElementById('mobileToggle');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const closeDrawer = document.getElementById('closeDrawer');

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      mobileDrawer.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  }

  if (closeDrawer && mobileDrawer) {
    closeDrawer.addEventListener('click', () => {
      mobileDrawer.classList.remove('open');
      document.body.style.overflow = '';
    });
  }

  // 2. Multilingual Switcher
  const langSelector = document.getElementById('langSelector');
  if (langSelector) {
    const langItems = langSelector.querySelectorAll('.lang-menu a');
    langItems.forEach(item => {
      item.addEventListener('click', (e) => {
        const lang = item.getAttribute('data-lang');
        const langLabel = item.textContent.trim();
        const currentBtn = langSelector.querySelector('.lang-btn span');
        if (currentBtn) currentBtn.textContent = langLabel;
        console.log(`[GEO Routing] Switched target locale to: ${lang}`);
      });
    });
  }

  // 3. Live 63-SKU Catalogue Engine
  const searchInput = document.getElementById('catalogueSearch');
  const categoryButtons = document.querySelectorAll('.cat-btn');
  const productGrid = document.getElementById('productGrid');
  const resultsCount = document.getElementById('resultsCount');

  let currentCategory = 'all';
  let searchQuery = '';

  function filterProducts() {
    if (!productGrid) return;
    const cards = productGrid.querySelectorAll('.catalogue-product-card');
    let visibleCount = 0;

    cards.forEach(card => {
      const cardCategory = card.getAttribute('data-category');
      const cardTitle = (card.getAttribute('data-title') || '').toLowerCase();
      const matchesCategory = (currentCategory === 'all' || cardCategory === currentCategory);
      const matchesSearch = (!searchQuery || cardTitle.includes(searchQuery));

      if (matchesCategory && matchesSearch) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (resultsCount) {
      resultsCount.textContent = visibleCount;
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim().toLowerCase();
      filterProducts();
    });
  }

  if (categoryButtons.length > 0) {
    categoryButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        categoryButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentCategory = btn.getAttribute('data-cat') || 'all';
        filterProducts();
      });
    });
  }

  // 4. Interactive FAQ Accordion Mutual Exclusion
  const faqDetails = document.querySelectorAll('.faq-item');
  faqDetails.forEach(targetDetail => {
    targetDetail.addEventListener('toggle', () => {
      if (targetDetail.open) {
        faqDetails.forEach(detail => {
          if (detail !== targetDetail) {
            detail.removeAttribute('open');
          }
        });
      }
    });
  });

  // 5. B2B RFQ Form Handler
  const rfqForms = document.querySelectorAll('.rfq-form-submit');
  rfqForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.textContent : 'Submit';
      
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Processing Quotation...';
      }

      // Collect data
      const formData = new FormData(form);
      const payload = Object.fromEntries(formData.entries());
      console.log('[B2B RFQ Submitted]', payload);

      setTimeout(() => {
        if (submitBtn) {
          submitBtn.textContent = '✓ Quote Request Sent';
          submitBtn.style.backgroundColor = '#2d6a4f';
        }
        alert('Thank you for your enquiry! Our factory export sales manager will reach out with a detailed quotation within 12 hours.');
        form.reset();
        setTimeout(() => {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
            submitBtn.style.backgroundColor = '';
          }
        }, 4000);
      }, 1000);
    });
  });
});
