from __future__ import annotations

import json
from pathlib import Path
from typing import Union

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
