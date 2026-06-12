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
### Plataforma SaaS para la Gestión Integral de Freelancers

**INS - 600 INGENIERIA DE SOFTWARE**

<div class="pt-6 text-sm opacity-80">
  Estudiante: Armin Daniel Antonio Mendieta<br>
  Catedrático: Pablo Osco
</div>

<div class="pt-10">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white op-10">
    Presiona Espacio para continuar <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: center
class: text-center
---

# Resumen del Proyecto 📝

**RootDev** es una aplicación web diseñada para facilitar la administración de clientes, proyectos y tareas de trabajadores independientes y pequeñas agencias.

Centraliza toda la información, permitiendo un mejor seguimiento de actividades, control de tiempos y organización del trabajo mediante herramientas modernas como tableros **Kanban** y **Dashboards** interactivos.

---

# Problemática y Objetivos 🎯

### La Problemática
* ❌ Pérdida de información por uso de herramientas dispersas (Excel, correos).
* ❌ Falta de seguimiento de proyectos y priorización de tareas.
* ❌ Baja eficiencia operativa y dificultad para medir productividad.

### Objetivo General
Desarrollar una plataforma web para la gestión integral de clientes, proyectos y tareas orientada a freelancers.

### Objetivos Específicos
* ✅ Centralizar la gestión de clientes.
* ✅ Organizar proyectos asociados a clientes.
* ✅ Gestionar tareas mediante Kanban.
* ✅ Visualizar métricas y exponer servicios **REST**.

---

# Requisitos del Sistema (MVP) 📋

<div class="grid grid-cols-2 gap-4">
  <div>
    <h3 class="text-primary font-bold">Funcionales (RF)</h3>
    <ul class="text-xs list-disc pl-4">
      <li>Registro y Autenticación de usuarios.</li>
      <li>CRUD completo de Clientes.</li>
      <li>Gestión de Proyectos vinculados a clientes.</li>
      <li>Gestión de Tareas con estados dinámicos.</li>
      <li>Dashboard de indicadores de productividad.</li>
      <li>Exposición de servicios vía <b>API REST</b>.</li>
    </ul>
  </div>
  <div>
    <h3 class="text-primary font-bold">No Funcionales (RNF)</h3>
    <ul class="text-xs list-disc pl-4">
      <li>Disponibilidad > 95%.</li>
      <li>Interfaz amigable e intuitiva.</li>
      <li>Seguridad robusta mediante autenticación.</li>
      <li>Persistencia con <b>PostgreSQL</b>.</li>
      <li>Arquitectura desacoplada y escalable.</li>
    </ul>
  </div>
</div>

---

# Arquitectura: Hexagonal (Puertos y Adaptadores) 🏗️

Elegida para separar la lógica de negocio de los detalles técnicos.

*   **Independencia:** El núcleo es independiente del framework Django.
*   **Testabilidad:** Facilita las pruebas unitarias del dominio.
*   **Mantenibilidad:** Código más limpio y fácil de evolucionar.
*   **Flexibilidad:** Permite cambiar adaptadores (DB, UI, APIs) con mínimo impacto.

---

# Plataforma de Trabajo 🛠️

