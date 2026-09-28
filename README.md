# 🤖 Agentic AI Social Media Content Generator (Task 2)

An autonomous, offline AI Agent built using **Python**, **Ollama**, and **Gemma 3:4B** designed to generate, review, and persist platform-specific social media posts, captions, hashtags, and 30-second video scripts.

---

## 📌 Project Overview & Objective

This repository contains the complete implementation for **Agentic AI Task 2**. The core objective is to create a lightweight, production-grade, and beginner-friendly social media agent that runs 100% locally on consumer hardware without relying on third-party cloud APIs (such as OpenAI, Claude, or OpenRouter).

### Key Features
- **100% Offline & Local Execution:** Powered by Gemma 3:4B via local Ollama inference.
- **Sequential Agentic Workflow:** Memory lookup -> Strategic Planning -> Tool Execution -> Quality Review -> Markdown Persistence.
- **6 Dedicated Agent Tools:**
  1. `Trend Idea Generator` — Generates 3 content angles locally and selects the best fit.
  2. `Caption Writer` — Crafts scroll-stopping hooks and platform-tailored post bodies.
  3. `Hashtag Generator` — Produces domain-relevant hashtags returned as a Python list.
  4. `Reel Script Generator` — Drafts scene-by-scene 30-second video scripts.
  5. `Content Reviewer` — Critiques output quality and suggests actionable tweaks.
  6. `File Saver` — Mandatory tool persisting output into structured Markdown files.
- **Persistent JSON Memory:** Saves history to `outputs/memory.json` to inform future runs with contextual continuity.
- **Multi-Platform & Multi-Tone Awareness:** Supports LinkedIn, Instagram, X/Twitter, and YouTube Shorts across various content vibes (Professional, Motivational, Funny, Meme style, etc.).

---

## 🛠️ Technology Stack

- **Language:** Python 3.14+
- **Local LLM Engine:** Ollama (v0.34.4+)
- **Model:** `gemma3:4b` (Google Gemma 3 4B parameters)
- **Virtual Environment:** `.venv`
- **Output Formats:** Markdown (`.md`), JSON (`.json`), PDF (`.pdf`)

---

## 📁 Project Structure

```
agentic_ai_task_2/
│
├── app/
│   ├── __init__.py      # Package initialization
│   ├── main.py          # Programmatic entry point & input validation
│   ├── agent.py         # Agent class orchestrating LLM & tool workflow
│   ├── tools.py         # Clean implementation of all 6 tools with logs
│   ├── memory.py        # JSON persistent memory manager
│   └── prompts.py       # Modular, platform-aware prompt templates
│
├── outputs/
│   ├── generated_posts/   # Saved Markdown posts (.md)
│   ├── generated_scripts/ # Saved Markdown video scripts (.md)
│   ├── saved_results/     # Final combined output records (.md)
│   └── memory.json        # Persistent local conversation history
│
├── tests/
│   └── test_cases.md    # 10 test cases, test matrix, error analysis & roadmap
│
├── screenshots/         # Visual execution logs and screenshots
│   ├── ollama_running.png
│   ├── demo_output.png
│   └── saved_file_output.png
│
├── report/
│   ├── build_pdf.py     # Script to generate internship report PDF
│   └── final_report.pdf # Compiled internship submission report PDF
│
├── README.md            # Comprehensive project documentation
├── requirements.txt     # Minimal dependencies (ollama)
├── test_ollama.py       # Ollama connectivity test script
├── run_tests.py         # Automated test runner for 10 test cases
└── demo.py              # Beginner-friendly CLI demo
```

---

## ⚙️ Ollama & Gemma 3:4B Setup Instructions

