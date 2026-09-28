"""
Tool definitions for the Agentic AI Social Media Content Generator.
Each tool prints explicit execution logs: [Tool Called]: <Tool Name>
"""

import os
import re
import sys
import ollama
from typing import List, Dict, Any, Tuple

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
from app.prompts import (
    SYSTEM_PROMPT,
    get_trend_idea_prompt,
    get_caption_prompt,
    get_hashtag_prompt,
    get_reel_script_prompt,
    get_review_prompt
)

MODEL_NAME = "gemma3:4b"


def call_ollama(prompt: str, system_prompt: str = SYSTEM_PROMPT) -> str:
    """Helper function to execute prompt via Ollama Gemma 3:4B."""
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            options={"num_predict": 256, "temperature": 0.7}
        )
        return response.message.content.strip()
    except Exception as e:
        raise RuntimeError(
            f"Failed to communicate with Ollama model '{MODEL_NAME}'. "
            f"Ensure Ollama service is running locally on port 11434.\nDetails: {str(e)}"
        )


def trend_idea_generator(topic: str, platform: str, tone: str, memory_context: str = "") -> Dict[str, Any]:
    """
    Tool 1: Trend Idea Generator
    Generates 3 content angles locally using Gemma 3:4B and selects the optimal angle.
    """
    print("[Tool Called]: Trend Idea Generator", flush=True)
    prompt = get_trend_idea_prompt(topic, platform, tone, memory_context)
    raw_response = call_ollama(prompt)

    # Parse selected angle or default to response summary
    selected_idea = raw_response
    if "Selected Angle:" in raw_response:
        selected_idea = raw_response.split("Selected Angle:")[-1].strip()
    elif "Angle 1:" in raw_response:
        lines = [line.strip() for line in raw_response.split("\n") if line.strip().startswith("Angle 1:")]
        if lines:
            selected_idea = lines[0]

    return {
        "raw_ideas": raw_response,
        "selected_idea": selected_idea
    }


def caption_writer(topic: str, selected_angle: str, platform: str, tone: str, memory_context: str = "") -> Dict[str, str]:
    """
    Tool 2: Caption Writer
    Generates a platform-specific hook and caption matching requested tone.
    """
    print("[Tool Called]: Caption Writer", flush=True)
    prompt = get_caption_prompt(topic, selected_angle, platform, tone, memory_context)
    raw_response = call_ollama(prompt)

    hook = "Not extracted"
    caption = raw_response

    if "HOOK:" in raw_response and "CAPTION:" in raw_response:
        parts = raw_response.split("CAPTION:")
        hook_part = parts[0].replace("HOOK:", "").strip()
        caption = parts[1].strip()
        hook = hook_part
    elif "HOOK:" in raw_response:
        lines = raw_response.split("\n")
        for line in lines:
            if line.startswith("HOOK:"):
                hook = line.replace("HOOK:", "").strip()
                break

    if hook == "Not extracted" and caption:
        # Fallback to first sentence as hook
        sentences = caption.split(".")
        hook = sentences[0].strip() + ("." if sentences[0] else "")

    return {
        "hook": hook,
        "caption": caption
    }


def hashtag_generator(topic: str, platform: str, content_snippet: str) -> List[str]:
    """
    Tool 3: Hashtag Generator
    Generates relevant hashtags as a Python list.
    """
    print("[Tool Called]: Hashtag Generator", flush=True)
    prompt = get_hashtag_prompt(topic, platform, content_snippet)
    raw_response = call_ollama(prompt)

    # Extract all words starting with #
    tags = re.findall(r"#\w+", raw_response)
    
    # Deduplicate while preserving order
    seen = set()
    unique_tags = []
    for tag in tags:
        if tag.lower() not in seen:
            seen.add(tag.lower())
            unique_tags.append(tag)

    if not unique_tags:
        # Fallback hashtags based on topic
        clean_topic = re.sub(r"[^\w\s]", "", topic).split()
        unique_tags = [f"#{word.capitalize()}" for word in clean_topic if len(word) > 2]
        unique_tags.extend(["#SocialMedia", "#ContentStrategy"])

    return unique_tags[:10]


def reel_script_generator(topic: str, selected_angle: str, platform: str, tone: str) -> str:
    """
    Tool 4: Reel Script Generator
    Generates a 30-second scene-based video script.
    """
    print("[Tool Called]: Reel Script Generator", flush=True)
    prompt = get_reel_script_prompt(topic, selected_angle, platform, tone)
    return call_ollama(prompt)


def content_reviewer(topic: str, platform: str, tone: str, content: str) -> str:
    """
    Tool 5: Content Reviewer
    Reviews generated content, evaluates fit against requested tone, and suggests improvements.
    """
    print("[Tool Called]: Content Reviewer", flush=True)
    prompt = get_review_prompt(topic, platform, tone, content)
    return call_ollama(prompt)


def file_saver(
    topic: str,
    platform: str,
    tone: str,
    output_type: str,
    idea: str,
    hook: str,
    caption: str,
    hashtags: List[str],
    script: str,
    review: str
) -> Dict[str, str]:
    """
    Tool 6: File Saver (Mandatory)
    Saves generated content as Markdown files in proper directories and returns saved file paths.
    """
    print("[Tool Called]: File Saver", flush=True)

    # Safe slug for filename
    safe_topic = re.sub(r"[^\w\s-]", "", topic.lower())
    slug = re.sub(r"[-\s]+", "_", safe_topic).strip("_")[:30]
    if not slug:
        slug = "content_result"

    posts_dir = os.path.join("outputs", "generated_posts")
    scripts_dir = os.path.join("outputs", "generated_scripts")
    results_dir = os.path.join("outputs", "saved_results")

    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(scripts_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    hashtag_str = " ".join(hashtags) if isinstance(hashtags, list) else str(hashtags)
    
    markdown_content = f"""# Social Media Content Output

## Metadata
- **Topic:** {topic}
- **Platform:** {platform}
- **Tone:** {tone}
- **Output Type:** {output_type}

---

## 1. Content Angle / Idea
{idea}

---

## 2. Hook
{hook}

---

## 3. Caption / Post Body
{caption if caption else "N/A (Reel Script requested)"}

---

## 4. Hashtags
{hashtag_str}

---

## 5. Reel Script (~30 Seconds)
{script if script else "N/A (Post output requested)"}

---

## 6. Content Review & Quality Evaluation
{review}
"""

    saved_paths = {}

    # Save to specific directory depending on output_type
    if output_type in ["Post", "Post + Reel Script"]:
        post_path = os.path.join(posts_dir, f"{slug}_post.md")
        with open(post_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        saved_paths["post_path"] = post_path

    if output_type in ["Reel Script", "Post + Reel Script"]:
        script_path = os.path.join(scripts_dir, f"{slug}_script.md")
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        saved_paths["script_path"] = script_path

    # Always save combined result in saved_results directory
    final_path = os.path.join(results_dir, f"{slug}_final.md")
    with open(final_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    saved_paths["final_path"] = final_path

    return {
        "primary_path": final_path,
        "all_paths": saved_paths
    }
