/**
 * AI Agents Learning Wiki - Interactive Presentation Controller
 * Manages slide transitions, keyboard shortcuts, progress tracking, and touch navigation.
 */

document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".slide");
  const totalSlides = slides.length;
  let currentSlide = 1;

  // DOM Elements
  const progressBar = document.getElementById("progress-bar");
  const slideCounter = document.getElementById("slide-counter");
  const prevBtn = document.getElementById("prev-btn");
  const nextBtn = document.getElementById("next-btn");
  const overviewBtn = document.getElementById("overview-btn");
  const overviewModal = document.getElementById("overview-modal");
  const closeModalBtn = document.getElementById("close-modal-btn");
  const overviewGrid = document.getElementById("overview-grid");

  // Populate overview modal links
  if (overviewGrid) {
    slides.forEach((slide, idx) => {
      const slideNum = idx + 1;
      const titleEl = slide.querySelector(".slide-title");
      const titleText = titleEl ? titleEl.textContent : `Slide ${slideNum}`;

      const item = document.createElement("div");
      item.className = "slide-link-item";
      item.innerHTML = `<strong>#${slideNum}</strong>: ${titleText}`;
      item.addEventListener("click", () => {
        goToSlide(slideNum);
        closeModal();
      });
      overviewGrid.appendChild(item);
    });
  }

  function updateSlide(newIndex) {
    if (newIndex < 1) newIndex = 1;
    if (newIndex > totalSlides) newIndex = totalSlides;

    slides.forEach((slide, idx) => {
      if (idx + 1 === newIndex) {
        slide.classList.add("active");
        slide.scrollTop = 0;
      } else {
        slide.classList.remove("active");
      }
    });

    currentSlide = newIndex;

    // Update Counter
    if (slideCounter) {
      slideCounter.textContent = `Slide ${currentSlide} of ${totalSlides}`;
    }

    // Update Progress Bar
    if (progressBar) {
      const pct = (currentSlide / totalSlides) * 100;
      progressBar.style.width = `${pct}%`;
    }

    // Update Prev Button
    if (prevBtn) {
      prevBtn.disabled = currentSlide === 1;
    }

    // Update Next Button
    if (nextBtn) {
      if (currentSlide === totalSlides) {
        nextBtn.innerHTML = "Restart &#x21bb;";
        nextBtn.disabled = false;
      } else {
        nextBtn.innerHTML = "Next &rarr;";
        nextBtn.disabled = false;
      }
    }
  }

  function nextSlide() {
    if (currentSlide === totalSlides) {
      updateSlide(1);
    } else {
      updateSlide(currentSlide + 1);
    }
  }

  function prevSlide() {
    if (currentSlide > 1) {
      updateSlide(currentSlide - 1);
    }
  }

  function goToSlide(n) {
    updateSlide(n);
  }

  function openModal() {
    if (overviewModal) overviewModal.classList.add("open");
  }

  function closeModal() {
    if (overviewModal) overviewModal.classList.remove("open");
  }

  // Event Listeners
  if (prevBtn) prevBtn.addEventListener("click", prevSlide);
  if (nextBtn) nextBtn.addEventListener("click", nextSlide);
  if (overviewBtn) overviewBtn.addEventListener("click", openModal);
  if (closeModalBtn) closeModalBtn.addEventListener("click", closeModal);
  const closeModalFooterBtn = document.getElementById("close-modal-footer-btn");
  if (closeModalFooterBtn) closeModalFooterBtn.addEventListener("click", closeModal);

  if (overviewModal) {
    overviewModal.addEventListener("click", (e) => {
      if (e.target === overviewModal) closeModal();
    });
  }

  // Keyboard Navigation
  document.addEventListener("keydown", (e) => {
    // If modal is open, Escape closes it
    if (overviewModal && overviewModal.classList.contains("open")) {
      if (e.key === "Escape") {
        closeModal();
      }
      return;
    }

    if (e.key === "ArrowRight" || e.key === " " || e.key === "PageDown") {
      e.preventDefault();
      nextSlide();
    } else if (e.key === "ArrowLeft" || e.key === "PageUp") {
      e.preventDefault();
      prevSlide();
    } else if (e.key === "Home") {
      e.preventDefault();
      goToSlide(1);
    } else if (e.key === "End") {
      e.preventDefault();
      goToSlide(totalSlides);
    } else if (e.key.toLowerCase() === "o") {
      e.preventDefault();
      openModal();
    }
  });

  // Touch Swipe for Mobile
  let touchStartX = 0;
  let touchEndX = 0;

  document.addEventListener("touchstart", (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  document.addEventListener("touchend", (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  }, { passive: true });

  function handleSwipe() {
    const diff = touchEndX - touchStartX;
    if (Math.abs(diff) > 50) {
      if (diff < 0) {
        nextSlide(); // Swiped left -> next
      } else {
        prevSlide(); // Swiped right -> prev
      }
    }
  }

  // Initialize
  updateSlide(1);
});
