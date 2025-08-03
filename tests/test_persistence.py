import sys
from pathlib import Path

# Ensure src package is importable
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.models import Encounter, Entity
from src.persistence import EncounterRepository, load_encounter, save_encounter


def build_encounter(enc_id: str) -> Encounter:
    return Encounter(
        id=enc_id,
        name="Test",
        participants=[
            Entity(
                id="e1",
                name="Goblin",
                type="npc",
                owner_id=None,
                hp=7,
                max_hp=7,
                conditions=[],
                fatigue=0,
                initiative=None,
                notes="",
            )
        ],
        initiative_order=[],
        current_turn_index=0,
        is_active=False,
    )


def test_save_and_load_roundtrip(tmp_path: Path) -> None:
    enc = build_encounter("enc1")
    file_path = tmp_path / "encounter.json"
    save_encounter(enc, file_path)
    loaded = load_encounter(file_path)
    assert loaded == enc


def test_repository_operations(tmp_path: Path) -> None:
    repo = EncounterRepository(tmp_path)
    enc1 = build_encounter("first")
    enc2 = build_encounter("second")

    repo.save(enc1)
    repo.save(enc2)

    assert set(repo.list_ids()) == {"first", "second"}

    loaded = repo.load("second")
    assert loaded == enc2

    repo.delete("first")
    assert repo.list_ids() == ["second"]
