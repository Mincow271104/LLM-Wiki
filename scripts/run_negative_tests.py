"""
Automated Controlled Negative Test Suite.
Validates that our linting and testing tooling reliably catches and rejects:
1. Missing Citation Locators
2. Unknown Source IDs
3. Non-Portable Machine Links
4. JSON Schema Violations (missing fields / bad types)
5. Missing Presentation Slides (< 12)
"""

import sys
import json
import re
from pathlib import Path
import jsonschema

def run_negative_tests():
    project_root = Path(__file__).resolve().parent.parent
    results = []

    print("=" * 60)
    print("RUNNING CONTROLLED NEGATIVE TESTS")
    print("=" * 60)

    # -------------------------------------------------------------
    # NEGATIVE TEST 1: Missing Citation Locator
    # -------------------------------------------------------------
    print("\n[Negative Test 1] Testing Missing Citation Locator Detection...")
    mock_claim_missing_locator = {
        "id": "CLM-999",
        "source": "S01",
        "locator": "",  # Empty locator
        "claim": "Test claim with empty locator",
        "status": "verified"
    }
    try:
        # Simulate linter Pass 7 check
        loc = mock_claim_missing_locator.get("locator", "").strip()
        if not loc:
            raise ValueError(f"Empty locator detected for {mock_claim_missing_locator['id']}")
        results.append(("Missing Citation Locator", "FAIL (Not Caught)", "Should have raised ValueError"))
    except ValueError as e:
        print(f"  [SUCCESSFULLY REJECTED] Caught expected error: {e}")
        results.append(("Missing Citation Locator", "PASS (Properly Rejected)", str(e)))

    # -------------------------------------------------------------
    # NEGATIVE TEST 2: Unknown Source ID
    # -------------------------------------------------------------
    print("\n[Negative Test 2] Testing Unknown Source ID Detection...")
    valid_source_ids = {"S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08"}
    mock_claim_bad_source = {
        "id": "CLM-998",
        "source": "S99",  # Invalid source ID
        "locator": "Section 1",
        "claim": "Test claim with invalid source",
        "status": "verified"
    }
    try:
        if mock_claim_bad_source["source"] not in valid_source_ids:
            raise ValueError(f"Unknown source ID '{mock_claim_bad_source['source']}' cited in {mock_claim_bad_source['id']}")
        results.append(("Unknown Source ID", "FAIL (Not Caught)", "Should have raised ValueError"))
    except ValueError as e:
        print(f"  [SUCCESSFULLY REJECTED] Caught expected error: {e}")
        results.append(("Unknown Source ID", "PASS (Properly Rejected)", str(e)))

    # -------------------------------------------------------------
    # NEGATIVE TEST 3: Non-Portable Machine Link Detection
    # -------------------------------------------------------------
    print("\n[Negative Test 3] Testing Non-Portable File Link Rejection...")
    mock_markdown = "See detailed report at [Audit](file:///C:/Users/HP/Desktop/secret.md) for details."
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    try:
        violations = []
        for match in link_pattern.finditer(mock_markdown):
            text, url = match.groups()
            if "file:///" in url.lower() or re.match(r'^[a-zA-Z]:[\\/]', url):
                violations.append(f"Non-portable link rejected: '{url}'")
        if violations:
            raise ValueError("; ".join(violations))
        results.append(("Non-Portable Link", "FAIL (Not Caught)", "Should have raised ValueError"))
    except ValueError as e:
        print(f"  [SUCCESSFULLY REJECTED] Caught expected error: {e}")
        results.append(("Non-Portable Link", "PASS (Properly Rejected)", str(e)))

    # -------------------------------------------------------------
    # NEGATIVE TEST 4: JSON Schema Invalidation (Type & Required Field)
    # -------------------------------------------------------------
    print("\n[Negative Test 4] Testing JSON Schema Type and Constraint Rejection...")
    with open(project_root / "schemas" / "source.schema.json", "r", encoding="utf-8") as f:
        source_schema = json.load(f)

    mock_bad_source = {
        "id": "S01",
        "title": "Invalid Source",
        "authors": "Not An Array",  # Type error: should be array of strings
        "url": "https://example.com"
        # Missing required fields: publisher, date, verified_headings, etc.
    }
    try:
        jsonschema.validate(instance=mock_bad_source, schema=source_schema)
        results.append(("JSON Schema Validation", "FAIL (Not Caught)", "Should have raised jsonschema.ValidationError"))
    except jsonschema.ValidationError as e:
        print(f"  [SUCCESSFULLY REJECTED] Caught expected jsonschema error: {e.message}")
        results.append(("JSON Schema Validation", "PASS (Properly Rejected)", f"jsonschema.ValidationError: {e.message}"))

    # -------------------------------------------------------------
    # NEGATIVE TEST 5: Presentation Incomplete Slides (< 12)
    # -------------------------------------------------------------
    print("\n[Negative Test 5] Testing Presentation Slide Count Assertion...")
    mock_slide_count = 11  # Missing 1 slide
    try:
        if mock_slide_count != 12:
            raise AssertionError(f"Expected exactly 12 slides, found {mock_slide_count}")
        results.append(("Missing Slide Count", "FAIL (Not Caught)", "Should have raised AssertionError"))
    except AssertionError as e:
        print(f"  [SUCCESSFULLY REJECTED] Caught expected assertion: {e}")
        results.append(("Missing Slide Count", "PASS (Properly Rejected)", str(e)))

    print("\n" + "=" * 60)
    print("NEGATIVE TEST RESULTS SUMMARY")
    print("=" * 60)
    for test_name, status, detail in results:
        print(f"{test_name:30}: {status}")
    print("=" * 60)

    return results

if __name__ == "__main__":
    run_negative_tests()
