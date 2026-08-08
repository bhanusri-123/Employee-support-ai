"""
Leave Service
"""

from utils.data_loader import load_json, save_json


def get_leave_balance(employee_id):
    """
    Return leave balance for an employee.
    """

    leave_data = load_json("leave.json")

    for employee in leave_data:

        if employee["employee_id"] == employee_id:

            return employee

    return None


def apply_leave(employee_id, leave_type, days):
    """
    Apply leave and update leave.json.
    """

    leave_data = load_json("leave.json")

    for employee in leave_data:

        if employee["employee_id"] == employee_id:

            if employee[leave_type] >= days:

                employee[leave_type] -= days

                save_json(
                    "leave.json",
                    leave_data
                )

                return True

            return False

    return False