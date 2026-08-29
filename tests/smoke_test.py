from jarvis_xxii.health import check

def test_health():
    assert check()["status"] == "healthy"
