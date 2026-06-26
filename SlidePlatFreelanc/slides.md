---
theme: seriph
background: https://images.unsplash.com/photo-1484417894907-623942c8ee29?auto=format&fit=crop&q=80&w=1920
title: "RootDev: Gestión Integral para Freelancers"
info: |
  Proyecto: Plataforma SaaS para la Gestión Integral de Freelancers.
  Carrera de Informática Industrial - I.T. Escuela Industrial Superior “Pedro Domingo Murillo”.
class: text-center
transition: slide-left
mdc: true
---

# RootDev
### Plataforma para la Gestión Integral de Freelancers

**INS - 600 INGENIERIA DE SOFTWARE**

<div class="pt-6 text-sm opacity-80">
  Estudiante: Armin Daniel Antonio Mendieta<br>
</div>

<div class="pt-10">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white op-10">
    Presiona Espacio para continuar <carbon:arrow-right class="inline"/>
  </span>
</div>

<!-- 
TIEMPO: 0:30
- Presentarse.
- Mencionar el nombre del proyecto: RootDev.
- Indicar que es para la materia INS-600.
-->

---
layout: center
class: text-center
---

# Resumen del Proyecto 📝

**RootDev** es una aplicación web diseñada para facilitar la administración de clientes, proyectos y tareas de trabajadores independientes y pequeñas agencias.

Centraliza toda la información, permitiendo un mejor seguimiento de actividades, control de tiempos y organización del trabajo mediante herramientas modernas como tableros **Kanban** y **Dashboards** interactivos.

<!-- 
TIEMPO: 0:30
- Definir RootDev: Una solución SaaS para freelancers.
- Objetivo principal: Centralización y optimización del flujo de trabajo.
-->

---

# Problemática y Objetivos 🎯

### La Problemática
* ❌ Pérdida de información por uso de herramientas dispersas.
* ❌ Falta de seguimiento de proyectos.

### Objetivo General
Desarrollar una plataforma web para la gestión integral de clientes, proyectos y tareas orientada a freelancers.

### Objetivos Específicos
* ✅ Centralizar la gestión de clientes.
* ✅ Organizar proyectos asociados.
* ✅ Visualizar métricas y exponer servicios **REST**.

<!-- 
TIEMPO: 0:45
- Explicar el dolor del usuario: El desorden de usar Excel o correos.
- Mencionar que RootDev ataca directamente esa ineficiencia.
-->

---

# Requisitos del Sistema (MVP) 📋

<div class="grid grid-cols-2 gap-4">
  <div>
    <h3 class="text-primary font-bold">Funcionales (RF)</h3>
    <ul class="text-xs list-disc pl-4">
      <li>Registro y Autenticación.</li>
      <li>CRUD de Clientes y Proyectos.</li>
      <li>Gestión de Tareas (Kanban).</li>
      <li>Exposición de <b>API REST</b>.</li>
    </ul>
  </div>
  <div>
    <h3 class="text-primary font-bold">No Funcionales (RNF)</h3>
    <ul class="text-xs list-disc pl-4">
      <li>Seguridad mediante autenticación.</li>
      <li>Persistencia con <b>PostgreSQL</b>.</li>
      <li>Interfaz intuitiva con Tailwind.</li>
    </ul>
  </div>
</div>

<!-- 
TIEMPO: 0:30
- No leer todo, solo resaltar: Autenticación, Kanban y API REST.
- Mencionar que se buscó seguridad y persistencia sólida.
-->

---

# Arquitectura: Hexagonal 🏗️

Elegida para separar la lógica de negocio de los detalles técnicos.

*   **Independencia:** El núcleo es independiente del framework Django.
*   **Testabilidad:** Facilita las pruebas unitarias del dominio.
*   **Mantenibilidad:** Código más limpio y fácil de evolucionar.
*   **Flexibilidad:** Permite cambiar adaptadores (DB, UI) con mínimo impacto.

<!-- 
TIEMPO: 0:50
- EXPLICAR BIEN: Es el pilar técnico. 
- La lógica de negocio está protegida de cambios externos.
- Facilita los tests que veremos más adelante.
-->

