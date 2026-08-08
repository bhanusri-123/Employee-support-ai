import json
import uuid


def create_ticket(employee, tickets):

    ticket = {
        "ticket_id": str(uuid.uuid4())[:8],
        "employee_id": employee["employee_id"],
        "title": "General Support Request",
        "status": "Open"
    }

    tickets.append(ticket)

    return {
        "status": "success",
        "tool": "create_ticket",
        "ticket": ticket
    }


def list_tickets(employee, tickets):

    employee_tickets = [
        t for t in tickets
        if t["employee_id"] == employee["employee_id"]
    ]

    return {
        "status": "success",
        "tool": "list_tickets",
        "tickets": employee_tickets
    }