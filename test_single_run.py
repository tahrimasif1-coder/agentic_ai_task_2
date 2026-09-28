"""
Single Test Execution Script to generate real saved outputs.
"""

import sys
import os

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.main import generate_social_content

if __name__ == "__main__":
    print("Testing single agent run...")
    res = generate_social_content(
        topic="YOLOv8 helmet detection",
        platform="LinkedIn",
        tone="Professional",
        output_type="Post + Reel Script"
    )
    print("\nSUCCESS!")
    print("Saved Path:", res["saved_file_path"])
    print("Hook:", res["hook"])
    print("Hashtags:", res["hashtags"])
