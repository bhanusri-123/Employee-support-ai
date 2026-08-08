from tools.password_tool import (
    reset_password,
    unlock_account
)

from tools.ticket_tool import (
    create_ticket,
    list_tickets
)

from tools.leave_tool import (
    get_leave_balance_tool,
    apply_leave_tool
)

from tools.profile_tool import (
    get_employee_profile
)

from tools.policy_tool import (
    get_policy
)

from tools.greeting_tool import (
    greet
)
from tools.goodbye_tool import (
    goodbye
)

class IntentRouter:

    def __init__(
        self,
        employee,
        tickets,
        policies,
        query=""
    ):

        self.employee = employee
        self.tickets = tickets
        self.policies = policies
        self.query = query

        self.registry = {

            "greeting":
                lambda: greet(),

            "goodbye":
                 lambda: goodbye(),

            "password_reset":
                lambda: reset_password(
                    self.employee
                ),

            "account_unlock":
                lambda: unlock_account(
                    self.employee
                ),

            "create_ticket":
                lambda: create_ticket(
                    self.employee,
                    self.tickets
                ),

            "list_tickets":
                lambda: list_tickets(
                    self.employee,
                    self.tickets
                ),

            "leave_balance":
                lambda: get_leave_balance_tool(
                    self.employee
                ),

            "apply_leave":
                lambda: apply_leave_tool(
                    self.employee,
                    self.query
                ),

            "employee_profile":
                lambda: get_employee_profile(
                    self.employee
                ),

            "policy_query":
                lambda: get_policy(
                    self.query,
                    self.policies
                )
            

        }

    def execute(
        self,
        detected_intents
    ):

        results = []

        for item in detected_intents:

            intent = item["intent"]

            tool = self.registry.get(intent)

            if tool is None:

                continue

            try:

                results.append(
                    tool()
                )

            except Exception as e:

                results.append({

                    "status": "failed",

                    "tool": intent,

                    "message": str(e)

                })

        return results