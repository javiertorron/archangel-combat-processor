# 🧩 Especificación UX — D\&D 5e Combat Manager

Este documento describe la experiencia de usuario (UX) esperada para la aplicación, orientada a sesiones de *Vibe Coding*. Se detallan las vistas principales y su comportamiento en **tablets** y **móviles**, para dispositivos Android e iOS.

---

## 🎯 Principios de Diseño

* **Primero Tabletas:** Diseño optimizado para tablets en modo horizontal.
* **Adaptable a Móviles:** Adaptación simplificada en formato vertical para móviles.
* **Táctil y sin fricción:** Todos los elementos deben poder manejarse con una sola mano o mediante drag & drop.
* **Contraste visual y accesibilidad:** Colores, tipografía legible y feedback visual.
* **Modo oscuro:** Interfaz por defecto con fondo oscuro, colores suaves y estado resaltado.

---

## 🖥️ Vista del DJ (Tablet)

### 📋 Encuentro Previo al Combate

* Panel dividido horizontalmente:

  * **Izquierda:** Lista de entidades (PJs y PNJs) con avatar, nombre, HP, iniciativa (si ya enviada).
  * **Derecha:** Detalles del encuentro: botones para iniciar, cargar, guardar, añadir criatura.
* Botón flotante para iniciar combate.

### ⚔️ Combate Activo

* Vista tipo "Timeline":

  * Parte superior: orden de iniciativa con avatares.
  * Centro: panel de detalles del personaje activo.
  * Lateral derecho: lista editable de condiciones, botones para modificar HP, añadir efectos, etc.
  * Pie de pantalla: control de combate (siguiente turno, pausa, finalizar).

---

## 📱 Vista del Jugador (Tablet)

### 🏁 Unirse a Encuentro

* Pantalla de detección automática:

  * Lista de servidores encontrados con nombre del DJ o partida.
  * Botón para solicitar acceso.

### 🧍 Turno del Jugador

* Fondo cambia de color + vibración.
* Pantalla muestra:

  * Nombre del personaje, estado actual.
  * Lista de condiciones activas (con íconos y descripciones).
  * Indicador de tiempo opcional (reloj de arena o barra de turno).

---

## 📲 Vista Móvil (DJ y Jugador)

### 📐 Adaptación General

* Mismo flujo que en tablet, con vistas apiladas verticalmente.
* Menús colapsables y navegación por pestañas o acordeones.
* En modo DJ:

  * Control de combate en parte inferior (dock persistente).
  * Cambio entre PJs/PNJs mediante pestañas.
* En modo Jugador:

  * Vista compacta del personaje con un botón flotante para acciones principales.

---

## 🎨 Elementos UI Clave

| Elemento              | Descripción                                                         |
| --------------------- | ------------------------------------------------------------------- |
| Avatar Circular       | Muestra la criatura/personaje con borde según estado (rojo, gris)   |
| Barra de HP           | Color dinámico (verde > amarillo > rojo)                            |
| Fichas de Estado      | Íconos pequeños con tooltip o descripción expandible                |
| Botones flotantes     | Acciones como "siguiente turno", "modificar HP", "añadir condición" |
| Notificación de Turno | Vibración + cambio de fondo + sonido suave                          |

---

## 🧪 Comportamientos UX Especiales

* **Animación entre turnos:** Transición fluida con desvanecido o desplazamiento.
* **Feedback inmediato:** Al pulsar un botón, cambio de estado visible en menos de 100ms.
* **Transiciones seguras:** Al pausar o cerrar la app, debe recuperarse el estado actual.

---

## 🛠️ Consideraciones Técnicas

* Resoluciones base: 768x1024 (tablet) y 360x640 (móvil vertical).
* Sistema de diseño escalable con grid adaptable.
* Recomendado uso de librerías UI multiplataforma (React Native Paper, Flutter Material, etc.)

---

Este documento sirve como referencia visual para desarrollo progresivo y sesiones de Vibe Coding con LLMs.
