"""
Automated Test Runner for Social Media Agent.
Executes all 10 test cases programmatically and populates output folders and memory.json.
"""

import sys
import os

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.main import generate_social_content

TEST_CASES = [
    {
        "tc": "TC-01",
        "topic": "YOLOv8 helmet detection",
        "platform": "LinkedIn",
        "tone": "Professional",
        "output_type": "Post + Reel Script"
    },
    {
        "tc": "TC-02",
        "topic": "AI internship experience",
        "platform": "LinkedIn",
        "tone": "Motivational",
        "output_type": "Post"
    },
    {
        "tc": "TC-03",
        "topic": "Python learning journey",
        "platform": "Instagram",
        "tone": "Funny",
        "output_type": "Reel Script"
    },
    {
        "tc": "TC-04",
        "topic": "Machine learning project",
        "platform": "X/Twitter",
        "tone": "Short and catchy",
        "output_type": "Post"
    },
    {
        "tc": "TC-05",
        "topic": "Data annotation struggles",
        "platform": "LinkedIn",
        "tone": "Humorous",
        "output_type": "Post"
    },
    {
        "tc": "TC-06",
        "topic": "Model failed in production",
        "platform": "Instagram",
        "tone": "Meme style",
        "output_type": "Reel Script"
    },
    {
        "tc": "TC-07",
        "topic": "Final year project",
        "platform": "LinkedIn",
        "tone": "Professional",
        "output_type": "Post"
    },
    {
        "tc": "TC-08",
        "topic": "Computer vision project",
        "platform": "YouTube Shorts",
        "tone": "Exciting",
        "output_type": "Reel Script"
    },
    {
        "tc": "TC-09",
        "topic": "Debugging FastAPI",
        "platform": "X/Twitter",
        "tone": "Funny",
        "output_type": "Post"
    },
    {
        "tc": "TC-10",
        "topic": "Open-source contribution",
        "platform": "LinkedIn",
        "tone": "Inspirational",
        "output_type": "Post"
    }
]


def run_all_tests():
    print("🚀 Starting Automated Test Execution for 10 Test Cases...\n")
    results_summary = []

    for item in TEST_CASES:
        tc = item["tc"]
        topic = item["topic"]
        platform = item["platform"]
        tone = item["tone"]
        output_type = item["output_type"]

        print(f"\n==========================================")
        print(f"Running {tc}: Topic='{topic}' on {platform}")
        print(f"==========================================")

        try:
            res = generate_social_content(topic, platform, tone, output_type)
            saved_path = res["saved_file_path"]
            exists = os.path.exists(saved_path)
            status = "PASSED" if exists else "FAILED (File not found)"
            results_summary.append((tc, topic, status, saved_path))
            print(f"✅ {tc} Completed. Output File Exists: {exists}")
        except Exception as e:
            print(f"❌ {tc} FAILED with error: {e}")
            results_summary.append((tc, topic, f"FAILED: {e}", "N/A"))

    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY REPORT")
    print("=" * 60)
    for tc, topic, status, path in results_summary:
        print(f"{tc} | {status} | {topic} | Path: {path}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_tests()