| Componente | Tecnología |
|---|---|
| **S.O.** | Fedora Linux |
| **Lenguaje** | Python 3.14.5 |
| **Backend** | Django 4.2.30 |
| **API REST** | Django REST Framework 3.17.1 |
| **Base de Datos** | PostgreSQL + Django ORM |
| **Interactividad** | HTMX |
| **Estilos** | Tailwind CSS |
| **Otros** | WhiteNoise, Dotenv, WeasyPrint |

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
        <th class="px-4 py-3 font-bold uppercase text-xs tracking-wider">Objetivo Principal</th>
        <th class="px-4 py-3 font-bold uppercase text-xs tracking-wider">Entregables Clave</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200 dark:divide-gray-800 text-sm">
      <tr class="hover:bg-primary/5 transition-colors">
        <td class="px-4 py-4 font-bold text-primary">Sprint 1</td>
        <td class="px-4 py-4 italic">Cimientos y Seguridad</td>
        <td class="px-4 py-4 text-xs">Configuración Base, PostgreSQL, Auth de Usuarios y CRUD de Clientes.</td>
      </tr>
      <tr class="hover:bg-primary/5 transition-colors">
        <td class="px-4 py-4 font-bold text-primary">Sprint 2</td>
        <td class="px-4 py-4 italic">Operación Core</td>
        <td class="px-4 py-4 text-xs">Gestión de Proyectos, Tareas y Tablero Kanban interactivo con HTMX.</td>
      </tr>
      <tr class="hover:bg-primary/5 transition-colors">
        <td class="px-4 py-4 font-bold text-primary">Sprint 3</td>
        <td class="px-4 py-4 italic">Métricas y Conectividad</td>
        <td class="px-4 py-4 text-xs">Dashboard de Productividad y exposición de la API REST.</td>
      </tr>
    </tbody>
  </table>
</div>

---

# Diagrama de Casos de Uso 👤

<div class="grid grid-cols-2 gap-8 h-full items-center">
  <div class="space-y-4">
    <p class="text-lg opacity-90">Representación de las interacciones entre el <b>Freelancer</b> y las funcionalidades core del sistema.</p>
    <div class="bg-primary/10 border-l-4 border-primary p-4 rounded-r shadow-sm">
      <h4 class="font-bold text-primary">Puntos Clave:</h4>
      <ul class="list-disc pl-5 text-sm">
        <li>Gestión de Clientes (CRUD)</li>
        <li>Administración de Proyectos</li>
        <li>Control de Tareas y Kanban</li>
        <li>Visualización de Métricas</li>
      </ul>
    </div>
  </div>
  <div class="relative group">
    <div class="absolute -inset-1 bg-gradient-to-r from-primary to-blue-500 rounded-lg blur opacity-25 group-hover:opacity-50 transition duration-1000"></div>
    <div class="relative flex justify-center items-center bg-white dark:bg-gray-800 border-2 border-gray-100 dark:border-gray-700 rounded-lg p-2 h-80 shadow-xl overflow-hidden">
      <img src="./images/DIAGRAMADECASOSDEUSO.png" class="h-full object-contain" />
    </div>
  </div>
</div>

---

# Diagrama de Clases 📊

<div class="flex flex-col h-full">
  <p class="mb-4">Estructura detallada de las entidades y la jerarquía de datos en <b>RootDev</b>.</p>
  
  <div class="flex-grow relative flex justify-center items-center bg-gray-50 dark:bg-gray-900/50 rounded-xl border border-gray-200 dark:border-gray-700 shadow-inner p-4 overflow-hidden">
     <div class="absolute top-4 left-4 flex gap-2">
       <div class="w-3 h-3 rounded-full bg-red-400"></div>
       <div class="w-3 h-3 rounded-full bg-yellow-400"></div>
       <div class="w-3 h-3 rounded-full bg-green-400"></div>
     </div>
     <div class="flex flex-col items-center">
        <img src="./images/DIAGRAMADECLASES.png" class="h-70 object-contain shadow-lg rounded border border-gray-200" />
        <p class="text-sm font-mono text-primary opacity-60 bg-primary/5 px-4 py-2 rounded-full mt-4">Relación: User ➔ Client ➔ Project ➔ Task</p>
     </div>
  </div>
</div>

---

# Diagramas de Comportamiento ⚙️

<div class="grid grid-cols-2 gap-6 h-full pb-10">
  <div class="flex flex-col">
    <h3 class="flex items-center gap-2 text-primary mb-2 font-bold"><carbon:flow-data /> Secuencia</h3>
    <div class="flex-grow bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 p-2 flex flex-col items-center justify-center text-center shadow-md overflow-hidden text-sm">
      <img src="./images/DIAGRAMADESECUENCIA.png" class="h-full object-contain" />
    </div>
  </div>
  <div class="flex flex-col">
    <h3 class="flex items-center gap-2 text-primary mb-2 font-bold"><carbon:connect-recursive /> Colaboración</h3>
    <div class="flex-grow bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 p-2 flex flex-col items-center justify-center text-center shadow-md overflow-hidden text-sm">
      <img src="./images/DIAGRAMADECOLABORACION.png" class="h-full object-contain" />
    </div>
  </div>
