# ✅ Test Plan — D\&D 5e Combat Manager

Este documento define el plan de pruebas para asegurar la estabilidad, funcionalidad y experiencia de usuario del sistema. Las pruebas están organizadas por módulos funcionales y se pueden automatizar, validar manualmente o verificar en sesiones de juego reales.

---

## 🧪 1. Pruebas Generales

| Prueba                               | Tipo   | Método       | Criterio de Éxito                                   |
| ------------------------------------ | ------ | ------------ | --------------------------------------------------- |
| Iniciar aplicación en tablet y móvil | Manual | Exploratorio | Se inicia sin errores en ambos dispositivos         |
| Guardar y cargar encuentro           | Manual | Exploratorio | El estado se guarda y recupera con fidelidad        |
| Reconectar tras cierre inesperado    | Manual | Exploratorio | Se recupera el estado anterior sin pérdida de datos |

---

## 🧠 2. Motor de Combate

| Prueba                         | Tipo   | Método       | Criterio de Éxito                                   |
| ------------------------------ | ------ | ------------ | --------------------------------------------------- |
| Orden correcto de iniciativa   | Unit   | Automático   | Entidades se ordenan según iniciativa               |
| Paso de turno secuencial       | Unit   | Automático   | El turno avanza correctamente en cada ciclo         |
| Tirada automática de salvación | Unit   | Automático   | Se lanza al entrar un jugador inconsciente en turno |
| Fin de combate manual          | Manual | Exploratorio | Al pulsar finalizar, el estado se detiene           |

---

## 📡 3. Comunicación en Red

| Prueba                             | Tipo        | Método     | Criterio de Éxito                                 |
| ---------------------------------- | ----------- | ---------- | ------------------------------------------------- |
| Descubrimiento de servidor         | Integration | Manual     | Jugadores detectan el servidor en red local       |
| Solicitud y aceptación de unión    | Integration | Manual     | DJ recibe solicitud y puede aceptar/rechazar      |
| Sincronización de estado al unirse | Integration | Automático | El jugador ve su ficha y estado actual al entrar  |
| Reconexión tras pérdida de red     | Integration | Manual     | El jugador puede volver al combate sin duplicados |

---

## 🖥️ 4. Interfaz del DJ

| Prueba                     | Tipo   | Método       | Criterio de Éxito                                |
| -------------------------- | ------ | ------------ | ------------------------------------------------ |
| Añadir/eliminar entidades  | Manual | Exploratorio | Las entidades aparecen/desaparecen correctamente |
| Modificar HP y condiciones | Manual | Exploratorio | Los cambios son visibles y sincronizados         |
| Ver detalle de entidad     | Manual | Exploratorio | El panel muestra datos precisos y editables      |
| Control de combate         | Manual | Exploratorio | Los botones de turno, pausa y fin funcionan      |

---

## 📱 5. Interfaz del Jugador

| Prueba                           | Tipo        | Método       | Criterio de Éxito                                 |
| -------------------------------- | ----------- | ------------ | ------------------------------------------------- |
| Pantalla de conexión             | Manual      | Exploratorio | Lista de partidas visibles y seleccionables       |
| Cambio visual al iniciar turno   | Manual      | Exploratorio | Vibración + cambio de fondo se activa             |
| Visualización de condiciones     | Manual      | Exploratorio | Se muestran íconos y descripciones correctas      |
| Tirada automática y notificación | Integration | Automático   | Aparece resultado si el jugador está inconsciente |

---

## 📏 6. UX / Responsividad

| Prueba                          | Tipo   | Método       | Criterio de Éxito                                      |
| ------------------------------- | ------ | ------------ | ------------------------------------------------------ |
| Escalado correcto en móvil      | Manual | Exploratorio | UI adaptada y sin solapamientos                        |
| Orientación vertical/horizontal | Manual | Exploratorio | Cambios de orientación no rompen la interfaz           |
| Modo oscuro                     | Manual | Exploratorio | Activo por defecto y legible                           |
| Feedback visual en botones      | Manual | Exploratorio | Se muestra confirmación inmediata en acciones táctiles |

---

## 🧷 7. Pruebas de Límite / Edge Cases

| Prueba                            | Tipo        | Método     | Criterio de Éxito                                 |
| --------------------------------- | ----------- | ---------- | ------------------------------------------------- |
| Máximo de entidades en un combate | Stress      | Manual     | Fluidez y sincronización sin caídas               |
| Jugador entra tarde               | Integration | Manual     | Puede unirse y recibe estado correctamente        |
| Condición con duración 0          | Unit        | Automático | Se elimina automáticamente al final de turno      |
| Pérdida de conexión del DJ        | Stress      | Manual     | La partida se bloquea correctamente o se recupera |

---

Este plan puede expandirse a medida que se integren nuevas funciones o se automaticen más pruebas con frameworks como Jest, Flutter test, Playwright o Appium.
