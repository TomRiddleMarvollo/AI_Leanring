#!/usr/bin/env python3
"""Standalone entrypoint for the AI Learning Hub data-refresh pipeline.

Runs the same fetch-and-summarize logic as the "Cập nhật DL" button
(agent.run_all_background_tasks), but as an independent process instead
of a FastAPI background task tied to a web request. This means it can
be scheduled with cron / a CI job, run without the API server up at
all, and its logs/exit code inspected directly — instead of being lost
the moment the request that triggered it finishes.

Usage:
    python update_data.py
"""
import sys
import time

from agent import run_all_background_tasks


def main() -> int:
    started = time.monotonic()
    print("=== AI Learning Hub: data refresh started ===")
    try:
        run_all_background_tasks()
    except Exception as exc:
        print(f"Data refresh failed: {exc}", file=sys.stderr)
        return 1
    elapsed = time.monotonic() - started
    print(f"=== Data refresh finished in {elapsed:.1f}s ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
