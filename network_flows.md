# 🌐 Flujos de Red Local — D&D 5e Combat Manager

Este documento describe los **flujos de red** entre clientes (jugadores) y el servidor (DJ) en una red local, utilizando una arquitectura cliente-servidor con autodescubrimiento y comunicación en tiempo real.

---

## 🧭 1. Descubrimiento del Servidor

### Objetivo:
Permitir que los jugadores encuentren el servidor activo en la red local sin necesidad de introducir una IP manualmente.

### Proceso:
1. El DJ inicia la aplicación en **modo servidor**.
2. El servidor se anuncia en la red local mediante **mDNS** o **UDP broadcast**.
3. El jugador abre la app en **modo cliente**.
4. La app del jugador escucha la red y muestra una lista de servidores activos disponibles.

---

## 🔐 2. Solicitud de Conexión

### Objetivo:
Permitir que los jugadores pidan unirse a un combate iniciado por el DJ.

### Proceso:
1. El jugador selecciona un servidor de la lista.
2. Envía un mensaje `join_request` con su nombre.
3. El servidor muestra la solicitud al DJ.
4. El DJ **acepta o rechaza** manualmente la solicitud.
5. Si es aceptado, el servidor responde con `join_accepted` y asigna un `player_id`.

---

## 🎲 3. Tirada de Iniciativa

### Objetivo:
Recoger las iniciativas de todos los jugadores antes de empezar el combate.

### Proceso:
1. El jugador envía un mensaje `submit_initiative` con su tirada.
2. El servidor guarda todas las iniciativas.
3. Una vez todos los jugadores han enviado su iniciativa, el combate se inicia.

---

## 🕐 4. Gestión de Turnos

### Objetivo:
Coordinar los turnos entre jugadores de forma sincronizada.

### Proceso por turno:
1. El servidor determina quién actúa a continuación.
2. Envía a ese jugador el mensaje `turn_start`.
3. El jugador recibe:
   - Vibración (si aplica)
   - Cambio visual del fondo
   - Lista de condiciones activas y sus descripciones
4. Si el personaje está **inconsciente**:
   - El servidor lanza una **tirada automática de salvación contra la muerte**.
   - Envía el resultado al jugador y al DJ mediante `death_save_result`.
5. Al terminar el turno, el servidor emite `turn_end` y pasa al siguiente.

---

## 🔁 5. Sincronización de Estado

### Objetivo:
Mantener actualizada la información visible por los jugadores.

### Proceso:
- El servidor emite `update_state` cuando cambia el HP o los estados del personaje.
- También puede emitir `encounter_state` para sincronizar el orden de iniciativa y el turno actual.

---

## ❌ 6. Desconexión

### Objetivo:
Gestionar desconexiones de forma segura.

### Proceso:
- Si un jugador se desconecta voluntariamente, envía `disconnect`.
- Si se desconecta inesperadamente:
  - El servidor lo detecta.
  - Puede permitir reconexión manual o automática mediante `player_id`.

---

## 📶 Diagrama Resumido

```text
[Jugador] ---> (broadcast/mDNS) ---> Descubre servidor
[Jugador] ---> join_request -------> [Servidor]
[Servidor] ---> join_accepted ------> [Jugador]
[Jugador] ---> submit_initiative --> [Servidor]
[Servidor] ---> start_encounter ---> Todos
[Servidor] ---> turn_start --------> Jugador activo
[Servidor] ---> update_state ------> Jugador
[Servidor] ---> encounter_state ---> Todos
[Servidor] ---> turn_end ----------> Todos
```

Este diagrama resume los mensajes clave intercambiados durante un combate.