</div>

---

# Diagrama de Estados 🔄

<div class="flex flex-col items-center justify-center h-full space-y-4">
  <p class="text-lg">Control del ciclo de vida de una <b>Tarea</b>, garantizando la consistencia del flujo de trabajo.</p>
  
  <div class="w-full max-w-4xl h-80 bg-white dark:bg-gray-800 rounded-2xl border border-gray-200 dark:border-gray-700 shadow-2xl flex items-center justify-center relative overflow-hidden p-4">
    <img src="./images/DIAGRAMADEESTADOS.png" class="h-full object-contain" />
  </div>
</div>

---

# Módulo: CRM y Gestión de Clientes 👥

Centralización de la información de contacto y empresarial.

<div class="grid grid-cols-2 gap-4">
  <div>
    <ul>
      <li><b>CRUD Completo:</b> Registro, edición y eliminación de clientes.</li>
      <li><b>Seguridad:</b> Cada cliente está vinculado estrictamente al usuario autenticado.</li>
      <li><b>Interfaz:</b> Tablas dinámicas con Tailwind CSS y HTMX para búsquedas rápidas.</li>
    </ul>
    <div class="mt-4 p-2 bg-white dark:bg-gray-800 border rounded shadow-sm overflow-hidden">
      <ZoomImg src="./images/login_register.png" class="w-full h-32 object-cover rounded" />
      <p class="text-[8px] text-center mt-1 opacity-50 italic">Interfaz de Acceso Seguro</p>
    </div>
  </div>
  <div class="flex items-center justify-center p-2 bg-gray-50 dark:bg-gray-900 rounded-xl border border-gray-200 shadow-inner">
    <ZoomImg src="./images/clientes.png" class="rounded shadow-lg border border-gray-200" />
  </div>
</div>

---

# Módulo: Proyectos y Tablero Kanban 📋

El corazón operativo de RootDev.

<div class="grid grid-cols-2 gap-6">
  <div class="text-xs space-y-4">
    <div class="bg-primary/5 p-3 rounded border-l-4 border-primary">
      <h3 class="font-bold text-sm">Gestión de Proyectos</h3>
      <p>Asociación jerárquica que permite organizar el trabajo por cliente.</p>
      <ZoomImg src="./images/proyectos.png" class="mt-2 rounded shadow-sm border border-gray-200" />
    </div>
    
  
  </div>
  <div class="flex items-center justify-center p-2 bg-gray-50 dark:bg-gray-900 rounded-xl border border-gray-200 shadow-inner">
    <ZoomImg src="./images/tareas.png" class="rounded shadow-lg border border-gray-200" />
  </div>
</div>

---

# Módulo: Dashboard de Productividad 📊

Visualización de métricas en tiempo real para la toma de decisiones.

<div class="flex flex-col h-full space-y-4">
  <div class="grid grid-cols-3 gap-4 text-center">
    <div class="p-2 bg-green-500/10 rounded border border-green-500/20"><span class="block text-xl font-bold">Clientes</span><span class="text-xs opacity-70">Total Registrados</span></div>
    <div class="p-2 bg-blue-500/10 rounded border border-blue-500/20"><span class="block text-xl font-bold">Proyectos</span><span class="text-xs opacity-70">En Ejecución</span></div>
    <div class="p-2 bg-purple-500/10 rounded border border-purple-500/20"><span class="block text-xl font-bold">Tareas</span><span class="text-xs opacity-70">Pendientes/Hechas</span></div>
  </div>

  <div class="flex-grow flex items-center justify-center p-4 bg-white dark:bg-gray-800 rounded-2xl border border-gray-200 shadow-xl overflow-hidden">
    <ZoomImg src="./images/dashboard.png" class="max-h-full object-contain rounded" />
  </div>
