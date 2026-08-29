"""JARVIS XXII component 1241; domain: core."""
from dataclasses import dataclass
from typing import Any

@dataclass(slots=True)
class State:
    enabled: bool = True

class Component:
    def __init__(self, state: State | None = None) -> None:
        self.state = state or State()

    def health(self) -> dict[str, Any]:
        return {"component": "component_1241", "domain": "core", "enabled": self.state.enabled}

    def process(self, payload: Any) -> dict[str, Any]:
        return {"status": "ok" if self.state.enabled else "disabled", "payload": payload}
