# 📐 Arquitectura de Software

## 🧱 Modelo General

La aplicación sigue una arquitectura **cliente-servidor peer-to-peer en red local**, orientada principalmente a **tabletas** (Android e iOS), con soporte para móviles.

* **Servidor:** Dispositivo del DJ (Director de Juego)
* **Clientes:** Dispositivos de los jugadores

Cuando se inicia un combate, el DJ inicia la aplicación en modo servidor, permitiendo a los jugadores descubrir y conectarse a él mediante autodescubrimiento en red local (por ejemplo, mDNS o broadcast UDP).

---

## 🗂️ Componentes Principales

### 1. **Servidor (App del DJ)**

* Gestiona el estado central del combate.
* Espera conexiones entrantes y valida acceso de jugadores.
* Mantiene la lógica de turnos, iniciativa, estados y puntos de golpe.
* Envía notificaciones de turno y actualizaciones a los clientes conectados.

### 2. **Clientes (Apps de Jugadores)**

* Detectan servidores activos en la red local.
* Solicitan unirse a un encuentro activo.
* Una vez aceptados, interactúan con su ficha y reciben actualizaciones en tiempo real.
* Reciben notificaciones de turno con vibración y cambio de fondo visual.

---

## 🔁 Flujo de Conexión y Combate

1. DJ inicia la aplicación en modo "Servidor".

2. Jugadores abren su app en modo "Unirse a Encuentro".

3. App del jugador detecta servidores activos en red local (autodiscovery).

4. Jugador solicita acceso al servidor.

5. DJ acepta/rechaza solicitudes entrantes.

6. Una vez aceptado:

   * Jugador establece su iniciativa.
   * Combate inicia.

7. En cada turno:

   * Servidor informa a todos del nuevo turno.
   * Jugador activo recibe:

     * Vibración (si el dispositivo lo soporta)
     * Cambio de fondo indicando su turno
     * Información de estados actuales y sus descripciones
     * Tiradas de salvación automática si está inconsciente (y notificación del resultado)

8. El DJ puede modificar los datos de cualquier entidad:

   * Puntos de golpe
   * Estados y condiciones
   * Fatiga

---

## 📶 Comunicación en Red

* Utilizar sockets TCP o WebSockets en red local.
* Sistema de descubrimiento basado en protocolos como **mDNS** o **UDP broadcast**.
* Todos los datos del estado del combate se sincronizan en tiempo real desde el servidor a los clientes.

---

## 🧩 Tecnologías sugeridas (no vinculantes)

* **Frontend:** React Native, Flutter, SwiftUI/Jetpack Compose
* **Red Local:** mDNS, UDP broadcast, WebSocket para tiempo real
* **Persistencia:** Almacenamiento local para backups del DJ
* **Sincronización:** Modelo unidireccional desde servidor a clientes (pub-sub interno)

---

## 🛡️ Seguridad y Control

* Sólo el DJ puede aceptar jugadores y modificar el estado general del combate.
* Jugadores sólo pueden ver su propia ficha y acciones permitidas.
* El servidor controla la lógica de combate para evitar inconsistencias.

---

## 📱 Enfoque en Tabletas

* El diseño de la interfaz y experiencia de usuario prioriza tablets.
* Distribución adaptable para móviles, con menor prioridad.

---

Este documento evoluciona junto al desarrollo y debe mantenerse sincronizado con los cambios funcionales o estructurales importantes.
