"""
Functionality that needs to happen on startup.
"""

import backend.config as cfg

from langchain_groq import ChatGroq

def _setup_dirs():
    return PlatformDirs("Mini-Bankruptcy", appauthor=False, ensure_exists=True)

def _setup_llm():
    return ChatGroq(
            model="llama-3.1-8b-instant"
        )

def setup():
    cfg.USER_DIRS = _setup_dirs()
    cfg.LLM = _setup_llm()















