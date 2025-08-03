from __future__ import annotations

import json
from pathlib import Path
from typing import List, Union

from .models import Encounter, to_dict


def save_encounter(encounter: Encounter, path: Union[str, Path]) -> None:
    """Save an encounter to a JSON file."""
    data = to_dict(encounter)
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False))


def load_encounter(path: Union[str, Path]) -> Encounter:
    """Load an encounter from a JSON file."""
    content = Path(path).read_text()
    data = json.loads(content)
    return Encounter.from_dict(data)


class EncounterRepository:
    """Manage a collection of encounters stored as JSON files.

    Each encounter is stored in its own file inside ``base_path`` using
    the encounter's ``id`` as filename. The repository offers helpers to
    save, load, list and delete encounters without exposing file-system
    details to callers.
    """

    def __init__(self, base_path: Union[str, Path]) -> None:
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # CRUD operations
    # ------------------------------------------------------------------
    def save(self, encounter: Encounter) -> Path:
        """Persist ``encounter`` under ``base_path``.

        Returns the path of the written file.
        """

        file_path = self.base_path / f"{encounter.id}.json"
        save_encounter(encounter, file_path)
        return file_path

    def load(self, encounter_id: str) -> Encounter:
        """Load an encounter by ``encounter_id`` from ``base_path``."""

        file_path = self.base_path / f"{encounter_id}.json"
        return load_encounter(file_path)

    def list_ids(self) -> List[str]:
        """Return the list of available encounter identifiers."""

        return [p.stem for p in self.base_path.glob("*.json")]

    def delete(self, encounter_id: str) -> None:
        """Remove the stored encounter if it exists."""

        file_path = self.base_path / f"{encounter_id}.json"
        if file_path.exists():
            file_path.unlink()
