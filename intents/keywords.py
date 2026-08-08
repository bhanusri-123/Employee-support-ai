"""
Keyword definitions for Rule-Based Intent Detection.

Each intent contains:

Primary Keywords:
    Highly indicative phrases.
    Score = PRIMARY_KEYWORD_SCORE

Secondary Keywords:
    Supporting keywords.
    Score = SECONDARY_KEYWORD_SCORE
"""

INTENT_KEYWORDS = {

    "password_reset": {

        "primary": [
            "forgot password",
            "reset password",
            "recover password",
            "password reset"
        ],

        "secondary": [
            "password",
            "change password",
            "new password"
        ]
    },

    "account_unlock": {

        "primary": [
            "unlock account",
            "account locked",
            "locked account"
        ],

        "secondary": [
            "unlock",
            "cannot login",
            "can't login",
            "unable to login",
            "login issue",
            "access my account"
        ]
    },

    "create_ticket": {

        "primary": [
            "create ticket",
            "raise ticket",
            "open ticket",
            "report issue"
        ],

        "secondary": [
            "problem",
            "issue",
            "bug",
            "error",
            "not working",
            "technical issue"
        ]
    },

    "list_tickets": {

        "primary": [
            "show my tickets",
            "view my tickets",
            "list tickets"
        ],

        "secondary": [
            "ticket status",
            "support tickets",
            "my tickets",
            "open tickets"
        ]
    },

    "leave_balance": {

        "primary": [
            "leave balance",
            "remaining leave",
            "available leave"
        ],

        "secondary": [
            "leave remaining",
            "leave left",
            "how many leave"
        ]
    },

    "apply_leave": {

        "primary": [
            "apply leave",
            "request leave",
            "leave application"
        ],

        "secondary": [
            "vacation",
            "day off",
            "take leave"
        ]
    },

    "employee_profile": {

        "primary": [
            "my profile",
            "employee profile",
            "employee details"
        ],

        "secondary": [
            "my details",
            "manager",
            "department",
            "designation",
            "email address",
            "contact details"
        ]
    },

    "policy_query": {

        "primary": [
            "leave policy",
            "wfh policy",
            "work from home",
            "insurance policy",
            "travel policy",
            "office policy"
        ],

        "secondary": [
            "policy",
            "insurance",
            "company policy",
            "rules"
        ]
    },

    "greeting": {

    "primary": [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ],

    "secondary": []
    },

    "goodbye": {

    "primary": [
        "bye",
        "goodbye",
        "see you later",
        "see ya",
        "take care",
        "catch you later",
        "thank you",
        "thanks",
        "see you"
    ],

    "secondary": []
    }
}