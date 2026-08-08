from langchain_core.tools import tool

from services.employee_service import (
    reset_password,
    unlock_account,
    get_employee_profile
)


@tool
def reset_password_tool():
    """
    Reset the password for the currently logged-in employee.
    """
    return reset_password()


@tool
def unlock_account_tool():
    """
    Unlock the account for the currently logged-in employee.
    """
    return unlock_account()


@tool
def employee_profile_tool():
    """
    Retrieve the profile of the currently logged-in employee.
    """
    return get_employee_profile()