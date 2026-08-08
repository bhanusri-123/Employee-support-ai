"""
Formats tool outputs into chatbot responses.
"""


def format_response(results):

    responses = []

    for result in results:

        tool = result.get("tool")

        # -------------------------------------------------
        # Greeting
        # -------------------------------------------------

        if tool == "greeting":

            responses.append(
                result["message"]
            )

        # -------------------------------------------------
        # Password Reset
        # -------------------------------------------------

        elif tool == "password_reset":

            responses.append(
                f"""✅ Password reset successful.

Temporary Password: **{result["temporary_password"]}**
"""
            )

        # -------------------------------------------------
        # Account Unlock
        # -------------------------------------------------

        elif tool == "account_unlock":

            responses.append(
                "✅ Your account has been unlocked successfully."
            )

        # -------------------------------------------------
        # Leave Balance
        # -------------------------------------------------

        elif tool == "leave_balance":

            leave = result["leave_details"]

            responses.append(
f"""### Leave Balance

| Leave Type | Remaining |
|------------|-----------|
| Annual Leave | {leave["annual_leave"]} |
| Casual Leave | {leave["casual_leave"]} |
| Sick Leave | {leave["sick_leave"]} |
"""
            )

        # -------------------------------------------------
        # Apply Leave
        # -------------------------------------------------

        elif tool == "apply_leave":

            responses.append(
                result["message"]
            )

        # -------------------------------------------------
        # Employee Profile
        # -------------------------------------------------

        elif tool == "employee_profile":

            profile = result["profile"]

            responses.append(
f"""### 👤 Employee Profile

**Name:** {profile["name"]}

**Department:** {profile["department"]}

**Designation:** {profile["designation"]}

**Manager:** {profile["manager"]}

**Location:** {profile["location"]}
"""
            )

        # -------------------------------------------------
        # Ticket List
        # -------------------------------------------------

        elif tool == "list_tickets":

            tickets = result["tickets"]

            if not tickets:

                responses.append(
                    "No support tickets found."
                )

            else:

                text = "### 🎫 Your Tickets\n\n"

                text += "| Ticket ID | Status |\n"
                text += "|-----------|--------|\n"

                for ticket in tickets:

                    text += (
                        f'| {ticket["ticket_id"]} | {ticket["status"]} |\n'
                    )

                responses.append(text)

        # -------------------------------------------------
        # Create Ticket
        # -------------------------------------------------

        elif tool == "create_ticket":

            ticket = result["ticket"]

            responses.append(
f"""✅ Ticket created successfully.

**Ticket ID:** {ticket["ticket_id"]}
"""
            )

        # -------------------------------------------------
        # Policy Query
        # -------------------------------------------------

        elif tool == "policy_query":

            responses.append(
                result["policy_text"]
            )
        elif tool == "unknown":

            responses.append(
            result["message"]
            )
        elif tool == "goodbye":

            responses.append(
            result["message"]
            )

        # -------------------------------------------------
        # Default
        # -------------------------------------------------

        else:

           responses.append(

           result.get(

                "message",

                """Sorry, I couldn't understand your request.
Please try again or contact support for assistance."""
        )

    )
    return "\n\n".join(responses)