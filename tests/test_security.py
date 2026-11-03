from crypto_intel.security.redact import redact
from crypto_intel.security.audit import seal

def test_redact():
    assert "[REDACTED]" in redact("ghp_abcdefghijklmnopqrstuvwxyz123456")

def test_seal():
    s = seal("test")
    assert s["sealed"] and "sha256" in s
