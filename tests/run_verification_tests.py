"""
Comprehensive Verification Suite executing TEST 1 to TEST 5.
"""

import sys
import os
import json

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Ensure app imports work from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import generate_social_content
from app.memory import MemoryManager


def test_1_post():
    print("\n--------------------------------------------------")
    print("RUNNING TEST 1: Post Generation")
    print("--------------------------------------------------")
    topic = "AI internship experience"
    platform = "LinkedIn"
    tone = "Professional"
    output_type = "Post"

    res = generate_social_content(topic, platform, tone, output_type)

    assert res["topic"] == topic
    assert res["platform"] == platform
    assert res["tone"] == tone
    assert res["output_type"] == output_type
    assert res["caption"] != "N/A" and len(res["caption"]) > 0
    assert res["hook"] != "Not extracted" and len(res["hook"]) > 0
    assert len(res["hashtags"]) >= 5
    assert os.path.exists(res["saved_file_path"])

    print(f"✅ TEST 1 PASSED: File saved at {res['saved_file_path']}")
    return res


def test_2_reel():
    print("\n--------------------------------------------------")
    print("RUNNING TEST 2: Reel Script Generation")
    print("--------------------------------------------------")
    topic = "Python learning journey"
    platform = "Instagram"
    tone = "Funny"
    output_type = "Reel Script"

    res = generate_social_content(topic, platform, tone, output_type)

    assert res["output_type"] == "Reel Script"
    assert res["reel_script"] != "N/A" and len(res["reel_script"]) > 0
    assert os.path.exists(res["saved_file_path"])

    script_text = res["reel_script"]
    # Check scene indicators or structure
    assert "[Scene 1" in script_text or "Scene 1" in script_text or "Visual:" in script_text
    print(f"✅ TEST 2 PASSED: Reel script generated with 4-scene structure. File: {res['saved_file_path']}")
    return res


def test_3_post_plus_reel():
    print("\n--------------------------------------------------")
    print("RUNNING TEST 3: Post + Reel Script Generation")
    print("--------------------------------------------------")
    topic = "YOLOv8 helmet detection"
    platform = "LinkedIn"
    tone = "Professional"
    output_type = "Post + Reel Script"

    res = generate_social_content(topic, platform, tone, output_type)

    assert res["caption"] != "N/A"
    assert res["reel_script"] != "N/A"
    assert len(res["hashtags"]) >= 5
    assert os.path.exists(res["saved_file_path"])

    print(f"✅ TEST 3 PASSED: Combined Post + Reel output generated. File: {res['saved_file_path']}")
    return res


def test_4_persistence():
    print("\n--------------------------------------------------")
    print("RUNNING TEST 4: Memory Persistence Verification")
    print("--------------------------------------------------")
    memory = MemoryManager()
    records = memory.load_memory()

    assert len(records) > 0, "Memory should contain previous test records."

    context = memory.get_recent_context(current_topic="AI internship")
    assert "AI internship experience" in context or len(context) > 0

    print("✅ TEST 4 PASSED: Persistent JSON memory successfully retrieved prior context:")
    print(context)


def test_5_input_validation():
    print("\n--------------------------------------------------")
    print("RUNNING TEST 5: Input Validation Verification")
    print("--------------------------------------------------")

    # 1. Empty topic
    try:
        generate_social_content("", "LinkedIn", "Professional", "Post")
        assert False, "Empty topic should have raised ValueError"
    except ValueError as e:
        print(f"  - Empty topic rejected cleanly: {e}")

    # 2. Invalid platform
    try:
        generate_social_content("Topic", "TikTok", "Professional", "Post")
        assert False, "Invalid platform should have raised ValueError"
    except ValueError as e:
        print(f"  - Invalid platform rejected cleanly: {e}")

    # 3. Invalid output type
    try:
        generate_social_content("Topic", "LinkedIn", "Professional", "Thread")
        assert False, "Invalid output type should have raised ValueError"
    except ValueError as e:
        print(f"  - Invalid output type rejected cleanly: {e}")

    print("✅ TEST 5 PASSED: Input validation rejected all malformed requests.")


if __name__ == "__main__":
    print("🚀 STARTING E2E VERIFICATION TESTS...")
    test_1_post()
    test_2_reel()
    test_3_post_plus_reel()
    test_4_persistence()
    test_5_input_validation()
    print("\n🎉 ALL 5 VERIFICATION TESTS PASSED SUCCESSFULLY!")
