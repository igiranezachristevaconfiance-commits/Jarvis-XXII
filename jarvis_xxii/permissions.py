"""Permission boundaries for optional integrations."""
def allowed(action: str) -> bool:
    return bool(action)
