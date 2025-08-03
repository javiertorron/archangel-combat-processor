from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any


@dataclass
class Condition:
    id: str
    name: str
    description: str
    duration_type: str  # "manual" | "turns"
    remaining_turns: Optional[int] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Condition":
        return Condition(**data)


@dataclass
class EventLog:
    timestamp: int
    event_type: str
    description: str
    entity_id: Optional[str] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "EventLog":
        return EventLog(**data)


@dataclass
class Entity:
    id: str
    name: str
    type: str  # "player" | "npc"
    owner_id: Optional[str]
    hp: int
    max_hp: int
    conditions: List[Condition] = field(default_factory=list)
    fatigue: int = 0
    initiative: Optional[int] = None
    death_saves: Dict[str, int] = field(default_factory=lambda: {"successes": 0, "failures": 0})
    notes: str = ""

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Entity":
        data = data.copy()
        data["conditions"] = [Condition.from_dict(c) for c in data.get("conditions", [])]
        return Entity(**data)


@dataclass
class Player:
    id: str
    name: str
    connected_entity_id: str
    connection_status: str
    is_turn: bool

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Player":
        return Player(**data)


@dataclass
class ConnectionInfo:
    player_id: str
    ip_address: str
    last_ping: int
    status: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ConnectionInfo":
        return ConnectionInfo(**data)


@dataclass
class Encounter:
    id: str
    name: str
    participants: List[Entity]
    initiative_order: List[str]
    current_turn_index: int
    is_active: bool
    history: List[EventLog] = field(default_factory=list)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Encounter":
        data = data.copy()
        data["participants"] = [Entity.from_dict(e) for e in data.get("participants", [])]
        data["history"] = [EventLog.from_dict(e) for e in data.get("history", [])]
        return Encounter(**data)


@dataclass
class ServerState:
    encounter: Encounter
    players: List[Player]
    connections: List[ConnectionInfo]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ServerState":
        data = data.copy()
        data["encounter"] = Encounter.from_dict(data["encounter"])
        data["players"] = [Player.from_dict(p) for p in data.get("players", [])]
        data["connections"] = [ConnectionInfo.from_dict(c) for c in data.get("connections", [])]
        return ServerState(**data)


def to_dict(obj: Any) -> Dict[str, Any]:
    """Convert a dataclass instance to a serializable dictionary."""
    return asdict(obj)