---

# Plataforma de Trabajo 🛠️

| Componente | Tecnología |
|---|---|
| **S.O.** | Fedora Linux |
| **Lenguaje** | Python 3.14.5 |
| **Backend** | Django 4.2.30 |
| **API REST** | Django REST Framework 3.17.1 |
| **Base de Datos** | PostgreSQL + Django ORM |
| **Interactividad** | HTMX + Tailwind CSS |

<!-- 
TIEMPO: 0:20
- Rápido: Usamos Python/Django por su robustez y PostgreSQL para datos críticos.
- HTMX para no sobrecargar el frontend.
-->

---
background: https://images.unsplash.com/photo-1531403009284-440f080d1e12?auto=format&fit=crop&q=80&w=1920
---

# Metodología: SCRUM Ágil 🔄

Desarrollo iterativo e incremental organizado en fases:

<div class="mt-8 overflow-hidden rounded-xl border border-gray-200 shadow-lg">
  <table class="w-full text-left border-collapse bg-white dark:bg-gray-900">
    <thead class="bg-primary text-white">
      <tr>
        <th class="px-4 py-3 font-bold uppercase text-xs tracking-wider">Sprint</th>
        <th class="px-4 py-3 font-bold uppercase text-xs tracking-wider">Objetivo</th>
        <th class="px-4 py-3 font-bold uppercase text-xs tracking-wider">Entregables</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200 dark:divide-gray-800 text-sm">
      <tr>
        <td class="px-4 py-4 font-bold text-primary">Sprint 1</td>
        <td class="px-4 py-4 italic">Seguridad</td>
        <td class="px-4 py-4 text-xs">Auth y Clientes.</td>
      </tr>
      <tr>
        <td class="px-4 py-4 font-bold text-primary">Sprint 2</td>
        <td class="px-4 py-4 italic">Operación</td>
        <td class="px-4 py-4 text-xs">Kanban y Proyectos.</td>
      </tr>
      <tr>
        <td class="px-4 py-4 font-bold text-primary">Sprint 3</td>
        <td class="px-4 py-4 italic">Métricas</td>
        <td class="px-4 py-4 text-xs">Dashboard y API REST.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- 
TIEMPO: 0:30
- Dividido en 3 etapas claras: Desde la base segura hasta el análisis de datos.
-->

---

# Diagrama de Casos de Uso 👤

<div class="flex flex-col h-full">
  <div class="bg-primary/10 border-l-4 border-primary p-2 mb-4 rounded-r shadow-sm">
    <p class="text-sm opacity-90 italic text-center">Interacciones principales: Gestión de Clientes, Proyectos y Métricas.</p>
  </div>
  <div class="flex-grow flex items-center justify-center bg-gray-50 rounded-2xl border border-gray-200 shadow-inner overflow-hidden p-4">
    <img src="./images/DIAGRAMADECASOSDEUSO.png" class="max-w-full max-h-full object-contain transform scale-110 shadow-xl" />
  </div>
</div>

<!-- 
TIEMPO: 0:30
- El actor principal es el Freelancer.
- Resaltar las 3 áreas de acción: Administrativa, Operativa y Analítica.
-->

---

# Diagrama de Clases 📊

<div class="flex flex-col h-full">
  <div class="flex-grow relative flex justify-center items-center bg-gray-50 rounded-xl border border-gray-200 p-4">
     <div class="flex flex-col items-center">
        <img src="./images/DIAGRAMADECLASES.png" class="h-60 object-contain shadow-lg" />
        <p class="text-sm font-mono text-primary mt-4">User ➔ Client ➔ Project ➔ Task</p>
     </div>
  </div>
</div>

<!-- 
TIEMPO: 0:40
- Explicar la jerarquía: Un usuario tiene N clientes, un cliente tiene N proyectos...
- Es una estructura relacional sólida.
-->

---

# Diagramas de Comportamiento ⚙️

