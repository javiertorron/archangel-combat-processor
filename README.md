# 📘 Proyecto: Gestor de Encuentros y Seguimiento de Combate para D&D 5e

## 🧠 Propósito de este documento

Este README sirve como *contexto base* para un LLM que participará en sesiones de _Vibe Coding_. Su objetivo es transmitir de forma clara y estructurada **qué debe hacer la aplicación**, sin entrar en detalles de lenguaje, arquitectura o código.

---

## 🎯 Objetivo General

Crear una aplicación que asista a los Directores de Juego (DJs) de **Dungeons & Dragons 5ª edición** durante los combates, facilitando la gestión de encuentros, el seguimiento de turnos y el estado de los participantes, con una experiencia fluida y centrada en la narrativa.

---

## 🧰 Funcionalidades Clave

- **Gestión de Encuentros:**
  - Crear, guardar y cargar encuentros personalizados.
  - Añadir personajes jugadores (PJs) y enemigos (PNJs) con sus datos básicos.

- **Seguimiento de Combate:**
  - Control automático de la iniciativa y del orden de turnos.
  - Gestión visual de condiciones, estados y efectos activos.
  - Modificación y seguimiento de puntos de vida.
  - Control del progreso del combate (siguiente turno, pausa, reinicio).

- **Soporte para el DJ:**
  - Área para tomar notas por criatura o combate.
  - Visualización rápida del estado de cada entidad.
  - Registro cronológico de eventos del combate.

---

## ✅ Requisitos Funcionales

- El sistema debe permitir al DJ:
  - Añadir, editar y eliminar criaturas (PJs y PNJs).
  - Iniciar un combate con los participantes definidos.
  - Calcular y ordenar la iniciativa automáticamente.
  - Avanzar y retroceder turnos.
  - Aplicar y visualizar condiciones/estados.
  - Modificar puntos de vida en tiempo real.
  - Acceder a un historial básico del combate.

---

## 🚫 Requisitos No Funcionales

- **Usabilidad:** Interfaz accesible y clara, diseñada para usarse durante una partida en curso, sin interrumpir el flujo de juego.
- **Rendimiento:** Operativa fluida con múltiples entidades en el combate.
- **Persistencia:** Capacidad para guardar encuentros y restaurarlos más adelante.
- **Portabilidad:** Funcional en escritorio y móvil, idealmente como aplicación web.
- **Integridad:** Evitar la pérdida de datos durante sesiones largas.
- **Autonomía del DJ:** Solo el DJ debe poder hacer cambios críticos.

---

## 📎 Notas para el LLM

- No se requiere especificar el lenguaje, framework ni patrón de arquitectura en este documento.
- Este archivo define el **comportamiento esperado** desde una perspectiva de usuario.
- Cualquier desarrollo posterior debe alinearse con estas descripciones funcionales.
- Las sesiones de *Vibe Coding* deben partir de este README como referencia de visión general.

