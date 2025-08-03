# Fases de Implementación

## Fase 0 — Preparación y documentación
- **0.1 Correcciones editoriales:** corregir erratas, completar tablas y cerrar bloques de código.
- **0.2 Máquina de estados:** reemplazar `state_machine.md` con la descripción real de estados y transiciones.
- **0.3 Alineación de documentación:** asegurar que todos los documentos coincidan con el modelo de datos y los contratos de red.

## Fase 1 — Modelo y persistencia
- **1.1 Estructuras de datos:** implementar `Encounter`, `Entity`, `Condition`, `Player`, `EventLog` y `ServerState`.
- **1.2 Persistencia local:** permitir cargar y guardar encuentros del DJ en almacenamiento local.

## Fase 2 — Motor de combate
- **2.1 Cola de eventos:** desarrollar `CombatEngine` con eventos como `COMBAT_INITIATED` y `TURN_STARTED`.
- **2.2 Gestión de turnos:** implementar `TurnManager` y la lógica de desempate de iniciativa.
- **2.3 Sincronización y registro:** integrar `EventLogger` y `StateSynchronizer`.

## Fase 3 — Comunicación en red
- **3.1 Descubrimiento:** implementar mDNS o broadcast UDP para localizar servidores.
- **3.2 Conexiones:** crear `ConnectionManager` y `MessageDispatcher` basados en WebSocket.
- **3.3 Sincronización de estado:** manejar mensajes `update_state`, `encounter_state` y reconexiones.

## Fase 4 — Interfaz del DJ
- **4.1 Componentes principales:** `EncounterSetupPanel`, `EntityList`, `InitiativeTimeline`, `EntityDetailPanel`, `CombatControlBar` y `NotesPanel`.
- **4.2 Control de combate:** iniciar, pausar y terminar encuentros; edición de HP y condiciones.

## Fase 5 — Interfaz del Jugador
- **5.1 Pantallas:** `ServerDiscoveryScreen`, `AwaitingApprovalScreen`, `PlayerTurnView` y `ConditionViewer`.
- **5.2 Notificaciones de turno:** vibración, cambio de fondo y tiradas automáticas de salvación.

## Fase 6 — UI compartida y UX
- **6.1 Componentes reutilizables:** `HealthBar`, `ConditionBadge`, `RollIndicator`, `TabbedView`.
- **6.2 Responsividad y accesibilidad:** soporte móvil/tablet, tema oscuro y criterios de accesibilidad.

## Fase 7 — Pruebas
- **7.1 Unitarias:** motor de combate, empates de iniciativa, condiciones de duración cero.
- **7.2 Integración:** flujos de conexión, sincronización y reconexión.
- **7.3 Manuales/UX:** exploración de vistas, escalado y orientación de pantalla.

## Fase 8 — Empaquetado y despliegue
- **8.1 Builds móviles:** scripts para Android e iOS.
- **8.2 Beta interna:** distribución, recopilación de feedback y refinamiento final.