<div class="grid grid-cols-2 gap-6 h-full pb-10">
  <div class="flex flex-col">
    <h3 class="flex items-center gap-2 text-primary font-bold">Secuencia</h3>
    <div class="flex-grow bg-white rounded-lg border p-2 flex items-center justify-center">
      <img src="./images/DIAGRAMADESECUENCIA.png" class="h-40" />
    </div>
  </div>
  <div class="flex flex-col">
    <h3 class="flex items-center gap-2 text-primary font-bold">Colaboración</h3>
    <div class="flex-grow bg-white rounded-lg border p-2 flex items-center justify-center">
      <img src="./images/DIAGRAMADECOLABORACION.png" class="h-40" />
    </div>
  </div>
</div>

<!-- 
TIEMPO: 0:40
- Secuencia: Cómo viajan los mensajes para crear una tarea.
- Colaboración: Cómo se organizan los objetos estructuralmente.
-->

---

# Diagrama de Estados 🔄

<div class="flex flex-col items-center justify-center h-full space-y-4">
  <div class="w-full max-w-4xl h-70 bg-white rounded-2xl border shadow-xl flex items-center justify-center p-4">
    <img src="./images/DIAGRAMADEESTADOS.png" class="h-full object-contain" />
  </div>
</div>

<!-- 
TIEMPO: 0:30
- Ciclo de vida de una tarea: De Pendiente a Completada.
- Es vital para el funcionamiento del Kanban.
-->

---

# Módulo: CRM y Gestión de Clientes 👥

<div class="grid grid-cols-2 gap-4">
  <div>
    <ul class="text-sm">
      <li><b>CRUD Completo</b> de Clientes.</li>
      <li><b>Seguridad:</b> Datos aislados por usuario.</li>
    </ul>
    <div class="mt-4 p-2 bg-white border rounded shadow-sm overflow-hidden">
      <ZoomImg src="./images/login_register.png" class="w-full h-32 object-cover rounded" />
    </div>
  </div>
  <div class="flex items-center justify-center p-2 bg-gray-50 rounded-xl border">
    <ZoomImg src="./images/clientes.png" class="rounded shadow-lg" />
  </div>
</div>

<!-- 
TIEMPO: 0:40
- ENTRAR EN DETALLE: Aquí empieza el zoom.
- Mostrar la interfaz limpia y el acceso seguro.
-->

---

# Módulo: Proyectos y Tablero Kanban 📋

<div class="grid grid-cols-2 gap-6">
  <div class="text-xs space-y-4">
    <div class="bg-primary/5 p-3 rounded border-l-4 border-primary">
      <h3 class="font-bold text-sm text-primary">Gestión de Proyectos</h3>
      <ZoomImg src="./images/proyectos.png" class="mt-2 rounded shadow-sm" />
    </div>
  </div>
  <div class="flex items-center justify-center p-2 bg-gray-50 rounded-xl border">
    <ZoomImg src="./images/tareas.png" class="rounded shadow-lg" />
  </div>
</div>

<!-- 
TIEMPO: 0:50
- EL CORAZÓN: Explica cómo el Kanban usa HTMX para actualizaciones sin recarga.
- Haz zoom en las tareas para que vean el detalle.
-->

---

# Módulo: Dashboard de Productividad 📊

<div class="flex flex-col h-full space-y-4">
  <div class="flex-grow flex items-center justify-center p-4 bg-white rounded-2xl border shadow-xl overflow-hidden">
    <ZoomImg src="./images/dashboard.png" class="max-h-full object-contain rounded" />
  </div>
</div>

<!-- 
TIEMPO: 0:40
- El valor agregado: El freelancer ve cuánto está produciendo en tiempo real.
-->

---

# Plan de Pruebas Automatizado 🛡️

Puntos validados en el módulo `freelance_core`:

1.  **Creación de Entidades:** Registro correcto de Clientes, Proyectos y Tareas.
2.  **Borrado en Cascada:** Validación de la integridad referencial en la base de datos.
3.  **Protección de Rutas:** Verificación de redirección al Login para usuarios no autorizados.
4.  **Gestión de Cuentas:** Validación de los flujos de Registro e Inicio de Sesión.

