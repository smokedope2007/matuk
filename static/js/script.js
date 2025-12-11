document.addEventListener('DOMContentLoaded', function() {
  AOS.init();

  const searchInput = document.getElementById('searchInput');
  const filterTags = document.querySelectorAll('.filter-tag');
  const sortSelect = document.getElementById('sortSelect');
  const cardsContainer = document.getElementById('destinationsContainer');
  const cards = document.querySelectorAll('.destination-card');

  let currentFilter = 'all';
  let currentSort = 'popularity';

  function updateDisplay() {
    const query = searchInput.value.toLowerCase().trim();

    let filtered = Array.from(cards).filter(card => {
      const name = card.dataset.name.toLowerCase();
      const desc = card.dataset.description.toLowerCase();
      const tags = card.dataset.tags.split(' ');

      const matchesSearch = query === '' || 
        name.includes(query) || 
        desc.includes(query) ||
        tags.some(tag => tag.includes(query));

      const matchesTag = currentFilter === 'all' || tags.includes(currentFilter);

      return matchesSearch && matchesTag;
    });


    filtered.sort((a, b) => {
      const aPop = parseFloat(a.dataset.popularity);
      const bPop = parseFloat(b.dataset.popularity);
      const aPrice = parseFloat(a.dataset.price);
      const bPrice = parseFloat(b.dataset.price);
      const aDur = parseFloat(a.dataset.duration);
      const bDur = parseFloat(b.dataset.duration);

      switch (currentSort) {
        case 'popularity': return bPop - aPop;
        case 'price-asc': return aPrice - bPrice;
        case 'price-desc': return bPrice - aPrice;
        case 'duration': return aDur - bDur;
        default: return 0;
      }
    });


    cardsContainer.innerHTML = '';
    filtered.forEach(card => cardsContainer.appendChild(card));
  }


  searchInput.addEventListener('input', updateDisplay);

  filterTags.forEach(tag => {
    tag.addEventListener('click', () => {
      filterTags.forEach(t => t.classList.remove('active'));
      tag.classList.add('active');
      currentFilter = tag.dataset.tag;
      updateDisplay();
    });
  });

  sortSelect.addEventListener('change', () => {
    currentSort = sortSelect.value;
    updateDisplay();
  });


  updateDisplay();

  let currentSlide = 0;
  const slides = document.querySelectorAll('.slide');
  const dotsContainer = document.getElementById('slideDots');

  function updateSlider() {
    slides.forEach((slide, index) => {
      slide.classList.toggle('active', index === currentSlide);
    });

    dotsContainer.innerHTML = '';
    slides.forEach((_, index) => {
      const dot = document.createElement('div');
      dot.classList.add('dot');
      if (index === currentSlide) dot.classList.add('active');
      dot.onclick = () => goToSlide(index);
      dotsContainer.appendChild(dot);
    });
  }

  function goToSlide(index) {
    currentSlide = index;
    updateSlider();
  }

  window.changeSlide = function(direction) {
    currentSlide = (currentSlide + direction + slides.length) % slides.length;
    updateSlider();
  };

  if (slides.length > 0) {
    updateSlider();
  }
});