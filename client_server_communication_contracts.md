# 📡 Contratos de Comunicación Cliente-Servidor

> Formato: JSON sobre WebSocket  
> Todos los mensajes deben incluir una clave `"type"` para identificar su propósito.  
> La comunicación se realiza en red local entre el servidor (DJ) y los clientes (jugadores).

---

## 🧑‍🎤 Cliente → Servidor

| `type`                  | Descripción                                  | Payload                                           |
|------------------------|----------------------------------------------|--------------------------------------------------|
| `discover_server`      | Solicita lista de servidores disponibles      | —                                                |
| `join_request`         | Solicita unirse a un combate activo          | `{ "player_name": string }`                     |
| `submit_initiative`    | Envía la tirada de iniciativa del jugador    | `{ "initiative": number }`                      |
| `ack_turn_notification`| Confirma recepción del turno                  | `{}`                                             |
| `disconnect`           | El jugador abandona el encuentro             | `{}`                                             |

---

## 🧙 Servidor → Cliente (individual)

| `type`                | Descripción                                      | Payload                                                      |
|----------------------|--------------------------------------------------|--------------------------------------------------------------|
| `join_accepted`      | El DJ acepta al jugador                          | `{ "player_id": string }`                                   |
| `join_rejected`      | El DJ rechaza la solicitud del jugador           | `{ "reason": string }`                                      |
| `start_encounter`    | El combate ha comenzado                          | `{}`                                                         |
| `turn_start`         | Es el turno del jugador                          | `{ "player_id": string }`                                   |
| `turn_end`           | Fin del turno del jugador                        | `{}`                                                         |
| `update_state`       | Actualiza los puntos de golpe y condiciones      | `{ "hp": number, "conditions": [string] }`                  |
| `death_save_result`  | Resultado automático de salvación contra la muerte | `{ "success": boolean, "roll": number }`                  |
| `condition_description` | Envia descripción de condiciones activas    | `{ "conditions": [{ "name": string, "description": string }] }` |
| `combat_ended`       | Fin del combate                                  | `{}`                                                         |

---

## 📢 Servidor → Todos los Clientes

| `type`             | Descripción                                | Payload                                  |
|-------------------|--------------------------------------------|------------------
