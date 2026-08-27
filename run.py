"""
ElewaSTEM One-Click Runner
Starts the FastAPI server on port 8000.
"""

import os
import sys
import webbrowser

# Ensure UTF-8 output encoding on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(PROJECT_DIR, "backend")

if __name__ == "__main__":
    print("=" * 60)
    print("ElewaSTEM -- Mwalimu wa Sayansi na Hesabu")
    print("Multilingual Adaptive AI STEM Tutor for African Children")
    print("=" * 60)
    print("Starting server on http://localhost:8000 ...")

    # Run uvicorn
    import uvicorn
    sys.path.insert(0, BACKEND_DIR)
    from app import app
    uvicorn.run(app, host="0.0.0.0", port=8000)
