# ⚙️ Eventos Internos del Motor de Combate

Este documento define los **eventos internos** que rigen el flujo del sistema de combate. Cada evento representa una transición de estado, y puede desencadenar acciones automáticas, actualizaciones visuales, mensajes en red o cambios en los datos del combate.

---

## 🧱 Estructura de un Evento

Cada evento interno consta de:

- `id`: Identificador único del evento.
- `trigger`: Qué lo activa (manual, automático o externo).
- `acciones`: Qué cambios produce en el sistema.
- `efectos secundarios`: Notificaciones, logs, animaciones, etc.

---

## 📜 Lista de Eventos

### 1. `COMBAT_INITIATED`

- **Trigger:** El DJ inicia el combate tras recibir todas las iniciativas.
- **Acciones:**
  - Ordenar entidades por iniciativa.
  - Establecer el primer turno.
- **Efectos secundarios:**
  - Emitir `start_encounter` a todos los jugadores.
  - Emitir `turn_start` al primer jugador.

---

### 2. `TURN_STARTED`

- **Trigger:** Se entra en el turno de una entidad.
- **Acciones:**
  - Registrar el comienzo del turno actual.
  - Verificar estados (inconsciencia, condiciones, etc.).
- **Efectos secundarios:**
  - Emitir `turn_start` al jugador correspondiente.
  - Si está inconsciente, lanzar evento `DEATH_SAVE_REQUIRED`.

---

### 3. `DEATH_SAVE_REQUIRED`

- **Trigger:** El jugador está a 0 HP al comenzar su turno.
- **Acciones:**
  - Realizar automáticamente una tirada d20.
  - Evaluar éxito o fallo.
- **Efectos secundarios:**
  - Emitir `death_save_result` al DJ y al jugador.
  - Registrar el éxito/fallo en el historial.
  - Si acumula 3 éxitos o fallos, lanzar `PLAYER_DIED` o `PLAYER_STABLE`.

---

### 4. `TURN_COMPLETED`

- **Trigger:** El DJ o el jugador indica que el turno ha terminado.
- **Acciones:**
  - Aplicar efectos de final de turno (condiciones, duraciones).
  - Determinar siguiente entidad.
- **Efectos secundarios:**
  - Emitir `turn_end` al jugador saliente.
  - Lanzar `TURN_STARTED` para el siguiente.

---

### 5. `PLAYER_STATE_UPDATED`

- **Trigger:** El DJ modifica HP, estados o condiciones de un jugador o PNJ.
- **Acciones:**
  - Actualizar la entidad correspondiente.
- **Efectos secundarios:**
  - Emitir `update_state` al jugador (si aplica).
  - Registrar la modificación en el historial.

---

### 6. `PLAYER_JOINED`

- **Trigger:** Un jugador es aceptado por el DJ.
- **Acciones:**
  - Añadir el jugador al combate.
- **Efectos secundarios:**
  - Emitir `player_joined` a todos los jugadores.
  - Asignar `player_id` único.

---

### 7. `PLAYER_DISCONNECTED`

- **Trigger:** Desconexión inesperada o manual.
- **Acciones:**
  - Marcar al jugador como inactivo.
- **Efectos secundarios:**
  - Notificación opcional al DJ.
  - Permitir reconexión mediante `player_id`.

---

### 8. `COMBAT_ENDED`

- **Trigger:** El DJ decide terminar el encuentro o se elimina al último enemigo.
- **Acciones:**
  - Finalizar todos los estados activos.
  - Guardar el resultado del encuentro.
- **Efectos secundarios:**
  - Emitir `combat_ended` a todos.
  - Volver a modo de edición/post-combate.

---

## 🧩 Observaciones

- Todos los eventos se procesan secuencialmente dentro de una **máquina de estados** o sistema de control centralizado.
- Pueden integrarse con logs, métricas o replay de sesiones.
- Recomendado: colas de eventos internas + middleware para efectos secundarios.

