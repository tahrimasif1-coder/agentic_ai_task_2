# Agentic AI Task 2 — Test Cases & Error Analysis

This document details the test matrix, empirical test execution logs, and error analysis for the local Gemma 3:4B Social Media Agent.

---

## 🧪 Test Matrix (10 Required Scenarios)

| # | Topic | Platform | Tone | Output Type | Expected Tools Called | Expected Saved Path | Rating |
|---|---|---|---|---|---|---|---|
| **1** | YOLOv8 helmet detection | LinkedIn | Professional | Post + Reel Script | All 6 Tools | `outputs/saved_results/yolov8_helmet_detection_final.md` | Useful |
| **2** | AI internship experience | LinkedIn | Motivational | Post | 5 Tools (No Reel) | `outputs/saved_results/ai_internship_experience_final.md` | Useful |
| **3** | Python learning journey | Instagram | Funny | Reel Script | 5 Tools (No Post Caption) | `outputs/saved_results/python_learning_journey_final.md` | Useful |
| **4** | Machine learning project | X/Twitter | Short and catchy | Post | 5 Tools | `outputs/saved_results/machine_learning_project_final.md` | Useful |
| **5** | Data annotation struggles | LinkedIn | Humorous | Post | 5 Tools | `outputs/saved_results/data_annotation_struggles_final.md` | Useful |
| **6** | Model failed in production | Instagram | Meme style | Reel Script | 5 Tools | `outputs/saved_results/model_failed_in_production_final.md` | Useful |
| **7** | Final year project | LinkedIn | Professional | Post | 5 Tools | `outputs/saved_results/final_year_project_final.md` | Useful |
| **8** | Computer vision project | YouTube Shorts | Exciting | Reel Script | 5 Tools | `outputs/saved_results/computer_vision_project_final.md` | Useful |
| **9** | Debugging FastAPI | X/Twitter | Funny | Post | 5 Tools | `outputs/saved_results/debugging_fastapi_final.md` | Useful |
| **10** | Open-source contribution | LinkedIn | Inspirational | Post | 5 Tools | `outputs/saved_results/open_source_contribution_final.md` | Useful |

---

## 📊 Detailed Test Descriptions

### Test Case 1: YOLOv8 Helmet Detection
- **Input:** Topic="YOLOv8 helmet detection", Platform="LinkedIn", Tone="Professional", Output Type="Post + Reel Script"
- **Tools Used:** `Trend Idea Generator`, `Caption Writer`, `Reel Script Generator`, `Hashtag Generator`, `Content Reviewer`, `File Saver`
- **Expected Output:** Professional LinkedIn post explaining computer vision safety detection + 30s video script breakdown + relevant computer vision tags.
- **Saved Path:** `outputs/saved_results/yolov8_helmet_detection_final.md`
- **Usefulness:** Highly useful for portfolio showcases.

### Test Case 2: AI Internship Experience
- **Input:** Topic="AI internship experience", Platform="LinkedIn", Tone="Motivational", Output Type="Post"
- **Tools Used:** `Trend Idea Generator`, `Caption Writer`, `Hashtag Generator`, `Content Reviewer`, `File Saver`
- **Expected Output:** Motivational storytelling caption about learning LLMs and persistence, strong hook, professional hashtag set.
- **Saved Path:** `outputs/saved_results/ai_internship_experience_final.md`
- **Usefulness:** Useful for student networking.

### Test Case 3: Python Learning Journey
- **Input:** Topic="Python learning journey", Platform="Instagram", Tone="Funny", Output Type="Reel Script"
- **Tools Used:** `Trend Idea Generator`, `Caption Writer`, `Reel Script Generator`, `Hashtag Generator`, `Content Reviewer`, `File Saver`
- **Expected Output:** Relatable visual reel script showing expectations vs reality of syntax errors.
- **Saved Path:** `outputs/saved_results/python_learning_journey_final.md`
- **Usefulness:** Useful for developer humor reels.

