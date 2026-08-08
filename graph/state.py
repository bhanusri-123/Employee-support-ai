from typing import TypedDict, List, Dict, Any


class ChatState(TypedDict):

    query: str

    intent_result: Dict[str, Any]

    tool_result: List[Dict[str, Any]]

    response: str

    method: str

    confidence: float

    intent: str

    response_time: float