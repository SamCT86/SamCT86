#!/usr/bin/env python3
"""Fixture analyzer for Beat Claude Engineer 004.
Usage: python3 analyze_fixture.py path/to/event_sample.jsonl
Produces deterministic JSON on stdout and never mutates the input.
"""
import json, hashlib, sys
from datetime import datetime
from pathlib import Path
from collections import Counter

if len(sys.argv) != 2:
    raise SystemExit("usage: analyze_fixture.py <event_sample.jsonl>")
P = Path(sys.argv[1])
raw = P.read_bytes()
rows, parse_errors = [], []
for i, line in enumerate(raw.decode("utf-8").splitlines(), 1):
    try:
        rows.append((i, json.loads(line)))
    except Exception as exc:
        parse_errors.append({"line": i, "error": str(exc), "raw": line})

def dt(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        return None

ids = Counter(r.get("event_id") for _, r in rows if r.get("event_id"))
report = {
    "sha256": hashlib.sha256(raw).hexdigest(),
    "valid_rows": len(rows),
    "parse_errors": parse_errors,
    "duplicate_event_ids": {k: v for k, v in ids.items() if v > 1},
    "negative_event_to_receive_delta": [],
    "strong_future_clock_anomalies": [],
    "missing_tenant_ids": [],
    "schema_drift_event_ids": [],
    "pii_in_properties_event_ids": [],
    "bot_like_event_ids": [],
    "privacy_request_event_ids": [],
    "identity_events": [],
}
for _, r in rows:
    event_id = r.get("event_id")
    if r.get("tenant_id") is None:
        report["missing_tenant_ids"].append(event_id)
    ts, recv = dt(r.get("ts")), dt(r.get("received_at"))
    if ts and recv:
        delta = (recv - ts).total_seconds()
        if delta < 0:
            report["negative_event_to_receive_delta"].append({"event_id": event_id, "delta_s": delta})
        if delta < -3600:
            report["strong_future_clock_anomalies"].append({"event_id": event_id, "delta_s": delta})
    props = r.get("properties", {})
    if "timestamp" in r or r.get("type") == "pageview" or "page_path" in props or "ref" in props:
        report["schema_drift_event_ids"].append(event_id)
    if any(k in props for k in ("contact_email", "phone", "email", "telephone")):
        report["pii_in_properties_event_ids"].append(event_id)
    if "scanner" in json.dumps(props).lower():
        report["bot_like_event_ids"].append(event_id)
    if r.get("type") == "privacy_request":
        report["privacy_request_event_ids"].append(event_id)
    if r.get("type") == "identify":
        report["identity_events"].append({"event_id": event_id, "anonymous_id": r.get("anonymous_id"), "user_id": r.get("user_id")})
print(json.dumps(report, indent=2, sort_keys=True))
