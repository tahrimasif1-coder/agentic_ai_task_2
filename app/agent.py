"""
Main Agent workflow implementation for Social Media Content Generation.
Orchestrates memory loading, LLM planning, sequential tool execution, and result saving.
"""

import sys
from typing import Dict, Any
from app.memory import MemoryManager

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
from app.prompts import get_planning_prompt
from app.tools import (
    call_ollama,
    trend_idea_generator,
    caption_writer,
    hashtag_generator,
    reel_script_generator,
    content_reviewer,
    file_saver
)


class SocialMediaAgent:
    """Agent orchestrating local Gemma 3:4B tools to generate social media content."""

    def __init__(self, memory_file_path: str = None):
        if memory_file_path:
            self.memory = MemoryManager(memory_file_path)
        else:
            self.memory = MemoryManager()

    def run(self, topic: str, platform: str, tone: str, output_type: str) -> Dict[str, Any]:
        """
        Executes full agentic workflow:
        1. Memory Context Retrieval
        2. Agent Planning
        3. Sequential Tool Execution based on Output Type
        4. Content Quality Review
        5. File Saver Execution
        6. Persistent Memory Update
        """
        print(f"\n==================================================")
        print(f"🚀 AGENT STARTED: '{topic}'")
        print(f"Platform: {platform} | Tone: {tone} | Output Type: {output_type}")
        print(f"==================================================\n")

        # Step 1: Memory Context Retrieval
        memory_context = self.memory.get_recent_context(current_topic=topic)
        if memory_context:
            print("🧠 [Memory Loaded]: Found prior context from memory:")
            print(memory_context)
            print()
        else:
            print("🧠 [Memory Loaded]: No prior topic context. Proceeding with fresh memory.\n")

        # Step 2: Agent Planning
        print("📋 [Agent Planning]: Formulating execution strategy...")
        planning_prompt = get_planning_prompt(topic, platform, tone, output_type, memory_context)
        plan_output = call_ollama(planning_prompt)
        print("\n--- AGENT PLAN ---")
        print(plan_output)
        print("-------------------\n")

        # Step 3: Tool Execution Sequence
        # Tool 1: Trend Idea Generator
        idea_res = trend_idea_generator(topic, platform, tone, memory_context)
        selected_idea = idea_res["selected_idea"]

        caption = ""
        hook = ""
        script = ""

        if output_type in ["Post", "Post + Reel Script"]:
            # Tool 2: Caption Writer
            caption_res = caption_writer(topic, selected_idea, platform, tone, memory_context)
            hook = caption_res["hook"]
            caption = caption_res["caption"]

        if output_type in ["Reel Script", "Post + Reel Script"]:
            # Tool 4: Reel Script Generator
            script = reel_script_generator(topic, selected_idea, platform, tone)
            if not hook and script:
                # If only Reel Script requested, extract first line as visual/verbal hook
                hook = script.split("\n")[0]

        # Tool 3: Hashtag Generator
        content_snippet = caption if caption else script
        hashtags = hashtag_generator(topic, platform, content_snippet)

        # Tool 5: Content Reviewer
        combined_content = f"Hook: {hook}\n\nCaption: {caption}\n\nScript: {script}"
        review_comments = content_reviewer(topic, platform, tone, combined_content)

        # Tool 6: File Saver (Mandatory)
        file_save_res = file_saver(
            topic=topic,
            platform=platform,
            tone=tone,
            output_type=output_type,
            idea=selected_idea,
            hook=hook,
            caption=caption,
            hashtags=hashtags,
            script=script,
            review=review_comments
        )
        saved_file_path = file_save_res["primary_path"]

        # Step 4: Persist in Memory
        self.memory.save_record(
            topic=topic,
            platform=platform,
            tone=tone,
            output_type=output_type,
            selected_idea=selected_idea,
            hook=hook,
            saved_file_path=saved_file_path
        )
        print("💾 [Memory Saved]: Output record appended to memory.json")

        result = {
            "topic": topic,
            "platform": platform,
            "tone": tone,
            "output_type": output_type,
            "plan": plan_output,
            "content_idea": selected_idea,
            "hook": hook,
            "caption": caption if caption else "N/A",
            "hashtags": hashtags,
            "reel_script": script if script else "N/A",
            "review_comments": review_comments,
            "saved_file_path": saved_file_path,
            "all_saved_paths": file_save_res["all_paths"]
        }

        print(f"\n✅ WORKFLOW COMPLETED SUCCESSFULLY!")
        print(f"Primary output saved at: {saved_file_path}\n")

        return result
