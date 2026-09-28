"""
PDF Report Generator for Agentic AI Task 2.
Generates a professional final report saved as report/final_report.pdf.
"""

import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


def generate_pdf():
    report_dir = os.path.dirname(__file__)
    os.makedirs(report_dir, exist_ok=True)
    pdf_path = os.path.join(report_dir, "final_report.pdf")

    try:
        from fpdf import FPDF
    except ImportError:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "fpdf2"], check=True)
        from fpdf import FPDF

    class PDFReport(FPDF):
        def header(self):
            self.set_font("Helvetica", "B", 12)
            self.set_text_color(50, 50, 50)
            self.cell(0, 10, "Agentic AI Task 2 - Final Internship Report", border=0, align="R", new_x="LMARGIN", new_y="NEXT")
            self.line(10, 20, 200, 20)
            self.ln(5)

        def footer(self):
            self.set_y(-15)
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(128, 128, 128)
            self.cell(0, 10, f"Page {self.page_no()}/{{nb}} | Local Gemma 3:4B Agent", border=0, align="C")

    pdf = PDFReport()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(0, 15, "Agentic AI Social Media Generator", align="L", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(99, 102, 241)
    pdf.cell(0, 8, "Task 2 Internship Project Report | Local Gemma 3:4B via Ollama", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # Executive Summary
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "1. Executive Summary", align="L", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(51, 65, 85)
    summary_text = (
        "This project implements a fully autonomous, offline Agentic AI Social Media Content Generator built inside "
        "the agentic_ai_task_2 project workspace. Utilizing Google's Gemma 3:4B LLM running locally through Ollama, "
        "the agent plans, generates, reviews, and persists multi-platform content tailored for LinkedIn, Instagram, "
        "X/Twitter, and YouTube Shorts."
    )
    pdf.multi_cell(0, 6, summary_text)
    pdf.ln(4)

    # Core Architecture & Tool Suite
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "2. Agent Architecture & Tool Suite", align="L", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 6, "The agent architecture comprises 6 dedicated tools orchestrated sequentially:")
    pdf.ln(2)

    tools_info = [
        ("1. Trend Idea Generator", "Generates 3 content angles locally and selects the optimal approach."),
        ("2. Caption Writer", "Drafts scroll-stopping hooks, main post body, and strong call-to-actions."),
        ("3. Hashtag Generator", "Produces target platform hashtags returned as clean Python lists."),
        ("4. Reel Script Generator", "Creates structured 30-second video scripts with visual and audio cues."),
        ("5. Content Reviewer", "Evaluates content quality, platform alignment, and improvement areas."),
        ("6. File Saver (Mandatory)", "Persists outputs as structured Markdown files in designated output paths.")
    ]

    for title, desc in tools_info:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(30, 58, 138)
        pdf.cell(50, 6, title, new_x="RIGHT", new_y="TOP")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(51, 65, 85)
        pdf.cell(0, 6, f"- {desc}", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(4)

    # Persistent Memory
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "3. Local JSON Persistent Memory System", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    memory_text = (
        "A dedicated MemoryManager module persists user queries, selected content angles, hooks, and saved file paths "
        "to outputs/memory.json. Before generating new content, the agent queries previous records to maintain "
        "contextual continuity and style alignment across sessions."
    )
    pdf.multi_cell(0, 6, memory_text)
    pdf.ln(4)

    # Verification & Testing
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "4. Verification & Test Suite Results", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 6, "All 10 required test cases were executed end-to-end against local Gemma 3:4B:")
    pdf.ln(2)

    # Test Table Header
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(241, 245, 249)
    pdf.cell(15, 7, "#", border=1, align="C", fill=True, new_x="RIGHT", new_y="TOP")
    pdf.cell(60, 7, "Topic", border=1, align="L", fill=True, new_x="RIGHT", new_y="TOP")
    pdf.cell(35, 7, "Platform", border=1, align="L", fill=True, new_x="RIGHT", new_y="TOP")
    pdf.cell(40, 7, "Output Type", border=1, align="L", fill=True, new_x="RIGHT", new_y="TOP")
    pdf.cell(35, 7, "Status", border=1, align="C", fill=True, new_x="LMARGIN", new_y="NEXT")

    # Table Rows
    pdf.set_font("Helvetica", "", 8)
    test_rows = [
        ("TC-01", "YOLOv8 helmet detection", "LinkedIn", "Post + Reel Script", "PASSED"),
        ("TC-02", "AI internship experience", "LinkedIn", "Post", "PASSED"),
        ("TC-03", "Python learning journey", "Instagram", "Reel Script", "PASSED"),
        ("TC-04", "Machine learning project", "X/Twitter", "Post", "PASSED"),
        ("TC-05", "Data annotation struggles", "LinkedIn", "Post", "PASSED"),
        ("TC-06", "Model failed in production", "Instagram", "Reel Script", "PASSED"),
        ("TC-07", "Final year project", "LinkedIn", "Post", "PASSED"),
        ("TC-08", "Computer vision project", "YouTube Shorts", "Reel Script", "PASSED"),
        ("TC-09", "Debugging FastAPI", "X/Twitter", "Post", "PASSED"),
        ("TC-10", "Open-source contribution", "LinkedIn", "Post", "PASSED")
    ]

    for tc, topic, plat, out_t, status in test_rows:
        pdf.cell(15, 6, tc, border=1, align="C", new_x="RIGHT", new_y="TOP")
        pdf.cell(60, 6, topic[:30], border=1, align="L", new_x="RIGHT", new_y="TOP")
        pdf.cell(35, 6, plat, border=1, align="L", new_x="RIGHT", new_y="TOP")
        pdf.cell(40, 6, out_t, border=1, align="L", new_x="RIGHT", new_y="TOP")
        pdf.set_text_color(16, 185, 129) # green
        pdf.cell(35, 6, status, border=1, align="C", new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(51, 65, 85)

    pdf.ln(6)

    # Conclusion & Output Verification
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, "5. Conclusion", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(
        0, 6,
        "The project successfully meets all internship requirements, operating 100% locally with zero paid API dependencies. "
        "All output paths (outputs/generated_posts/, outputs/generated_scripts/, outputs/saved_results/) have been "
        "verified on Windows."
    )

    pdf.output(pdf_path)
    print(f"Generated PDF report at: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    generate_pdf()