### Test Case 4: Machine Learning Project
- **Input:** Topic="Machine learning project", Platform="X/Twitter", Tone="Short and catchy", Output Type="Post"
- **Tools Used:** `Trend Idea Generator`, `Caption Writer`, `Hashtag Generator`, `Content Reviewer`, `File Saver`
- **Expected Output:** Short punchy tweet (<280 chars) summarizing model accuracy and repository link.
- **Saved Path:** `outputs/saved_results/machine_learning_project_final.md`
- **Usefulness:** Useful for build-in-public updates.

### Test Case 5: Data Annotation Struggles
- **Input:** Topic="Data annotation struggles", Platform="LinkedIn", Tone="Humorous", Output Type="Post"
- **Tools Used:** `Trend Idea Generator`, `Caption Writer`, `Hashtag Generator`, `Content Reviewer`, `File Saver`
- **Expected Output:** Humorous anecdote about manually bounding 5,000 images, connecting to quality data practices.
- **Saved Path:** `outputs/saved_results/data_annotation_struggles_final.md`
- **Usefulness:** Useful for data engineering engagement.

### Test Case 6: Model Failed in Production
- **Input:** Topic="Model failed in production", Platform="Instagram", Tone="Meme style", Output Type="Reel Script"
- **Tools Used:** `Trend Idea Generator`, `Caption Writer`, `Reel Script Generator`, `Hashtag Generator`, `Content Reviewer`, `File Saver`
- **Expected Output:** Meme video concept contrasting local 99% accuracy vs production memory crash.
- **Saved Path:** `outputs/saved_results/model_failed_in_production_final.md`
- **Usefulness:** Highly engaging reel format.

### Test Case 7: Final Year Project
- **Input:** Topic="Final year project", Platform="LinkedIn", Tone="Professional", Output Type="Post"
- **Tools Used:** `Trend Idea Generator`, `Caption Writer`, `Hashtag Generator`, `Content Reviewer`, `File Saver`
- **Expected Output:** Comprehensive portfolio post detailing problem statement, stack, and outcome.
- **Saved Path:** `outputs/saved_results/final_year_project_final.md`
- **Usefulness:** Essential for graduate hiring.

### Test Case 8: Computer Vision Project
- **Input:** Topic="Computer vision project", Platform="YouTube Shorts", Tone="Exciting", Output Type="Reel Script"
- **Tools Used:** `Trend Idea Generator`, `Caption Writer`, `Reel Script Generator`, `Hashtag Generator`, `Content Reviewer`, `File Saver`
- **Expected Output:** High-energy 30s video script with fast visual cuts and audio hooks.
- **Saved Path:** `outputs/saved_results/computer_vision_project_final.md`
- **Usefulness:** Fits YouTube Shorts format requirements.

### Test Case 9: Debugging FastAPI
- **Input:** Topic="Debugging FastAPI", Platform="X/Twitter", Tone="Funny", Output Type="Post"
- **Tools Used:** `Trend Idea Generator`, `Caption Writer`, `Hashtag Generator`, `Content Reviewer`, `File Saver`
- **Expected Output:** Witty tweet about async event loop errors and missing `await` keywords.
- **Saved Path:** `outputs/saved_results/debugging_fastapi_final.md`
- **Usefulness:** Highly relatable dev tweet.

### Test Case 10: Open-Source Contribution
- **Input:** Topic="Open-source contribution", Platform="LinkedIn", Tone="Inspirational", Output Type="Post"
- **Tools Used:** `Trend Idea Generator`, `Caption Writer`, `Hashtag Generator`, `Content Reviewer`, `File Saver`
- **Expected Output:** Uplifting post encouraging junior developers to submit their first pull request.
- **Saved Path:** `outputs/saved_results/open_source_contribution_final.md`
- **Usefulness:** Excellent community building post.

---

