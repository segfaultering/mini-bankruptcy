"""
Stores the global variables as well as constants for the program
"""

import os
from enum import StrEnum

from dotenv import load_dotenv


load_dotenv()

class ApiKeys(StrEnum):
    GROQ_API_KEY = os.environ["GROQ_API_KEY"]
    GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
















