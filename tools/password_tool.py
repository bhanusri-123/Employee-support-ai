from datetime import datetime


def reset_password(employee):

    return {
        "status": "success",
        "tool": "password_reset",
        "employee_id": employee["employee_id"],
        "temporary_password": "Temp@123",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def unlock_account(employee):

    return {
        "status": "success",
        "tool": "account_unlock",
        "employee_id": employee["employee_id"],
        "message": "Account unlocked successfully."
    }