## 📈 Empirical Test Results & Verification

| Test Case | Status | Verified Output File | Memory Persisted |
|---|---|---|---|
| TC-01 | PASSED | `outputs/saved_results/yolov8_helmet_detection_final.md` | Yes |
| TC-02 | PASSED | `outputs/saved_results/ai_internship_experience_final.md` | Yes |
| TC-03 | PASSED | `outputs/saved_results/python_learning_journey_final.md` | Yes |
| TC-04 | PASSED | `outputs/saved_results/machine_learning_project_final.md` | Yes |
| TC-05 | PASSED | `outputs/saved_results/data_annotation_struggles_final.md` | Yes |
| TC-06 | PASSED | `outputs/saved_results/model_failed_in_production_final.md` | Yes |
| TC-07 | PASSED | `outputs/saved_results/final_year_project_final.md` | Yes |
| TC-08 | PASSED | `outputs/saved_results/computer_vision_project_final.md` | Yes |
| TC-09 | PASSED | `outputs/saved_results/debugging_fastapi_final.md` | Yes |
| TC-10 | PASSED | `outputs/saved_results/open_source_contribution_final.md` | Yes |

---

## 🔍 Error Analysis (5 Failure/Weak Scenarios)

### Scenario 1: Generic AI Internship Post
- **Problem Found:** Initial output produced cliché phrases ("In today's fast-paced tech world...") without specific technical details.
- **Possible Reason:** Prompt lacked platform-specific constraints forcing concrete examples.
- **Fix Applied:** Updated `get_caption_prompt` in `app/prompts.py` with explicit instructions to include actionable key takeaways and realistic project context.

### Scenario 2: Weak Meme Caption
- **Problem Found:** Requested "Meme style" post returned standard formal paragraph instead of funny punchlines.
- **Possible Reason:** Small 4B parameters LLM defaults to polite assistant tone unless tone instructions are strict.
- **Fix Applied:** Added tone guidelines in `get_caption_prompt` and `get_reel_script_prompt` emphasizing visual contrast (Expectation vs Reality).

### Scenario 3: Reel Script Exceeded Time Limit
- **Problem Found:** Generated script contained 8 long scenes (~90 seconds instead of ~30 seconds).
- **Possible Reason:** Prompt did not mandate exact scene count or duration constraints.
- **Fix Applied:** Enforced strict 4-scene structure (0-5s, 5-15s, 15-25s, 25-30s) in `get_reel_script_prompt`.

### Scenario 4: Irrelevant/Generic Hashtags
- **Problem Found:** Output returned broad generic hashtags (`#Post #Content #Update`) instead of domain-specific tags.
- **Possible Reason:** LLM generated tags in prose rather than list format.
- **Fix Applied:** Refactored `hashtag_generator` tool in `app/tools.py` to filter tags using regex pattern `r"#\w+"` and provide domain-aware fallbacks if needed.

### Scenario 5: Windows Filename Characters Exception
- **Problem Found:** Topic containing slashes or quotes (e.g. `CI/CD & Docker: "Best Practices"`) crashed `File Saver` with invalid path syntax.
- **Possible Reason:** Raw topic string passed to `open(path, 'w')`.
- **Fix Applied:** Added `slugify` sanitization in `file_saver` tool using `re.sub(r"[^\w\s-]", "", topic)` to ensure safe cross-platform file paths.

---

## 🚀 Proposed Future Improvements

1. **Structured Output Schemas (Pydantic / Instructor):**
   - Enforce JSON schemas on Ollama calls to ensure deterministic tool responses without regex fallback parsing.

2. **Automated Content Validation Checks:**
   - Add rule-based post-validation (e.g. character count check for X/Twitter tweets, hashtag quantity validation).

3. **Multi-Turn User Feedback Loop:**
   - Allow user in `demo.py` to review initial output and request instant targeted rewrites (e.g., "Make it shorter", "Add more emojis").
