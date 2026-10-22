"""Render certificate files to web-sized JPGs for the certificates page.

Run locally (the source folder is not in the repo):  python export_certs.py
Slugs must match the CERTS list in build.py.
"""

from pathlib import Path

import fitz  # PyMuPDF
from PIL import Image

SRC = Path(r"C:\Me\Aymane\4-Certificates")
OUT = Path(__file__).parent / "certificates" / "img"
WIDTH = 1000

SOURCES = {
    "cisco-cybersecurity": "Cisco CyberSecurity Intro/Certificate.pdf",
    "higgsfield-filmmaking": "Higgsfield/THE AI FILMMAKING PIPELINE HIGGSFIELD.png",
    "alx-professional-foundations": "2-ALX Program/Data Analytics/Certificates/Professional Foundations.png",
    "anthropic-agent-skills": "1-Claude/Introduction to agent skills.pdf",
    "anthropic-claude-code": "1-Claude/Claude Code in Action.pdf",
    "kodekloud-aws": "KodeCloud/Crash Course AWS Basics.pdf",
    "365-git-github": "Data Science 365/Git & Github/Certificate.pdf",
    "365-chatgpt-sql": "Data Science 365/ChaGPT for SQL/Certificate.pdf",
    "google-ai-essentials": "Google Career Essentials - AI/Google AI Essentials Certificate.pdf",
    "365-data-analysis-chatgpt": "Data Science 365/Data Analysis with ChatGPT/Certificate.jpg",
    "datacamp-understanding-ds": "DataCamp/Undestanding Data Science/Undestanding Data Science.pdf",
    "datacamp-ai-fundamentals": "DataCamp/AI Fundamentals/AI Fundamentals.jpg",
    "alx-ai-career-essentials": "2-ALX Program/xCertificatesx/AiCE Certificate.png",
    "udemy-illustrator": "Udemy/Illustrator/UC-c4046809-ad0d-4c4f-ac72-a07e82c4d784.jpg",
    "udemy-photoshop": "Udemy/Photoshop/UC-ca4f5dd0-7a26-4ed1-9bd5-1b3168511c35.jpg",
    "udemy-canva": "Udemy/Instagram Post/UC-91471415-ab04-40b6-a5a8-aa9b4e4fb4a9.jpg",
}


def load(path):
    if path.suffix.lower() == ".pdf":
        page = fitz.open(path)[0]
        zoom = WIDTH * 2 / page.rect.width  # some PDFs have huge page sizes
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    return Image.open(path).convert("RGB")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, rel in SOURCES.items():
        img = load(SRC / rel)
        img.thumbnail((WIDTH, WIDTH * 2), Image.LANCZOS)
        img.save(OUT / f"{slug}.jpg", quality=84, optimize=True, progressive=True)
        print(f"{slug}: {img.width}x{img.height}")


if __name__ == "__main__":
    main()
