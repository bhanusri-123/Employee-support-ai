from chatbot.intent_router import IntentRouter
from utils.data_loader import load_json

employee = load_json("employees.json")[0]
tickets = load_json("tickets.json")

policies = {
    "leave_policy": open("data/policies/leave_policy.txt").read(),
    "wfh_policy": open("data/policies/wfh_policy.txt").read(),
    "office_policy": open("data/policies/office_policy.txt").read(),
    "travel_policy": open("data/policies/travel_policy.txt").read(),
    "insurance_policy": open("data/policies/insurance_policy.txt").read()
}

router = IntentRouter(
    employee,
    tickets,
    policies
)

sample_intents = [
    {"intent": "password_reset"},
    {"intent": "leave_balance"},
    {"intent": "employee_profile"}
]

results = router.execute(sample_intents)

for result in results:
    print(result)