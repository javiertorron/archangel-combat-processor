from __future__ import annotations

"""Minimal player-side interface components for phase 5.

These classes encapsulate behaviour expected by the player UI such as
server discovery, approval waiting and turn notifications. They are
framework agnostic and purely in-memory to keep the code testable.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional

from .models import Entity, Condition


@dataclass
class ServerDiscoveryScreen:
    """Stores the list of discovered servers and the selection."""

    servers: List[Dict[str, str]] = field(default_factory=list)
    selected: Optional[Dict[str, str]] = None

    def update_servers(self, discovered: List[Dict[str, str]]) -> None:
        self.servers = discovered

    def select(self, index: int) -> None:
        if 0 <= index < len(self.servers):
            self.selected = self.servers[index]


@dataclass
class AwaitingApprovalScreen:
    """Represents the waiting state before the DM approves a player."""

    approved: bool = False

    def approve(self) -> None:
        self.approved = True


@dataclass
class PlayerTurnView:
    """Tracks whether it is the player's turn and provides notifications."""

    entity: Entity
    is_active: bool = False

    def notify_turn(self) -> str:
        self.is_active = True
        return f"It is now {self.entity.name}'s turn!"

    def end_turn(self) -> None:
        self.is_active = False


@dataclass
class ConditionViewer:
    """Simple view over an entity's conditions."""

    entity: Entity

    def list_conditions(self) -> List[str]:
        return [c.name for c in self.entity.conditions]

    def has_condition(self, name: str) -> bool:
        return any(c.name == name for c in self.entity.conditions)
