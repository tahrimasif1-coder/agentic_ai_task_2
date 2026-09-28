"""
Main entry point module for programmatic execution of the Social Media Agent.
Provides helper wrapper function `generate_social_content` with robust error handling.
"""

from typing import Dict, Any
from app.agent import SocialMediaAgent


def generate_social_content(
    topic: str,
    platform: str,
    tone: str,
    output_type: str
) -> Dict[str, Any]:
    """
    Programmatic interface for running the Social Media Agent with input validation.
    
    Args:
        topic: Social media topic or keyword (e.g. 'YOLOv8 helmet detection')
        platform: Target platform ('LinkedIn', 'Instagram', 'X/Twitter', 'YouTube Shorts')
        tone: Desired content tone ('Professional', 'Motivational', 'Funny', etc.)
        output_type: Format ('Post', 'Reel Script', 'Post + Reel Script')
        
    Returns:
        Structured result dictionary.
    """
    # Validate inputs
    if not topic or not topic.strip():
        raise ValueError("Topic cannot be empty. Please provide a valid social media topic.")
        
    valid_platforms = ["LinkedIn", "Instagram", "X/Twitter", "YouTube Shorts"]
    if platform not in valid_platforms:
        raise ValueError(f"Invalid platform '{platform}'. Choose from: {', '.join(valid_platforms)}")
        
    valid_outputs = ["Post", "Reel Script", "Post + Reel Script"]
    if output_type not in valid_outputs:
        raise ValueError(f"Invalid output type '{output_type}'. Choose from: {', '.join(valid_outputs)}")

    # Instantiate and run agent
    agent = SocialMediaAgent()
    return agent.run(topic=topic.strip(), platform=platform, tone=tone, output_type=output_type)


if __name__ == "__main__":
    # Quick standalone test
    print("Testing app/main.py execution...")
    res = generate_social_content(
        topic="Python Agentic AI Development",
        platform="LinkedIn",
        tone="Professional",
        output_type="Post"
    )
    print("Saved file path:", res["saved_file_path"])