</div>

---

# Plan de Pruebas Detallado 🛡️

Estrategia de validación en múltiples niveles.

1.  **Pruebas Unitarias:** Validación de lógica en modelos y formularios (Cobertura total en lógica core).
2.  **Pruebas de Integración:** Verificación del flujo de datos entre ORM y Vistas.
3.  **Pruebas Funcionales:** Simulación de navegación del usuario (Login -> Registro -> Dashboard).
4.  **Pruebas de Seguridad:** Validación de redirecciones y acceso restringido.

<div class="mt-4 p-4 bg-gray-900 rounded-lg font-mono text-[10px] text-green-400 shadow-2xl">
  $ python manage.py test freelance_core<br>
  Creating test database for alias 'default'...<br>
  System check identified no issues (0 silenced).<br>
  .......<br>
  ----------------------------------------------------------------------<br>
  Ran 7 tests in 6.759s<br><br>
  OK<br>
  Destroying test database for alias 'default'...
</div>

---

# Evidencias de Validación ✅

<div class="grid grid-cols-2 gap-4 h-full">
  <div class="text-xs">
    <table class="w-full">
      <thead>
        <tr class="border-b border-primary/30">
          <th class="text-left py-2">Caso de Prueba</th>
          <th class="text-left py-2">Estado</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
        <tr><td class="py-2">Registro de Usuarios</td><td class="py-2 text-green-500 font-bold">EXITOSO</td></tr>
        <tr><td class="py-2">Autenticación (Login)</td><td class="py-2 text-green-500 font-bold">EXITOSO</td></tr>
        <tr><td class="py-2">Protección de Rutas (Middleware)</td><td class="py-2 text-green-500 font-bold">EXITOSO</td></tr>
        <tr><td class="py-2">Gestión de Clientes y Proyectos</td><td class="py-2 text-green-500 font-bold">EXITOSO</td></tr>
        <tr><td class="py-2">Integridad Referencial (Cascada)</td><td class="py-2 text-green-500 font-bold">EXITOSO</td></tr>
      </tbody>
    </table>
    <div class="mt-4 p-3 bg-primary/5 border-l-4 border-primary rounded">
      <p class="font-bold text-primary">Resultado Final:</p>
      <p class="italic">100% de las pruebas críticas superadas en entorno PostgreSQL.</p>
    </div>
  </div>
  <div class="flex flex-col space-y-2">
    <p class="text-xs font-bold text-center opacity-70">Endpoints API REST</p>
    <div class="flex-grow bg-white dark:bg-gray-800 rounded border border-gray-200 p-2 shadow-inner overflow-hidden flex items-center justify-center text-sm">
      <ZoomImg src="./images/APIREST.png" class="h-full object-contain" />
    </div>
  </div>
</div>

---

# Conclusiones y Futuro 🎓

### Conclusiones
* ✅ Se desarrolló una herramienta integral, robusta y escalable.
* ✅ La arquitectura hexagonal permite una evolución técnica sin deuda técnica masiva.
* ✅ HTMX reduce la complejidad del frontend manteniendo una experiencia de alta calidad.

### Próximos Pasos (Fase 3+)
* 🤖 **IA Engine:** Predicción de tiempos basada en histórico de tareas.
* 📱 **Mobile Native:** App en Flutter para gestión on-the-go.
* 📈 **Analytics:** Reportes avanzados de rentabilidad por cliente.

---
layout: center
class: text-center
background: https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1920
---

# ¡Gracias por su atención!

**RootDev**
*Carrera de Informática Industrial - I.T.E.I.S. "Pedro Domingo Murillo"*

<div class="mt-10 flex justify-center gap-4 text-sm">
  <span>Estudiante: Armin Daniel Antonio Mendieta</span>
</div>
