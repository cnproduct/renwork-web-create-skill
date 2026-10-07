/**
 * Sourcing & Container Load Estimator
 * Integrated from cnproduct/b2b-global-brand-site-master
 * Calculates 20GP / 40HQ container utilization for B2B export buyers.
 */

export function initContainerEstimator() {
  const container = document.getElementById('containerEstimatorSection');
  if (!container) return;

  const qtyInput = document.getElementById('calcQuantity');
  const typeSelect = document.getElementById('calcContainerType');
  const fillBar = document.getElementById('calcFillBar');
  const fillPercentText = document.getElementById('calcFillPercent');
  const totalCbmText = document.getElementById('calcTotalCbm');
  const totalWeightText = document.getElementById('calcTotalWeight');
  const totalCartonsText = document.getElementById('calcTotalCartons');
  const suggestionText = document.getElementById('calcSuggestion');

  // Industry standards for food containers (BX1051 standard carton: 48 pcs, 0.172 m3, 14.3 kg)
  const PCS_PER_CARTON = 48;
  const CARTON_CBM = 0.172; // m3
  const CARTON_KG = 14.3;   // kg

  const CONTAINER_PRESETS = {
    '20GP': { volume: 28.5, maxWeight: 21500, label: '20ft General Purpose (20GP)' },
    '40HQ': { volume: 68.0, maxWeight: 26000, label: '40ft High Cube (40HQ)' }
  };

  function updateCalculation() {
    const qty = parseInt(qtyInput.value, 10) || 0;
    const containerType = typeSelect.value || '20GP';
    const preset = CONTAINER_PRESETS[containerType];

    const cartons = Math.ceil(qty / PCS_PER_CARTON);
    const totalVolume = cartons * CARTON_CBM;
    const totalWeight = cartons * CARTON_KG;

    const volumeRatio = (totalVolume / preset.volume) * 100;
    const weightRatio = (totalWeight / preset.maxWeight) * 100;
    const maxRatio = Math.max(volumeRatio, weightRatio);
    const containersNeeded = Math.ceil(maxRatio / 100);

    // Update UI
    if (totalCartonsText) totalCartonsText.textContent = cartons.toLocaleString();
    if (totalCbmText) totalCbmText.textContent = totalVolume.toFixed(2) + ' m³';
    if (totalWeightText) totalWeightText.textContent = totalWeight.toLocaleString() + ' kg';

    const displayPercent = Math.min(Math.round(maxRatio), 100);
    if (fillBar) fillBar.style.width = displayPercent + '%';
    if (fillPercentText) fillPercentText.textContent = Math.round(maxRatio) + '%';

    if (suggestionText) {
      if (maxRatio < 30) {
        suggestionText.innerHTML = `⚠️ <strong>LCL Consolidation:</strong> Volume is under 30%. Consider ordering at least ${(Math.round((preset.volume * 0.85) / CARTON_CBM) * PCS_PER_CARTON).toLocaleString()} pcs to fill an FCL container for optimal freight savings.`;
        suggestionText.style.color = '#856404';
      } else if (maxRatio <= 100) {
        suggestionText.innerHTML = `✓ <strong>Optimal FCL Batch:</strong> Fits neatly into <strong>1 × ${containerType}</strong> (${Math.round(maxRatio)}% space utilized).`;
        suggestionText.style.color = '#2d6a4f';
      } else {
        suggestionText.innerHTML = `🚢 <strong>Multi-Container Batch:</strong> Requires <strong>${containersNeeded} × ${containerType}</strong> containers.`;
        suggestionText.style.color = '#516b4b';
      }
    }
  }

  if (qtyInput) qtyInput.addEventListener('input', updateCalculation);
  if (typeSelect) typeSelect.addEventListener('change', updateCalculation);
  updateCalculation();
}

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initContainerEstimator);
  } else {
    initContainerEstimator();
  }
}
