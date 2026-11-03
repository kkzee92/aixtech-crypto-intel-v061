"""Expanded redaction patterns for zero-trust. Research only. v0.61"""
import re

PATTERNS = [
    re.compile(r"\b(?:[a-z]{3,8}\s+){11,24}[a-z]{3,8}\b", re.I),  # BIP39-like
    re.compile(r"5[HJK][1-9A-HJ-NP-Za-km-z]{49,50}"),  # WIF
    re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),  # AWS
    re.compile(r"ghp_[A-Za-z0-9]{36}"),  # GitHub PAT
    re.compile(r"[1-9A-HJ-NP-Za-km-z]{32,44}"),  # Solana-like base58
    re.compile(r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"),  # JWT
    re.compile(r"[0-9a-fA-F]{64}"),  # hex private key
    re.compile(r"[A-Za-z0-9_-]{40,}"),  # high entropy / bot tokens proxy
    # Exchange key patterns (research proxies)
    re.compile(r"binance[_-]?api[_-]?key", re.I),
    re.compile(r"bybit[_-]?secret", re.I),
]

def redact(text: str) -> str:
    for p in PATTERNS:
        text = p.sub("[REDACTED]", text)
    return text
