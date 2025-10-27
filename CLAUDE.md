# CLAUDE.md

Guidance for Claude Code when working with this repository.

## Project Overview

Animal Food Bank (AFB) Requests is a full-stack web application for managing food requests and deliveries.

- **Backend**: Django 5.1 + Django Rest Framework with PostgreSQL
- **Frontend**: Nuxt 3 (Vue 3) SPA with Tailwind CSS
- **Deployment**: Caddy Server with automatic HTTPS

## Essential Context

### Django Project Structure

**Critical non-discoverable facts:**
- Django project name: `afb`
- Main Django app: `afbcore`
- Settings module: `afb.settings`
- Backend code location: `apps/api/`
- Frontend code location: `apps/ui/`

**PYTHONPATH requirement:** When running Django commands directly (not via pnpm), you must set `PYTHONPATH=$(pwd)` from the project root:
```bash
PYTHONPATH=$(pwd) python apps/api/manage.py <command>
```

### Authentication Pattern

Uses **passwordless authentication** via a forked `drfpasswordless` package. Token-based authentication with DRF TokenAuthentication.

### API Versioning

URL path versioning with current version `v1` (e.g., `/api/v1/`). See `apps/api/afb/settings.py` for REST_FRAMEWORK configuration.

## Sources of Truth

Refer to these canonical sources instead of duplicating information:

- **Backend dependencies**: `pyproject.toml`
- **Frontend dependencies & scripts**: `package.json`
- **Django configuration**: `apps/api/afb/settings.py`
- **Nuxt configuration**: `apps/ui/nuxt.config.ts`
- **API routes**: `apps/api/afb/urls/`
- **Models**: `apps/api/afbcore/models/`

## Development Commands

Use pnpm scripts (defined in `package.json`):
```bash
pnpm django <command>     # Django wrapper (handles PYTHONPATH)
pnpm django:run           # Start Django dev server
pnpm dev                  # Start Nuxt dev server
pnpm lint                 # Run linters
pnpm typecheck            # TypeScript type checking
```

## Key Architectural Patterns

### Backend (Django)

Follows standard Django Rest Framework patterns:
- **Models**: `apps/api/afbcore/models/`
- **ViewSets**: `apps/api/afbcore/views/`
- **Serializers**: `apps/api/afbcore/serializers/`
- **Permissions**: `apps/api/afbcore/permissions.py`
- **URL routing**: `apps/api/afb/urls/`

**Testing**: Pytest with custom runner `afb.test_runner.PytestTestRunner`

### Frontend (Nuxt)

Standard Nuxt 3 structure with client-side rendering (`ssr: false`):
- **Pages**: `apps/ui/pages/` (file-based routing)
- **Components**: `apps/ui/components/`
- **Stores**: `apps/ui/stores/` (Pinia)
- **Types**: `apps/ui/types/`

**Key libraries**: Nuxt UI Pro, Vueform, @nuxt/ui

## Development Workflow

1. Start PostgreSQL (or set `DATABASE_URL`)
2. Run backend: `pnpm django:run`
3. Run frontend: `pnpm dev` (separate terminal)

**Admin access**: Create superuser with `pnpm django createsuperuser`, visit `/afbadmin/`

**API docs**: Available at `/api/v1/schema/swagger-ui/` (powered by drf-spectacular)

## Code Style

- **Python**: 80 char line length, Ruff for linting/formatting
- **TypeScript**: 80 char line length, Prettier + ESLint
- **Vue**: Composition API preferred

## Custom Dependencies

Two forked packages (see `pyproject.toml`):
- `djangorestframework`: Custom patches
- `drfpasswordless`: Passwordless authentication
