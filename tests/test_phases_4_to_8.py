import sys
from pathlib import Path

# Ensure src package is importable
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src import (
    EncounterSetupPanel,
    Entity,
    CombatControlBar,
    EntityDetailPanel,
    EntityList,
    ServerDiscoveryScreen,
    PlayerTurnView,
    HealthBar,
    TabbedView,
    build_android,
    build_ios,
)


def sample_entity(entity_id: str = "e1", name: str = "Goblin") -> Entity:
    return Entity(
        id=entity_id,
        name=name,
        type="npc",
        owner_id=None,
        hp=10,
        max_hp=10,
        conditions=[],
        fatigue=0,
        initiative=None,
        notes="",
    )


def test_combat_control_bar_lifecycle():
    panel = EncounterSetupPanel(name="Test")
    ent = sample_entity()
    panel.add_entity(ent)
    encounter = panel.build_encounter()
    entity_list = EntityList([ent])
    detail = EntityDetailPanel(ent)
    detail.apply_damage(5)
    assert ent.hp == 5
    detail.heal(5)
    assert ent.hp == 10

    cc = CombatControlBar(encounter, entity_list)
    cc.start()
    assert cc.status == "running" and encounter.is_active
    cc.pause()
    assert cc.status == "paused"
    cc.end()
    assert cc.status == "stopped" and not encounter.is_active


def test_player_turn_view_and_discovery():
    screen = ServerDiscoveryScreen()
    screen.update_servers([{"name": "s1", "address": "127.0.0.1"}])
    screen.select(0)
    assert screen.selected["name"] == "s1"

    entity = sample_entity("player1", "Hero")
    turn_view = PlayerTurnView(entity)
    msg = turn_view.notify_turn()
    assert entity.name in msg and turn_view.is_active
    turn_view.end_turn()
    assert not turn_view.is_active


def test_shared_ui_and_packaging(tmp_path):
    entity = sample_entity()
    hb = HealthBar(entity)
    assert hb.ratio() == 1.0

    tabs = TabbedView(["a", "b"])
    tabs.switch(1)
    assert tabs.active == 1
    tabs.toggle_dark_mode()
    assert tabs.dark_mode

    android = build_android(tmp_path)
    ios = build_ios(tmp_path)
    assert android.exists() and ios.exists()