<div class="mt-4 p-4 bg-gray-900 rounded-lg font-mono text-[10px] text-green-400 shadow-2xl border border-white/10">
  $ python manage.py test freelance_core<br>
  Creating test database for alias 'default'...<br>
  .......<br>
  Ran 7 tests in 6.759s | Result: OK
</div>

<!-- 
TIEMPO: 0:30
- Menciona que las pruebas son automatizadas y corren sobre PostgreSQL.
- Cubren desde la creación de usuarios hasta el borrado en cascada.
-->

---

# Evidencias de Validación ✅

<div class="grid grid-cols-2 gap-4 h-full">
  <div class="text-xs">
    <table class="w-full">
      <tbody class="divide-y">
        <tr><td class="py-2">Auth y Registro</td><td class="py-2 text-green-600 font-bold">EXITOSO</td></tr>
        <tr><td class="py-2">Middleware de Seguridad</td><td class="py-2 text-green-600 font-bold">EXITOSO</td></tr>
        <tr><td class="py-2">Integridad de Datos</td><td class="py-2 text-green-600 font-bold">EXITOSO</td></tr>
      </tbody>
    </table>
  </div>
  <div class="flex flex-col space-y-2">
    <div class="flex-grow bg-white rounded border p-2 overflow-hidden flex items-center justify-center">
      <ZoomImg src="./images/APIREST.png" class="h-full object-contain" />
    </div>
  </div>
</div>

<!-- 
TIEMPO: 0:30
- Resumen final de validación. 
- Mencionar la API REST como evidencia de conectividad.
-->

---

# Conclusiones y Futuro 🎓

### Conclusiones (Cumplimiento de Objetivos)
* ✅ **Gestión Centralizada:** Se logró unificar la información de clientes en un entorno seguro y accesible.
* ✅ **Organización Operativa:** La estructura de proyectos y el tablero Kanban optimizan el seguimiento de tareas.
* ✅ **Analítica y Conectividad:** El Dashboard y la API REST permiten la toma de decisiones basada en datos.

### Futuro
* 🤖 Predicción con IA.
* 📱 App Móvil.

<!-- 
TIEMPO: 0:30
- El proyecto cumple todos los objetivos.
- RootDev está listo para evolucionar.
-->

---
layout: center
class: text-center
background: https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1920
---

# ¡Gracias por su atención!

**RootDev**

<div class="mt-10 flex justify-center gap-4 text-sm">
  <span>Estudiante: Armin Daniel Antonio Mendieta</span>
</div>

<!-- 
TIEMPO: 0:05
- Cierre y preguntas.
-->

<script setup>
import { watch, onMounted } from 'vue'
import { useNav } from '@slidev/client'

const { next, currentPage } = useNav()

/**
 * CONFIGURACIÓN DE TIEMPOS (Total 600s = 10min)
 * Cada número representa los segundos que durará ese slide antes de saltar.
 */
const slideTimes = [
  10, // 1. Portada
  15, // 2. Resumen
  20, // 3. Problemática
  20, // 4. Requisitos
  15, // 5. Arquitectura
  15, // 6. Plataforma
  15, // 7. Metodología
  15, // 8. Casos de Uso
  15, // 9. Clases
  15, // 10. Comportamiento
  15, // 11. Estados
  15, // 12. CRM
  15, // 13. Kanban
  15, // 14. Dashboard
  15, // 15. Plan de Pruebas
  15, // 16. Evidencias
  15, // 17. Conclusiones
  10  // 18. Despedida
]

onMounted(() => {
  let timerId = null

  // Observar el cambio de página para reiniciar el temporizador
  watch(currentPage, (newPage) => {
    // Limpiar cualquier temporizador activo
    if (timerId) clearTimeout(timerId)

    // Obtener segundos para el slide actual (ajustado a índice 0)
    const seconds = slideTimes[newPage - 1]
    
    // Solo avanzar si no es el último slide
    if (seconds && newPage < slideTimes.length) {
      timerId = setTimeout(() => {
        next()
      }, seconds * 1000)
    }
  }, { immediate: true })
})
</script>

