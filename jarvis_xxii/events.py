"""Simple event representation."""
from dataclasses import dataclass
@dataclass
class Event:
    name: str
    payload: dict
