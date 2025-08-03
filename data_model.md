# 🗃️ Modelo de Datos — D\&D 5e Combat Manager

Este documento describe las **entidades clave** del sistema y sus relaciones. Sirve como base para definir estructuras de datos, sincronización de estado y lógica de negocio durante el desarrollo.

---

## 🧙 Entidad: `Encounter` (Encuentro)

Representa un combate o enfrentamiento activo.

```json
{
  "id": string,
  "name": string,
  "participants": [Entity],
  "initiative_order": [string], // IDs ordenados
  "current_turn_index": number,
  "is_active": boolean,
  "history": [EventLog]
}
```

---

## 👤 Entidad: `Entity` (PJ o PNJ)

Representa cualquier criatura participante en el combate.

```json
{
  "id": string,
  "name": string,
  "type": "player" | "npc",
  "owner_id": string | null, // jugador asociado (si aplica)
  "hp": number,
  "max_hp": number,
  "conditions": [Condition],
  "fatigue": number,
  "initiative": number | null,
  "death_saves": {
    "successes": number,
    "failures": number
  },
  "notes": string
}
```

---

## 💠 Entidad: `Condition` (Condición o estado)

Efecto temporal que altera el estado de una criatura.

```json
{
  "id": string,
  "name": string, // "Envenenado", "Aturdido", etc.
  "description": string,
  "duration_type": "manual" | "turns",
  "remaining_turns": number | null
}
```

---

## 👥 Entidad: `Player`

Usuario que se conecta como cliente y controla un PJ.

```json
{
  "id": string,
  "name": string,
  "connected_entity_id": string,
  "connection_status": "connected" | "disconnected",
  "is_turn": boolean
}
```

---

## 📜 Entidad: `EventLog`

Registro histórico de eventos relevantes del combate.

```json
{
  "timestamp": number,
  "event_type": string,
  "description": string,
  "entity_id": string | null
}
```

---

## 🔧 Estructura: `ServerState`

Estado global mantenido por el servidor (DJ).

```json
{
  "encounter": Encounter,
  "players": [Player],
  "connections": [ConnectionInfo]
}
```

---

## 🔌 Estructura: `ConnectionInfo`

Información de red asociada a un jugador conectado.

```json
{
  "player_id": string,
  "ip_address": string,
  "last_ping": number,
  "status": "pending" | "accepted" | "rejected"
}
```

---

Este modelo puede expandirse durante el desarrollo para incluir mecánicas adicionales (por ejemplo, efectos personalizados, acciones rápidas, inventario). Debe mantenerse sincronizado con los contratos de red y eventos del motor de combate.
