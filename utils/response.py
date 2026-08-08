def success_response(tool, message, data=None):
    """
    Create a standardized success response.
    """
    return {
        "success": True,
        "tool": tool,
        "data": data or {},
        "message": message
    }


def error_response(message, tool=None):
    """
    Create a standardized error response.
    """
    return {
        "success": False,
        "tool": tool,
        "data": {},
        "message": message
    }