1. **Install Ollama:**
   Download and install Ollama from [ollama.com](https://ollama.com).

2. **Pull Required Local Model:**
   Open your terminal and pull the Gemma 3:4B model:
   ```bash
   ollama pull gemma3:4b
   ```

3. **Verify Ollama Status:**
   Run the quick verification script included in this repository:
   ```bash
   python test_ollama.py
   ```
   *Expected Output:* Explanation of Agentic AI generated locally by Gemma 3:4B.

---

## 📦 Installation & Setup

1. **Clone/Navigate to Workspace:**
   ```bash
   cd agentic_ai_task_2
   ```

2. **Activate Virtual Environment:**
   - **Windows:**
     ```cmd
     .venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     source .venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run the Application

### 1. Interactive CLI Demo
Run the interactive CLI program:
```bash
python demo.py
```

**Prompts asked:**
- `Enter your topic:` (e.g. `YOLOv8 helmet detection`)
- `Select Platform:` `1. LinkedIn`, `2. Instagram`, `3. X/Twitter`, `4. YouTube Shorts`
- `Select Tone:` `1. Professional`, `2. Motivational`, `3. Funny`, `4. Exciting`, etc.
- `Select Output Type:` `1. Post`, `2. Reel Script`, `3. Post + Reel Script`

### 2. Programmatic Python Import
```python
from app.main import generate_social_content

result = generate_social_content(
    topic="AI internship experience",
    platform="LinkedIn",
    tone="Motivational",
    output_type="Post"
)

print("Hook:", result["hook"])
print("Saved Path:", result["saved_file_path"])
```

### 3. Automated 10-Test Execution
To run all 10 test cases and verify persistent file generation:
```bash
python run_tests.py
```

---

## 📝 Example Output

### Sample User Input:
- **Topic:** YOLOv8 helmet detection
- **Platform:** LinkedIn
- **Tone:** Professional
- **Output Type:** Post + Reel Script

### Visual Tool Logs Printed:
```text
[Tool Called]: Trend Idea Generator
[Tool Called]: Caption Writer
[Tool Called]: Reel Script Generator
[Tool Called]: Hashtag Generator
[Tool Called]: Content Reviewer
[Tool Called]: File Saver
```

### Generated Result File:
Saved at `outputs/saved_results/yolov8_helmet_detection_final.md`:
```markdown
# Social Media Content Output

## Metadata
- **Topic:** YOLOv8 helmet detection
- **Platform:** LinkedIn
- **Tone:** Professional
- **Output Type:** Post + Reel Script

---

## 1. Content Angle / Idea
Angle: Real-time Computer Vision for Industrial Workplace Safety.

---

## 2. Hook
🚀 Is your computer vision model fast enough to save lives in real-time?

---

## 3. Caption / Post Body
Safety on construction sites isn't just about compliance—it's about real-time prevention. 

Using YOLOv8, we trained a custom object detection pipeline to identify safety helmets under varying lighting and occlusion scenarios...

---

## 4. Hashtags
#YOLOv8 #ComputerVision #AI #WorkplaceSafety #DeepLearning #Python

---

## 5. Reel Script (~30 Seconds)
TITLE: Real-Time Helmet Detection in 30 Seconds
[Scene 1 (0-5s)] Visual: Live camera feed highlighting worker. Audio: "What if AI could prevent workplace accidents before they happen?"
...

---

## 6. Content Review & Quality Evaluation
Hook Strength: 9/10. Platform Fit: Excellent for LinkedIn.
```

---

## 🧠 Memory Persistence Engine

The agent uses a persistent JSON memory stored at `outputs/memory.json`.
Before executing any generation tool, the agent reads past entries via `MemoryManager.get_recent_context()` and injects prior context into the LLM prompts. Every completed generation is automatically appended to the memory file.

---

## 🧪 Testing & Error Analysis Summary

See [`tests/test_cases.md`](tests/test_cases.md) for full details.

### Error Analysis (5 Scenario Case Studies):
1. **Generic AI Internship Post:** Fixed by adding concrete technical prompt constraints.
2. **Weak Meme Style Tone:** Resolved by framing contrast prompts (Expectation vs Reality).
3. **Reel Script Too Long:** Enforced explicit 4-scene timestamp boundaries (0-5s, 5-15s, 15-25s, 25-30s).
4. **Irrelevant Hashtags:** Cleaned hashtag extraction with regex filtering `r"#\w+"`.
5. **Windows Path Exception:** Slugified topic strings to prevent invalid character errors on Windows filesystems.

---

## ⚠️ Limitations & Future Improvements

### Limitations:
- **Offline Generation:** Trend Idea Generator produces content angles locally; it does not connect to live real-time internet trends.
- **Hardware Dependent Speed:** Inference speed depends on local GPU/VRAM hardware performance.

### Future Improvements:
1. Enforce structured JSON schemas via Pydantic output parsers.
2. Implement an interactive multi-turn feedback revision loop.
3. Integrate real-time RSS trend feeds into the trend generator tool.

---

## 💼 LinkedIn-Ready Project Report

**Project Title:** Agentic AI Social Media Content Generator  

**Short Description:**  
An autonomous, 100% offline Agentic AI system built with Python, Ollama, and Google's Gemma 3:4B model. The system plans, generates, reviews, and persists multi-platform social media content (posts, captions, hashtags, and 30-second reel scripts) tailored for LinkedIn, Instagram, X/Twitter, and YouTube Shorts.

**Technologies Used:**  
Python 3.14, Ollama, Gemma 3:4B, JSON Persistent Memory, Markdown, FPDF2.

**Key Features & AI/Agentic Workflow:**  
1. **Context & Memory Retrieval:** Queries persistent JSON memory (`outputs/memory.json`) for prior topics/tones.
2. **Strategic LLM Planning:** Formulates a 4-step content execution plan prior to generation.
3. **Sequential Tool Suite Execution:** Orchestrates 6 specialized tools:
   - *Trend Idea Generator*
   - *Caption Writer*
   - *Hashtag Generator*
   - *Reel Script Generator*
   - *Content Reviewer*
   - *File Saver*
4. **Quality Evaluation & Tone Consistency:** Reviews generated output for platform fit and requested tone consistency.
5. **Markdown & PDF Persistence:** Saves formatted results across structured output directories.

**Outcome & Results:**  
- 100% offline operation with zero paid API dependencies.
- Successfully executed 10 test scenarios across 4 platforms and 6 content tones.
- Generated and verified 10 complete output packages, posts, and 4-scene video scripts.

