# SaaS para Freelancers - MVP

Este es el Producto Mínimo Viable (MVP) para una plataforma de gestión de freelancers y agencias pequeñas.

## 🚀 Tecnologías
- **Backend:** Django 4.2+ & Django REST Framework
- **Base de Datos:** PostgreSQL (Configurada)
- **PDFs:** WeasyPrint
- **Contenedores:** Docker

## 🛠️ Módulos Implementados
1.  **Clientes (CRM):** Gestión de contactos y empresas.
2.  **Proyectos:** Seguimiento de estados (Activo, Completado, etc.).
3.  **Tareas:** Kanban simple con prioridades y fechas de entrega.
4.  **Facturación:** Generación de facturas y **exportación a PDF**.
5.  **Dashboard:** Métricas básicas (ingresos pendientes, proyectos activos).

## 🏃 Cómo ejecutar (Docker)
Si tienes `docker` y `docker-compose` instalados:

```bash
docker-compose up --build
```

Si prefieres usar `docker compose` (v2):
```bash
docker compose up --build
```

## 🏃 Cómo ejecutar (Local - Desarrollo rápido)
Si prefieres probarlo localmente con SQLite primero:
1. Crea un entorno virtual: `python -m venv venv`
2. Actívalo: `source venv/bin/activate`
3. Instala dependencias: `pip install -r backend/requirements.txt`
4. Cambia `DATABASES` en `backend/config/settings.py` a SQLite temporalmente si no tienes Postgres a mano.
5. Migra: `python backend/manage.py migrate`
6. Crea superusuario: `python backend/manage.py createsuperuser`
7. Inicia: `python backend/manage.py runserver`

## 🔗 Endpoints Principales
- **Admin:** `/admin/`
- **API Base:** `/api/`
- **Dashboard:** `/api/dashboard/`
- **Descargar PDF Factura:** `/api/invoices/<id>/download_pdf/`

## 🤖 Próximos Pasos (IA)
- Integrar OpenAI/Anthropic para generar propuestas automáticas basadas en una descripción corta.
- Clasificación de clientes por potencial usando lógica simple o IA.
