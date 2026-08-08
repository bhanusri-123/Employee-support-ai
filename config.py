import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
CURRENT_EMPLOYEE_ID = "EMP001"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

llm = ChatGoogleGenerativeAI(
    model = os.getenv("MODEL_NAME", "gemini-3.5-flash"),
    #temperature = 0
)
DEBUG = True



# ==========================================
# Rule-Based Intent Detection Configuration
# ==========================================

PRIMARY_KEYWORD_SCORE = 2
SECONDARY_KEYWORD_SCORE = 1


# Used later by the Hybrid detector
RULE_BASED_THRESHOLD = 0.80

# ==========================================
# Hybrid Intent Detection Configuration
# ==========================================

# Minimum score required to trust Rule-Based detection.
# If the highest score is below this value,
# the Hybrid classifier will use Gemini.

RULE_BASED_SCORE_THRESHOLD = 2

# Supported intents
SUPPORTED_INTENTS = [

    "password_reset",

    "account_unlock",

    "create_ticket",

    "list_tickets",

    "leave_balance",

    "apply_leave",

    "employee_profile",

    "policy_query",

    "greeting",

    "goodbye",

    "unknown"
]