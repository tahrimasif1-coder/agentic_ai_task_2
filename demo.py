"""
Interactive CLI Demo for Agentic AI Task 2 - Social Media Content Generator.
Runs locally using Gemma 3:4B via Ollama.
"""

import sys
import os

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Add root directory to sys.path to ensure imports work from any working directory
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.main import generate_social_content


def display_banner():
    print("""
============================================================
🤖 AGENTIC AI CONTENT GENERATOR (Task 2)
Powered locally by Gemma 3:4B & Ollama
============================================================
""")


def get_user_inputs():
    """Interactively collects and validates user CLI inputs."""
    display_banner()

    # 1. Topic input
    topic = input("📌 Enter your topic (e.g., 'YOLOv8 helmet detection'): ").strip()
    while not topic:
        print("❌ Error: Topic cannot be empty!")
        topic = input("📌 Enter your topic: ").strip()

    # 2. Platform Selection
    print("\n🌐 Select Platform:")
    print("  1. LinkedIn")
    print("  2. Instagram")
    print("  3. X/Twitter")
    print("  4. YouTube Shorts")
    platform_map = {
        "1": "LinkedIn",
        "2": "Instagram",
        "3": "X/Twitter",
        "4": "YouTube Shorts"
    }
    p_choice = input("Enter platform number [1-4] (default 1): ").strip() or "1"
    platform = platform_map.get(p_choice, "LinkedIn")

    # 3. Tone Selection
    print("\n🎭 Select Tone:")
    print("  1. Professional")
    print("  2. Motivational")
    print("  3. Funny / Humorous")
    print("  4. Exciting")
    print("  5. Inspirational")
    print("  6. Short and catchy")
    tone_map = {
        "1": "Professional",
        "2": "Motivational",
        "3": "Funny",
        "4": "Exciting",
        "5": "Inspirational",
        "6": "Short and catchy"
    }
    t_choice = input("Enter tone number [1-6] or type custom tone (default 1): ").strip() or "1"
    tone = tone_map.get(t_choice, t_choice)

    # 4. Output Type Selection
    print("\n📝 Select Output Type:")
    print("  1. Post")
    print("  2. Reel Script")
    print("  3. Post + Reel Script")
    output_map = {
        "1": "Post",
        "2": "Reel Script",
        "3": "Post + Reel Script"
    }
    o_choice = input("Enter output type number [1-3] (default 1): ").strip() or "1"
    output_type = output_map.get(o_choice, "Post")

    return topic, platform, tone, output_type


def main():
    try:
        topic, platform, tone, output_type = get_user_inputs()
        
        print("\n⏳ Agent starting workflow...\n")
        result = generate_social_content(
            topic=topic,
            platform=platform,
            tone=tone,
            output_type=output_type
        )

        # Print structured final summary
        print("\n" + "=" * 60)
        print("🎯 FINAL AGENT GENERATED OUTPUT SUMMARY")
        print("=" * 60)
        print(f"📌 TOPIC:          {result['topic']}")
        print(f"🌐 PLATFORM:       {result['platform']}")
        print(f"🎭 TONE:           {result['tone']}")
        print(f"📝 OUTPUT TYPE:     {result['output_type']}")
        print("-" * 60)
        print(f"💡 CONTENT IDEA:\n{result['content_idea']}\n")
        print(f"🎣 HOOK:\n{result['hook']}\n")
        
        if result['caption'] != "N/A":
            print(f"📄 CAPTION:\n{result['caption']}\n")
            
        print(f"🏷️ HASHTAGS:\n{' '.join(result['hashtags'])}\n")
        
        if result['reel_script'] != "N/A":
            print(f"🎬 REEL SCRIPT (~30s):\n{result['reel_script']}\n")
            
        print(f"🔍 REVIEW COMMENTS:\n{result['review_comments']}\n")
        print("-" * 60)
        print(f"💾 SAVED FILE PATH: {result['saved_file_path']}")
        print("=" * 60 + "\n")

    except KeyboardInterrupt:
        print("\n\n🛑 Process cancelled by user. Exiting.")
        sys.exit(0)
    except RuntimeError as re_err:
        print(f"\n❌ RUNTIME ERROR: {re_err}")
        print("👉 Tip: Make sure Ollama is running (`ollama serve`) and model 'gemma3:4b' is pulled.")
        sys.exit(1)
    except Exception as err:
        print(f"\n❌ UNEXPECTED ERROR: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
