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

  // Historical demo has no receiving service. Preserve input and report the actual state.
  document.querySelectorAll('.rfq-form-submit').forEach(form => {
    form.addEventListener('submit', event => {
      event.preventDefault();
      alert('Demonstration only: no inquiry was sent. Connect and verify a receiving service before release.');
    });
  });
});
