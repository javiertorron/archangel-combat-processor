# 🧩 Component Map — D\&D 5e Combat Manager

Este documento define los principales **componentes de UI** y **componentes lógicos** de la aplicación, organizados por rol (DJ o jugador), dispositivo (tablet/móvil) y propósito (visualización, control, lógica interna). Sirve como referencia modular para el desarrollo progresivo del sistema.

---

## 🖥️ Componentes de UI — Vista del DJ (Tablet)

### 🎛️ `EncounterSetupPanel`

* Permite añadir, editar o eliminar entidades.
* Inicia/carga/guarda encuentros.

### 🧑‍🤝‍🧑 `EntityList`

* Muestra lista de participantes con HP, estado e iniciativa.

### 🔃 `InitiativeTimeline`

* Visualiza el orden de iniciativa como una línea horizontal de avatares.
* Resalta el turno actual.

### 📋 `EntityDetailPanel`

* Muestra y permite editar información detallada de una criatura.
* Acciones rápidas: HP +/–, añadir condición, etc.

### 🎮 `CombatControlBar`

* Botones: siguiente turno, pausar, terminar encuentro.
* Puede incluir reloj de combate.

### 📓 `NotesPanel`

* Notas rápidas por entidad o generales del combate.

---

## 📱 Componentes de UI — Jugador (Tablet/Móvil)

### 🌐 `ServerDiscoveryScreen`

* Lista servidores activos en red local.
* Permite solicitar conexión al DJ.

### ⏳ `AwaitingApprovalScreen`

* Muestra estado de conexión hasta ser aceptado.

### 🧙 `PlayerTurnView`

* Pantalla principal durante el turno del jugador.
* Muestra condiciones, HP, nombre, íconos de estado.
* Cambia fondo y vibra en su turno.

### 📖 `ConditionViewer`

* Lista y descripción de efectos activos.

---

## 📦 Componentes de Lógica Interna

### 🧠 `CombatEngine`

* Controla flujo del combate.
* Lanza eventos internos (inicio, turno, salvación, etc.).

### 🔁 `TurnManager`

* Gestiona el orden de iniciativa y rotación de turnos.

### 🧾 `EventLogger`

* Registra acciones importantes para historial.

### 💬 `MessageDispatcher`

* Envía y recibe mensajes WebSocket.
* Se encarga de la validación y parsing.

### 🔐 `ConnectionManager`

* Mantiene el estado de conexiones de jugadores.
* Detecta reconexiones y gestiona permisos.

### 🌡️ `StateSynchronizer`

* Reenvía datos actualizados a clientes conectados.

---

## 🧩 Componentes Compartidos (UI reutilizable)

### ❤️ `HealthBar`

* Visualiza HP actual con color dinámico.

### 🌀 `ConditionBadge`

* Ícono de estado con tooltip y color por condición.

### 🎲 `RollIndicator`

* Componente visual para mostrar tiradas de dados.

### 🗂️ `TabbedView`

* Navegación en móvil para separar secciones de entidad.

---

Este mapa de componentes es evolutivo y debe mantenerse sincronizado con el diseño UX, los contratos de datos y el flujo del motor de combate.
