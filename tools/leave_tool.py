"""
Leave Tool
"""

import re

from services.leave_service import (
    get_leave_balance,
    apply_leave
)


def get_leave_balance_tool(employee):

    leave = get_leave_balance(
        employee["employee_id"]
    )

    return {

        "status": "success",

        "tool": "leave_balance",

        "leave_details": leave

    }


def apply_leave_tool(employee, query):

    query = query.lower()

    # -----------------------------
    # Detect leave type
    # -----------------------------

    leave_type = "annual_leave"

    if "sick" in query:

        leave_type = "sick_leave"

    elif "casual" in query:

        leave_type = "casual_leave"

    elif "annual" in query:

        leave_type = "annual_leave"

    # -----------------------------
    # Detect number of days
    # -----------------------------

    match = re.search(r"(\d+)", query)

    days = int(match.group(1)) if match else 1

    success = apply_leave(

        employee["employee_id"],

        leave_type,

        days

    )

    if success:

        leave_name = leave_type.replace("_", " ")

        if days == 1:

            message = (
                f"✅ Your {leave_name} request has been submitted successfully."
            )

        else:

            message = (
                f"✅ Your {leave_name} request for {days} days has been submitted successfully."
            )

        return {

            "status": "success",

            "tool": "apply_leave",
 
            "message": message

        }

    return {

        "status": "failed",

        "tool": "apply_leave",

        "message": f"❌ Insufficient {leave_type.replace('_', ' ')} balance."

    }