# 🧙‍♂️ Aplicación de Gestión de Encuentros y Seguimiento de Combate para D&D 5e

## 🎯 Objetivo General

Crear una aplicación que asista a los Directores de Juego (DJs) de **Dungeons & Dragons quinta edición (5e)** durante los combates, facilitando la gestión de encuentros, el seguimiento de turnos y el estado de los participantes, con una experiencia fluida y centrada en la narrativa.

---

## 🧠 Propósito de este README

Este archivo está diseñado para ser utilizado como base de contexto por un **modelo de lenguaje (LLM)** en sesiones de _Vibe Coding_. Resume los objetivos funcionales del sistema sin entrar en aspectos técnicos de implementación, arquitectura ni código.

---

## 🧰 Funcionalidades Clave

### 👥 Gestión de Encuentros
- Crear, guardar y cargar encuentros personalizados.
- Añadir personajes jugadores (PJs) y enemigos (PNJs) con sus estadísticas básicas.
- Iniciar combates con control completo desde el DJ.

### 🌀 Seguimiento de Combate
- Control automático del orden de iniciativa y turnos.
- Modificación y visualización de puntos de golpe (HP).
- Aplicación y seguimiento de condiciones y estados (aturdido, envenenado, etc.).
- Registro cronológico básico del desarrollo del combate.
- Visualización del estado actual de cada entidad.

### 📝 Soporte para el DJ
- Área de notas por criatura o combate.
- Posibilidad de pausar, reiniciar o finalizar combates en cualquier momento.
- Cambiar HP, condiciones y niveles de fatiga de cualquier participante.

---

## 🔌 Funcionalidades Multidispositivo en Red Local

### 🌐 Arquitectura Cliente-Servidor
- El DJ inicia el combate y la app entra en **modo servidor**.
- Los jugadores usan su app en **modo cliente** y detectan automáticamente los servidores disponibles en la red local.

### 🤝 Conexión y Aceptación
- Los jugadores solicitan acceso al combate activo.
- El DJ acepta manualmente cada solicitud.

### 🎲 Fase de Iniciativa
- Una vez aceptado, cada jugador envía su iniciativa.
- El combate inicia automáticamente una vez todos han enviado su tirada.

### ⏱️ Turnos y Notificaciones
- Cuando es el turno de un jugador:
  - Su dispositivo vibra (si es compatible).
  - El fondo de pantalla cambia para indicar que es su turno.
  - Recibe información detallada sobre sus condiciones activas.
- Si el jugador está inconsciente, el sistema realiza automáticamente una tirada de salvación contra la muerte y notifica el resultado.

---

## ✅ Requisitos Funcionales

- Crear y editar entidades: PJs, PNJs, condiciones, HP, fatiga.
- Calcular y gestionar la iniciativa.
- Avanzar turnos con sincronización en tiempo real.
- Aplicar tiradas automáticas en caso de inconsciencia.
- Gestionar el acceso de jugadores desde la app del DJ.

---

## 🚫 Requisitos No Funcionales

- **Usabilidad:** Interfaz clara, táctil y usable durante la partida.
- **Rendimiento:** Baja latencia en red local con múltiples conexiones activas.
- **Portabilidad:** Orientado a tablets (Android/iOS), funcional en móviles.
- **Persistencia:** Capacidad de guardar y restaurar encuentros.
- **Integridad:** Protección contra pérdida de datos durante el combate.
- **Control de Autoridad:** Solo el DJ puede modificar el estado global del sistema.

---

## 📎 Notas para el LLM

- Este archivo define la visión y comportamiento esperado de la app.
- No se especifica aún ningún lenguaje, framework o patrón de desarrollo.
- Sirve como base para generar estructuras de datos, lógica de control, UI/UX y diseño de red.
- Cualquier diseño técnico posterior (componentes, APIs, etc.) debe alinearse con este documento.
