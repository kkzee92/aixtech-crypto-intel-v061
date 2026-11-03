from crypto_intel.strategies.asset_class import score_signal

def test_score_stress():
    assert score_signal("major", "stress", {}) == 0.0

def test_score_basic():
    s = score_signal("major", "trend", {"strength": 0.8, "vol_tier": 0.3})
    assert 0 < s <= 0.08
