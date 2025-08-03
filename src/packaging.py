from __future__ import annotations

"""Utility functions for packaging and deploying the application."""

from pathlib import Path
from typing import List


def build_android(output_dir: str) -> Path:
    """Pretend to build an Android package by creating a placeholder file."""
    path = Path(output_dir) / "app-android.apk"
    path.write_text("android build placeholder")
    return path


def build_ios(output_dir: str) -> Path:
    """Pretend to build an iOS package by creating a placeholder file."""
    path = Path(output_dir) / "app-ios.ipa"
    path.write_text("ios build placeholder")
    return path


def beta_release(files: List[Path]) -> List[Path]:
    """Collect build artifacts for beta distribution."""
    # In a real project this would upload to TestFlight, Firebase, etc.
    return files
