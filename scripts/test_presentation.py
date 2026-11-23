"""
Automated Browser Test and Screenshot Generation for Interactive Presentation.
Uses Playwright (Chromium) to verify slide navigation, responsive layouts, console integrity,
and captures visual evidence in reports/evidence/.
"""

import sys
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

def run_tests():
    project_root = Path(__file__).resolve().parent.parent
    html_path = project_root / "presentation" / "index.html"
    evidence_dir = project_root / "reports" / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)

    file_url = html_path.as_uri()
    print(f"Testing presentation at: {file_url}")

    console_errors = []
    page_errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # -------------------------------------------------------------
        # TEST 1: Desktop Viewport (1366 x 768)
        # -------------------------------------------------------------
        print("\n--- Running Desktop Tests (1366x768) ---")
        context = browser.new_context(viewport={"width": 1366, "height": 768})
        page = context.new_page()

        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: page_errors.append(str(err)))

        page.goto(file_url)
        page.wait_for_selector(".slide.active")

        # Check title
        title = page.title()
        print(f"Page Title: {title}")
        assert "AI Agents" in title, "Page title mismatch"

        # Check total slides count
        slides = page.query_selector_all(".slide")
        print(f"Total Slides Found: {len(slides)}")
        assert len(slides) == 12, f"Expected exactly 12 slides, found {len(slides)}"

        # Verify Slide 1 active
        counter_text = page.locator("#slide-counter").text_content()
        print(f"Initial Counter: {counter_text}")
        assert "Slide 1 of 12" in counter_text

        # Capture Slide 01
        s1_path = evidence_dir / "slide-01-desktop.png"
        page.screenshot(path=str(s1_path), full_page=False)
        print(f"Captured: {s1_path.name}")

        # Navigate forward to Slide 4 using Next button
        for _ in range(3):
            page.click("#next-btn")
            page.wait_for_timeout(200)

        counter_text = page.locator("#slide-counter").text_content()
        print(f"Counter at Slide 4: {counter_text}")
        assert "Slide 4 of 12" in counter_text
        s4_path = evidence_dir / "slide-04-architecture.png"
        page.screenshot(path=str(s4_path), full_page=False)
        print(f"Captured: {s4_path.name}")

        # Navigate to Slide 8 using Keyboard ArrowRight
        for _ in range(4):
            page.keyboard.press("ArrowRight")
            page.wait_for_timeout(200)

        counter_text = page.locator("#slide-counter").text_content()
        print(f"Counter at Slide 8: {counter_text}")
        assert "Slide 8 of 12" in counter_text
        s8_path = evidence_dir / "slide-08-react.png"
        page.screenshot(path=str(s8_path), full_page=False)
        print(f"Captured: {s8_path.name}")

        # Navigate to Slide 9 using Space
        page.keyboard.press("Space")
        page.wait_for_timeout(200)
        counter_text = page.locator("#slide-counter").text_content()
        print(f"Counter at Slide 9: {counter_text}")
        assert "Slide 9 of 12" in counter_text
        s9_path = evidence_dir / "slide-09-orchestration.png"
        page.screenshot(path=str(s9_path), full_page=False)
        print(f"Captured: {s9_path.name}")

        # Navigate to Slide 12 using PageDown
        for _ in range(3):
            page.keyboard.press("PageDown")
            page.wait_for_timeout(200)

        counter_text = page.locator("#slide-counter").text_content()
        print(f"Counter at Slide 12: {counter_text}")
        assert "Slide 12 of 12" in counter_text
        s12_path = evidence_dir / "slide-12-summary.png"
        page.screenshot(path=str(s12_path), full_page=False)
        print(f"Captured: {s12_path.name}")

        # Test Overview modal
        page.click("#overview-btn")
        page.wait_for_timeout(300)
        modal_open = page.locator("#overview-modal").is_visible()
        print(f"Overview modal visible: {modal_open}")
        assert modal_open, "Overview modal failed to open"

        # Click Slide 2 link in overview modal
        page.locator("#overview-grid .slide-link-item").nth(1).click()
        page.wait_for_timeout(300)
        counter_text = page.locator("#slide-counter").text_content()
        print(f"Jumped to via overview: {counter_text}")
        assert "Slide 2 of 12" in counter_text

        # Test Previous button
        page.click("#prev-btn")
        page.wait_for_timeout(200)
        counter_text = page.locator("#slide-counter").text_content()
        print(f"Back at Slide 1: {counter_text}")
        assert "Slide 1 of 12" in counter_text
        assert page.locator("#prev-btn").is_disabled(), "Prev button should be disabled on Slide 1"

        context.close()

        # -------------------------------------------------------------
        # TEST 2: Mobile Viewport (390 x 844 - iPhone 14 / modern mobile)
        # -------------------------------------------------------------
        print("\n--- Running Mobile Tests (390x844) ---")
        mobile_context = browser.new_context(
            viewport={"width": 390, "height": 844},
            is_mobile=True,
            has_touch=True
        )
        mobile_page = mobile_context.new_page()
        mobile_page.goto(file_url)
        mobile_page.wait_for_selector(".slide.active")

        mob_s1_path = evidence_dir / "slide-01-mobile.png"
        mobile_page.screenshot(path=str(mob_s1_path), full_page=False)
        print(f"Captured: {mob_s1_path.name}")

        # Test touch navigation via Next button
        mobile_page.click("#next-btn")
        mobile_page.wait_for_timeout(200)
        mob_counter = mobile_page.locator("#slide-counter").text_content()
        print(f"Mobile after next click: {mob_counter}")
        assert "Slide 2 of 12" in mob_counter

        mobile_context.close()
        browser.close()

    print("\n--- Test Integrity Verification ---")
    print(f"Console Errors: {len(console_errors)}")
    for ce in console_errors:
        print(f"  [ERROR] {ce}")
    print(f"Page Exceptions: {len(page_errors)}")
    for pe in page_errors:
        print(f"  [PAGE ERROR] {pe}")

    assert len(console_errors) == 0, f"Found {len(console_errors)} console errors!"
    assert len(page_errors) == 0, f"Found {len(page_errors)} uncaught page exceptions!"

    print("\n[SUCCESS] All presentation browser tests passed with 0 errors!")
    return True

if __name__ == "__main__":
    success = run_tests()
    if not success:
        sys.exit(1)
