from config import CURRENT_EMPLOYEE_ID
from utils.data_loader import load_json
from utils.response import success_response, error_response


def get_employee():
    """
    Return the currently logged-in employee.
    """
    employees = load_json("employees.json")

    for employee in employees:
        if employee["employee_id"] == CURRENT_EMPLOYEE_ID:
            return employee

    return None


def get_employee_profile():
    """
    Return the profile of the currently logged-in employee.
    """

    employee = get_employee()

    if employee is None:
        return error_response("Employee not found.")

    return success_response(
        tool="EmployeeProfileTool",
        message="Employee profile retrieved successfully.",
        data=employee
    )


def reset_password():
    """
    Simulate password reset.
    """

    employee = get_employee()

    if employee is None:
        return error_response("Employee not found.")

    return success_response(
        tool="PasswordResetTool",
        message=(
            f"Password reset successful for {employee['name']}. "
            "A temporary password has been sent to your registered email."
        ),
        data={
            "employee_id": employee["employee_id"],
            "employee_name": employee["name"]
        }
    )


def unlock_account():
    """
    Simulate account unlock.
    """

    employee = get_employee()

    if employee is None:
        return error_response("Employee not found.")

    return success_response(
        tool="AccountUnlockTool",
        message=f"{employee['name']}'s account has been unlocked successfully.",
        data={
            "employee_id": employee["employee_id"],
            "employee_name": employee["name"]
        }
    )