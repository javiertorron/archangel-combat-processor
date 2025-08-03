from __future__ import annotations

"""Shared UI utilities and components for both DM and player interfaces."""

from dataclasses import dataclass, field
from typing import List

from .models import Entity, Condition


@dataclass
class HealthBar:
    """Represents the HP bar of an entity."""

    entity: Entity

    def ratio(self) -> float:
        if self.entity.max_hp == 0:
            return 0.0
        return self.entity.hp / self.entity.max_hp


@dataclass
class ConditionBadge:
    """Shows a compact representation of conditions."""

    condition: Condition

    def label(self) -> str:
        return f"{self.condition.name} ({self.condition.duration_type})"


@dataclass
class RollIndicator:
    """Marks when automatic rolls (e.g., saving throws) occur."""

    rolls: List[int] = field(default_factory=list)

    def add_roll(self, value: int) -> None:
        self.rolls.append(value)

    def last_roll(self) -> int:
        return self.rolls[-1]


@dataclass
class TabbedView:
    """Simple container that switches between views."""

    tabs: List[str]
    active: int = 0
    dark_mode: bool = False

    def switch(self, index: int) -> None:
        if 0 <= index < len(self.tabs):
            self.active = index

    def toggle_dark_mode(self) -> None:
        self.dark_mode = not self.dark_mode
