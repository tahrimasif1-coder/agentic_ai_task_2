"""
Prompts repository for Social Media Content Agent using Gemma 3:4B via Ollama.
Contains system prompts, planning prompts, tool-specific prompts, platform rules, and tone guidelines.
"""

SYSTEM_PROMPT = """You are an expert Social Media AI Strategist and Content Creator running locally via Gemma 3:4B.
Your goal is to generate high-performing, platform-optimized, and engaging content tailored to the requested topic, platform, tone, and format.
Follow instructions strictly, stay creative yet practical, and adapt tone and formatting specifically to each social media platform.
"""

PLATFORM_GUIDELINES = {
    "LinkedIn": (
        "Focus on professional insights, career lessons, industry impact, clear line breaks for readability, "
        "and strong professional hooks. Avoid clickbait; use clean formatting."
    ),
    "Instagram": (
        "Focus on visually appealing hooks, conversational storytelling, relatable emojis, "
        "strong call-to-actions, and aesthetic appeal."
    ),
    "X/Twitter": (
        "Focus on conciseness (under 280 characters or punchy thread format), high-impact hooks, "
        "direct phrasing, minimal fluff, and sharp takeaway points."
    ),
    "YouTube Shorts": (
        "Focus on fast-paced verbal hooks, high viewer retention structure, visual scene descriptions, "
        "30-second pacing, and strong audio/visual directions."
    )
}


def get_planning_prompt(topic: str, platform: str, tone: str, output_type: str, memory_context: str = "") -> str:
    """Generate prompt for Agent Planning step."""
    guideline = PLATFORM_GUIDELINES.get(platform, "Create engaging, platform-suited content.")
    return f"""Analyze the user request and outline a 4-step content execution plan.

USER REQUEST:
- Topic: {topic}
- Target Platform: {platform}
- Desired Tone: {tone}
- Requested Output Type: {output_type}

PLATFORM GUIDELINE:
{guideline}

RECENT MEMORY CONTEXT:
{memory_context if memory_context else "No prior history available."}

Provide a concise, numbered plan (1 to 4) detailing:
1. Core Content Angle & Target Audience Insights
2. Hook Strategy & Platform Framing
3. Content & Script Structure
4. Call-To-Action & Review Checklist
"""


def get_trend_idea_prompt(topic: str, platform: str, tone: str, memory_context: str = "") -> str:
    """Generate prompt for Trend Idea Generator tool."""
    return f"""You are a Social Media Content Strategist. Generate 3 unique content angles/ideas for the following topic:

Topic: {topic}
Platform: {platform}
Tone: {tone}
{f"Prior Context: {memory_context}" if memory_context else ""}

Output format:
Angle 1: [Short Title] - [Explanation of perspective]
Angle 2: [Short Title] - [Explanation of perspective]
Angle 3: [Short Title] - [Explanation of perspective]

Selected Angle: [Specify the single best angle from above with reason why it fits the platform best]
"""


def get_caption_prompt(topic: str, selected_angle: str, platform: str, tone: str, memory_context: str = "") -> str:
    """Generate prompt for Caption Writer tool."""
    guideline = PLATFORM_GUIDELINES.get(platform, "")
    return f"""Write an engaging social media post for {platform}.

Topic: {topic}
Selected Content Angle: {selected_angle}
Requested Tone: {tone}
Platform Guidelines: {guideline}
{f"Past Style Context: {memory_context}" if memory_context else ""}

Requirements:
1. Hook: 1-2 compelling opening lines designed to stop the scroll.
2. Main Body: Well-structured caption matching the requested tone ({tone}). Use appropriate formatting (line breaks, bullet points if helpful).
3. Call to Action (CTA): A closing prompt to invite comments, shares, or thoughts.

Output Format:
HOOK: [Opening line(s)]
CAPTION: [Full caption body including Hook and CTA]
"""


def get_hashtag_prompt(topic: str, platform: str, content_snippet: str) -> str:
    """Generate prompt for Hashtag Generator tool."""
    return f"""Generate 5 to 10 highly relevant hashtags for a {platform} post.

Topic: {topic}
Content Snippet: {content_snippet}

Requirements:
- Return ONLY hashtags separated by spaces or comma.
- Must include a mix of broad industry tags and specific topic tags.
- Do NOT include markdown explanations, numbers, or extra text.
- Example format: #AI #Python #MachineLearning #TechCommunity #Coding
"""


def get_reel_script_prompt(topic: str, selected_angle: str, platform: str, tone: str) -> str:
    """Generate prompt for Reel Script Generator tool."""
    return f"""Generate a short scene-based video script for a {platform} (approx. 30 seconds).

Topic: {topic}
Angle: {selected_angle}
Tone: {tone}

Requirements:
- Structure into EXACTLY 4 scenes:
  * Scene 1 (0-5s): Hook
  * Scene 2 (5-15s): Core Message
  * Scene 3 (15-25s): Key Takeaway/Demo
  * Scene 4 (25-30s): CTA
- For each scene, specify:
  * Timecode / Scene Number
  * Visual Direction (what's on screen)
  * Audio / Voiceover (what is spoken or sound effects)

Output Format:
TITLE: [Script Title]
TARGET DURATION: ~30 Seconds

[Scene 1 (0-5s)]
Visual: ...
Audio: ...

[Scene 2 (5-15s)]
Visual: ...
Audio: ...

[Scene 3 (15-25s)]
Visual: ...
Audio: ...

[Scene 4 (25-30s)]
Visual: ...
Audio: ...
"""


def get_review_prompt(topic: str, platform: str, tone: str, content: str) -> str:
    """Generate prompt for Content Reviewer tool."""
    return f"""Review the following generated social media content for {platform}.

Topic: {topic}
Target Platform: {platform}
Requested Tone: {tone}

Content to Review:
{content}

Perform a quality evaluation and answer:
1. Hook Strength: (Rating 1-10 & comment)
2. Platform Fit: (Is it optimized for {platform}?)
3. Tone Consistency: (Evaluate tone consistency specifically against the requested tone: '{tone}')
4. Key Weaknesses / Areas for Improvement: (1-2 bullet points)
5. Final Verdict: (Approved / Needs minor tweaks)
"""
