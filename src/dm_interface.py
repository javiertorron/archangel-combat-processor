from __future__ import annotations

"""Simplified Dungeon Master interface components for phase 4.

These classes provide minimal logic to manage encounters, entities,
initiative order and combat control. They are intentionally lightweight
so they can be unit tested without a graphical environment.
"""

from dataclasses import dataclass, field
from typing import List, Optional

from .models import Encounter, Entity, Condition


@dataclass
class EncounterSetupPanel:
    """Allows the DM to configure basic encounter information."""

    name: str = ""
    participants: List[Entity] = field(default_factory=list)

    def add_entity(self, entity: Entity) -> None:
        self.participants.append(entity)

    def remove_entity(self, entity_id: str) -> None:
        self.participants = [e for e in self.participants if e.id != entity_id]

    def build_encounter(self) -> Encounter:
        return Encounter(
            id=self.name.lower().replace(" ", "-"),
            name=self.name,
            participants=self.participants,
            initiative_order=[],
            current_turn_index=0,
            is_active=False,
        )


@dataclass
class EntityList:
    """Maintains a list of entities for quick lookup and updates."""

    entities: List[Entity]

    def get(self, entity_id: str) -> Optional[Entity]:
        for ent in self.entities:
            if ent.id == entity_id:
                return ent
        return None

    def update_hp(self, entity_id: str, hp: int) -> None:
        ent = self.get(entity_id)
        if ent:
            ent.hp = max(0, min(hp, ent.max_hp))


@dataclass
class InitiativeTimeline:
    """Handles initiative order and turn progression."""

    order: List[str]
    current_index: int = 0

    def next_turn(self) -> str:
        if not self.order:
            raise ValueError("initiative order is empty")
        self.current_index = (self.current_index + 1) % len(self.order)
        return self.order[self.current_index]


@dataclass
class EntityDetailPanel:
    """Offers utility methods to modify a specific entity."""

    entity: Entity

    def apply_damage(self, amount: int) -> None:
        self.entity.hp = max(0, self.entity.hp - amount)

    def heal(self, amount: int) -> None:
        self.entity.hp = min(self.entity.max_hp, self.entity.hp + amount)

    def add_condition(self, condition: Condition) -> None:
        self.entity.conditions.append(condition)

    def remove_condition(self, condition_id: str) -> None:
        self.entity.conditions = [c for c in self.entity.conditions if c.id != condition_id]


class CombatControlBar:
    """Controls encounter lifecycle and quick entity edits."""

    def __init__(self, encounter: Encounter, entity_list: EntityList) -> None:
        self.encounter = encounter
        self.entities = entity_list
        self.status = "stopped"  # "stopped" | "running" | "paused"

    def start(self) -> None:
        self.status = "running"
        self.encounter.is_active = True

    def pause(self) -> None:
        if self.status == "running":
            self.status = "paused"

    def end(self) -> None:
        self.status = "stopped"
        self.encounter.is_active = False

    def edit_hp(self, entity_id: str, hp: int) -> None:
        self.entities.update_hp(entity_id, hp)


@dataclass
class NotesPanel:
    """Stores free-form notes for the DM."""

    notes: str = ""

    def add_line(self, text: str) -> None:
        if self.notes:
            self.notes += "\n"
        self.notes += text
