/**
 * AI Systems Atlas — Interactive Presentation Controller
 * Powered by GSAP 3.15.1 Core & Timelines
 * Features: Bespoke per-slide motion choreography, reduced-motion compliance,
 *           keyboard navigation, touch gestures, and interactive directory modal.
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
  const closeModalFooterBtn = document.getElementById("close-modal-footer-btn");
  const overviewGrid = document.getElementById("overview-grid");
  const headerEl = document.querySelector("header");
  const footerEl = document.querySelector("footer");

  // Motion Detection
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Animate slide entrance on demand with slide-specific choreography
  function animateSlideIn(slideEl, slideNum) {
    if (!window.gsap || prefersReducedMotion) return;

    // Clear any lingering tweens on this slide
    gsap.killTweensOf(slideEl.querySelectorAll("*"));

    const tl = gsap.timeline({ defaults: { ease: "power2.out" } });

    // Global editorial header reveal (if present)
    const header = slideEl.querySelector(".editorial-header");
    if (header) {
      tl.fromTo(header, { y: 12, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.28 }, 0);
    }

    // Slide-specific choreographies
    switch (slideNum) {
      case 1: { // Hero Split
        const heroLeft = slideEl.querySelector(".hero-left");
        if (heroLeft) {
          tl.fromTo(heroLeft.children,
            { y: 15, autoAlpha: 0 },
            { y: 0, autoAlpha: 1, stagger: 0.05, duration: 0.32 },
            0.04
          );
        }
        const hub = slideEl.querySelector(".hero-svg-hub");
        if (hub) {
          tl.fromTo(hub, { scale: 0.94, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.4, ease: "back.out(1.2)" }, 0.08);
          const nodes = hub.querySelectorAll(".hub-node");
          if (nodes.length > 0) {
            tl.fromTo(nodes, { scale: 0.85, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, stagger: 0.04, duration: 0.25 }, 0.15);
          }
        }
        break;
      }

      case 2: { // Journey & Executive Chef
        const theorem = slideEl.querySelector(".agency-theorem-bar");
        if (theorem) {
          tl.fromTo(theorem, { y: 10, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.26 }, 0.05);
        }
        const columns = slideEl.querySelectorAll(".analogy-column");
        if (columns.length > 0) {
          tl.fromTo(columns, { y: 12, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.06, duration: 0.3 }, 0.08);
        }
        const stages = slideEl.querySelectorAll(".stage-step-unit");
        if (stages.length > 0) {
          tl.fromTo(stages, { y: 10, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.05, duration: 0.26 }, 0.14);
        }
        break;
      }

      case 3: { // Split-Contrast
        const leftSide = slideEl.querySelector(".side-chatbot");
        const rightSide = slideEl.querySelector(".side-agent");
        if (leftSide) {
          tl.fromTo(leftSide, { x: -15, autoAlpha: 0 }, { x: 0, autoAlpha: 1, duration: 0.32 }, 0);
        }
        if (rightSide) {
          tl.fromTo(rightSide, { x: 15, autoAlpha: 0 }, { x: 0, autoAlpha: 1, duration: 0.32 }, 0.04);
        }
        const rows = slideEl.querySelectorAll(".split-row-item");
        if (rows.length > 0) {
          tl.fromTo(rows, { y: 8, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.025, duration: 0.22 }, 0.08);
        }
        const banner = slideEl.querySelector(".split-footer-banner");
        if (banner) {
          tl.fromTo(banner, { y: 10, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.25 }, 0.18);
        }
        break;
      }

      case 4: { // Architecture Canvas
        const svgMap = slideEl.querySelector(".arch-svg-map");
        if (svgMap) {
          tl.fromTo(svgMap, { scale: 0.96, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.35 }, 0.04);
        }
        const annotations = slideEl.querySelectorAll(".annotation-item");
        if (annotations.length > 0) {
          tl.fromTo(annotations, { y: 10, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.05, duration: 0.26 }, 0.12);
        }
        break;
      }

      case 5: { // Timeline
        const steps = slideEl.querySelectorAll(".timeline-step-column");
        if (steps.length > 0) {
          tl.fromTo(steps, { y: 14, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.06, duration: 0.3 }, 0.06);
        }
        const scaleBar = slideEl.querySelector(".tradeoff-scale-bar");
        if (scaleBar) {
          tl.fromTo(scaleBar, { y: 10, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.25 }, 0.16);
        }
        break;
      }

      case 6: { // Strata
        const levels = slideEl.querySelectorAll(".stratum-level");
        if (levels.length > 0) {
          tl.fromTo(levels, { y: 12, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.06, duration: 0.28 }, 0.06);
        }
        const strip = slideEl.querySelector(".pipeline-consolidation-strip");
        if (strip) {
          tl.fromTo(strip, { y: 10, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.25 }, 0.16);
        }
        break;
      }

      case 7: { // Workspace
        const workSteps = slideEl.querySelectorAll(".workspace-step");
        if (workSteps.length > 0) {
          tl.fromTo(workSteps, { x: -10, autoAlpha: 0 }, { x: 0, autoAlpha: 1, stagger: 0.04, duration: 0.25 }, 0.05);
        }
        const ide = slideEl.querySelector(".workspace-right-ide");
        if (ide) {
          tl.fromTo(ide, { y: 12, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.3 }, 0.08);
        }
        break;
      }

      case 8: { // ReAct Orbital
        const orbital = slideEl.querySelector(".react-left-orbital");
        if (orbital) {
          tl.fromTo(orbital, { scale: 0.95, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.3 }, 0.04);
        }
        const traceLines = slideEl.querySelectorAll(".trace-line-unit");
        if (traceLines.length > 0) {
          tl.fromTo(traceLines, { x: 10, autoAlpha: 0 }, { x: 0, autoAlpha: 1, stagger: 0.035, duration: 0.22 }, 0.08);
        }
        break;
      }

      case 9: { // Topology Trio
        const zones = slideEl.querySelectorAll(".topology-zone");
        if (zones.length > 0) {
          tl.fromTo(zones, { y: 12, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.05, duration: 0.28 }, 0.05);
        }
        const recon = slideEl.querySelector(".reconciliation-full-banner");
        if (recon) {
          tl.fromTo(recon, { y: 10, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.25 }, 0.15);
        }
        break;
      }

      case 10: { // Multi-Agent Network
        const contrast = slideEl.querySelector(".network-contrast-strip");
        if (contrast) {
          tl.fromTo(contrast, { y: 10, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.26 }, 0.04);
        }
        const cards = slideEl.querySelectorAll(".topology-card-open");
        if (cards.length > 0) {
          tl.fromTo(cards, { y: 12, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.05, duration: 0.28 }, 0.1);
        }
        break;
      }

      case 11: { // Frameworks Matrix
        const table = slideEl.querySelector(".open-matrix-table");
        if (table) {
          tl.fromTo(table, { y: 10, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 0.28 }, 0.04);
        }
        const terminals = slideEl.querySelectorAll(".terminal-box");
        if (terminals.length > 0) {
          tl.fromTo(terminals, { y: 12, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.06, duration: 0.28 }, 0.1);
        }
        break;
      }

      case 12: { // Conclusion Canvas
        const cols = slideEl.querySelectorAll(".concl-column");
        if (cols.length > 0) {
          tl.fromTo(cols, { y: 12, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.06, duration: 0.28 }, 0.04);
        }
        const takeaways = slideEl.querySelectorAll(".takeaway-unit");
        if (takeaways.length > 0) {
          tl.fromTo(takeaways, { y: 10, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.05, duration: 0.26 }, 0.12);
        }
        break;
      }
    }

    // Editorial Citations Strip fade-in
    const citations = slideEl.querySelector(".editorial-citations");
    if (citations) {
      tl.fromTo(citations, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.25 }, 0.2);
    }
  }

  // Reset outgoing slide
  function resetSlide(slideEl) {
    if (!window.gsap) return;
    gsap.killTweensOf(slideEl.querySelectorAll("*"));
    gsap.set(slideEl.querySelectorAll("*"), { clearProps: "all" });
  }

  // Populate Atlas Index / Overview Modal Links
  if (overviewGrid) {
    overviewGrid.innerHTML = "";
    slides.forEach((slide, idx) => {
      const slideNum = idx + 1;
      const titleEl = slide.querySelector(".editorial-title, .hero-main-title, h1, h2");
      let titleText = `Slide ${slideNum}`;
      if (titleEl) {
        titleText = titleEl.textContent.replace(/\s+/g, " ").trim();
        if (titleText.length > 40) {
          titleText = titleText.substring(0, 37) + "...";
        }
      }

      const item = document.createElement("div");
      item.className = `slide-link-item ${slideNum === 1 ? "active" : ""}`;
      item.dataset.slideNum = slideNum;
      item.innerHTML = `<strong>ATLAS #${slideNum.toString().padStart(2, "0")}</strong><span>${titleText}</span>`;
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
      const slideNum = idx + 1;
      if (slideNum === newIndex) {
        slide.classList.add("active");
        slide.scrollTop = 0;
        animateSlideIn(slide, slideNum);
      } else {
        if (slide.classList.contains("active")) {
          resetSlide(slide);
        }
        slide.classList.remove("active");
      }
    });

    currentSlide = newIndex;

    // Adapt Header and Footer theme for dark slides (1, 4, 8, 12)
    const activeSlide = slides[currentSlide - 1];
    const isDark = activeSlide && (activeSlide.classList.contains("slide-dark") || activeSlide.classList.contains("slide-deep"));
    if (headerEl) {
      headerEl.classList.toggle("theme-dark", isDark);
      headerEl.style.removeProperty("background");
      headerEl.style.removeProperty("border-color");
    }
    if (footerEl) {
      footerEl.classList.toggle("theme-dark", isDark);
      footerEl.style.removeProperty("background");
      footerEl.style.removeProperty("border-color");
    }

    // Update Counter
    if (slideCounter) {
      slideCounter.textContent = `Slide ${currentSlide} of ${totalSlides}`;
    }

    // Update Progress Bar
    if (progressBar) {
      const pct = (currentSlide / totalSlides) * 100;
      progressBar.style.width = `${pct}%`;
    }

    // Update Navigation Controls
    if (prevBtn) {
      prevBtn.disabled = currentSlide === 1;
    }

    if (nextBtn) {
      if (currentSlide === totalSlides) {
        nextBtn.innerHTML = "Restart &#x21bb;";
        nextBtn.disabled = false;
      } else {
        nextBtn.innerHTML = "Next &rarr;";
        nextBtn.disabled = false;
      }
    }

    // Highlight active item in overview grid
    if (overviewGrid) {
      const items = overviewGrid.querySelectorAll(".slide-link-item");
      items.forEach((item) => {
        if (parseInt(item.dataset.slideNum, 10) === currentSlide) {
          item.classList.add("active");
        } else {
          item.classList.remove("active");
        }
      });
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

  // Touch Swipe Navigation for Mobile
  let touchStartX = 0;
  let touchStartY = 0;

  document.addEventListener("touchstart", (e) => {
    touchStartX = e.changedTouches[0].screenX;
    touchStartY = e.changedTouches[0].screenY;
  }, { passive: true });

  document.addEventListener("touchend", (e) => {
    const diffX = e.changedTouches[0].screenX - touchStartX;
    const diffY = e.changedTouches[0].screenY - touchStartY;

    // Horizontal swipe threshold: 45px, vertical max tolerance: 80px
    if (Math.abs(diffX) > 45 && Math.abs(diffY) < 80) {
      if (diffX < 0) {
        nextSlide();
      } else {
        prevSlide();
      }
    }
  }, { passive: true });

  // Initial trigger
  updateSlide(1);
});
