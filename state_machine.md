# ⚙️ State Machine — D&D 5e Combat Manager

Este documento describe los estados principales del sistema y sus transiciones.

## Estados

- `idle`: no hay encuentro cargado.
- `setup`: el DJ prepara entidades y configuraciones.
- `awaiting_players`: esperando a que los jugadores se conecten y sean aprobados.
- `initiative`: recopilando tiradas de iniciativa.
- `in_progress`: el combate se está desarrollando.
- `paused`: el combate está temporalmente detenido.
- `completed`: el encuentro ha finalizado.

## Transiciones

| Desde | Evento | Hacia | Descripción |
|-------|--------|-------|-------------|
| `idle` | `load_encounter` | `setup` | El DJ crea o carga un encuentro. |
| `setup` | `start_server` | `awaiting_players` | El servidor queda disponible para conexiones. |
| `awaiting_players` | `all_players_ready` | `initiative` | Todos los jugadores se han unido y están listos. |
| `initiative` | `initiatives_submitted` | `in_progress` | Se determina el orden de iniciativa. |
| `in_progress` | `pause_requested` | `paused` | El DJ pausa el combate. |
| `paused` | `resume_requested` | `in_progress` | Se reanuda el combate. |
| `in_progress` | `encounter_finished` | `completed` | El DJ termina el combate. |
| `completed` | `reset` | `idle` | El sistema vuelve al estado inicial. |

Este diagrama de estados debe mantenerse alineado con el motor de combate y los contratos de red.
