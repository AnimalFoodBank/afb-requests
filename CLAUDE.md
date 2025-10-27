# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Animal Food Bank (AFB) Requests is a full-stack web application for managing food requests and deliveries. The application consists of:

- **Backend API**: Django 5.1 + Django Rest Framework with PostgreSQL 15
- **Frontend UI**: Nuxt 3 (Vue 3) with Tailwind CSS, running as a client-side SPA
- **Deployment**: Caddy Server as reverse proxy with automatic HTTPS

## Development Commands

### Backend (Django API)

The Django API lives in `apps/api/`. All Django management commands must be run from that directory or use the pnpm wrapper.

```bash
# Via pnpm (recommended - handles PYTHONPATH automatically)
pnpm django <command>                    # General Django command wrapper
pnpm django:run                          # Run dev server with SQL logging
pnpm django:shell                        # Django shell with shell_plus
pnpm django:test                         # Run Django tests

# Direct Django commands (from project root)
PYTHONPATH=$(pwd) python apps/api/manage.py <command>
PYTHONPATH=$(pwd) python apps/api/manage.py runserver_plus --print-sql
PYTHONPATH=$(pwd) python apps/api/manage.py shell_plus
PYTHONPATH=$(pwd) python apps/api/manage.py createsuperuser
PYTHONPATH=$(pwd) python apps/api/manage.py makemigrations
PYTHONPATH=$(pwd) python apps/api/manage.py migrate

# Rollback database to empty state
PYTHONPATH=$(pwd) python apps/api/manage.py migrate afbcore zero

# Run tests (pytest is configured)
pytest                                    # All tests
pytest apps/api/afbcore/tests/           # Specific directory
pytest -k test_name                       # Specific test
```

**Important**: Django settings module is `afb.settings`. The Django project is named `afb`, the main app is `afbcore`.

### Frontend (Nuxt/Vue)

The Nuxt application lives in `apps/ui/`.

```bash
pnpm dev                                  # Start Nuxt dev server
pnpm build                                # Build for production
pnpm lint                                 # Run ESLint
pnpm typecheck                            # Type check with vue-tsc
```

### Code Quality

```bash
# Python linting
ruff check apps/api/                      # Check for issues
ruff format apps/api/                     # Format code

# Pre-commit hooks
pre-commit run --all-files                # Run all hooks
```

## Architecture

### Backend Architecture

**Core Models** (`apps/api/afbcore/models/`):
- `User` & `Profile`: Extended Django auth with phone numbers and user profiles
- `FoodRequest`: Central entity for food assistance requests
- `Delivery`: Delivery scheduling and tracking
- `DeliveryRegion`: Geographic delivery zones
- `Branch`: AFB branch locations
- `Pet`: Pet information associated with requests
- `FoodAvailable`: Food inventory tracking

**API Structure**:
- ViewSets in `apps/api/afbcore/views/` (e.g., `FoodRequestViewSet`, `ProfileViewSet`)
- Serializers in `apps/api/afbcore/serializers/`
- URL routing in `apps/api/afb/urls/`
- Custom permissions in `apps/api/afbcore/permissions.py`
- Signals for lifecycle hooks in `apps/api/afbcore/signals.py`

**Authentication**:
- Token-based authentication (DRF TokenAuthentication)
- Passwordless authentication via `drfpasswordless` (forked version)
- Custom registration endpoint at `/api/v1/register/`
- Current user endpoint at `/api/v1/current_user/`

**API Versioning**:
- URL path versioning (e.g., `/api/v1/`)
- Current version: `v1`
- Configured in `REST_FRAMEWORK['DEFAULT_VERSION']`

**Database**:
- PostgreSQL 15 in production
- Settings loaded from environment variables via `python-dotenv`
- Database URL configured via `DATABASE_URL` env var

**Testing**:
- Pytest with `pytest-django` and `pytest-xdist`
- Test files follow `test_*.py` or `*_test.py` pattern
- Tests in `apps/api/afbcore/tests/` and `apps/api/tests/`
- Custom test runner: `afb.test_runner.PytestTestRunner`
- Run with `--keepdb` to preserve test database between runs

### Frontend Architecture

**Framework Setup**:
- Nuxt 3 configured for client-side rendering only (`ssr: false`)
- Uses Nuxt UI Pro and @nuxt/ui for components
- Vueform for advanced form handling
- Pinia for state management
- Sidebase nuxt-auth for authentication
- Tailwind CSS for styling

**Key Configurations**:
- Main config: `apps/ui/nuxt.config.ts`
- Tailwind: `apps/ui/tailwind.config.ts`
- Vueform: `apps/ui/vueform.config.ts`
- TypeScript: `apps/ui/tsconfig.json`

**Directory Structure**:
- `apps/ui/pages/`: File-based routing
- `apps/ui/components/`: Vue components
- `apps/ui/composables/`: Composable functions
- `apps/ui/layouts/`: Layout templates
- `apps/ui/stores/`: Pinia stores
- `apps/ui/types/`: TypeScript type definitions

**API Integration**:
- Base API URL configured via `NUXT_PUBLIC_API_BASE` environment variable
- Default dev: `https://dev.afb.pet/`
- Uses Axios for HTTP requests

### Cross-Stack Conventions

**CORS Configuration**:
- Configured for development origins (`http://127.0.0.1:3000`, `http://127.0.0.1:8000`)
- Production origins: `https://dev.afb.pet`, `https://staging.afb.pet`
- CSRF trusted origins match CORS origins
- Credentials allowed for cookie-based auth

**Environment Variables**:
- Backend uses `.env` file loaded via `python-dotenv`
- Frontend uses `.env` with `NUXT_` prefixed variables
- Example configuration in `.env.example`
- Never commit `.env` files

## Development Workflow

### Running Full Stack Locally

1. **Start PostgreSQL** (ensure running on default port or set `DATABASE_URL`)
2. **Start Django API**:
   ```bash
   pnpm django:run
   # API runs on http://127.0.0.1:8000
   ```
3. **Start Nuxt UI** (in separate terminal):
   ```bash
   pnpm dev
   # UI runs on http://127.0.0.1:3000
   ```

### Common Development Tasks

**Creating a new Django model**:
1. Add model to `apps/api/afbcore/models/`
2. Export in `apps/api/afbcore/models/__init__.py`
3. Create migration: `pnpm django makemigrations`
4. Apply migration: `pnpm django migrate`
5. Register in admin: `apps/api/afbcore/admin.py`
6. Create serializer in `apps/api/afbcore/serializers/`
7. Create viewset in `apps/api/afbcore/views/`
8. Register routes in `apps/api/afb/urls/`

**Testing email in development**:
- Use Mailpit: `pnpm mailpit`
- Web interface: http://127.0.0.1:8025/
- SMTP server: localhost:1025

**Accessing Django admin**:
- Create superuser: `pnpm django createsuperuser`
- Visit: http://127.0.0.1:8000/afbadmin/
- Uses Django Unfold theme

**API Documentation**:
- Swagger UI: http://127.0.0.1:8000/api/v1/schema/swagger-ui/
- ReDoc: http://127.0.0.1:8000/api/v1/schema/redoc/
- OpenAPI schema: http://127.0.0.1:8000/api/v1/schema/
- Powered by drf-spectacular

## Code Style

### Python (Backend)

- Line length: 80 characters (Black/Ruff configuration)
- Use Ruff for linting and formatting
- Import order: stdlib, third-party, local (enforced by isort config)
- Type hints encouraged but not required
- Follow Django naming conventions (PascalCase for models/classes, snake_case for functions/variables)

### JavaScript/TypeScript (Frontend)

- Line length: 80 characters (Prettier configuration)
- Use Prettier for formatting
- ESLint with Nuxt config
- Prefer composition API over options API for Vue components
- Use TypeScript for type safety

## Special Notes

### Custom Dependencies

The project uses forked versions of some dependencies:
- `djangorestframework`: Custom fork with specific patches
- `drfpasswordless`: Custom fork for passwordless authentication

Both are installed from Git repositories (see `pyproject.toml`).

### Security Considerations

- Token expiration: 1 week (`TOKEN_EXPIRED_AFTER_WEEKS`)
- CSRF protection configured for CORS setup
- Session and CSRF cookies secure in production only
- Rate limiting configured via DRF throttling (60 signups/hour per IP)

### Production Deployment

- Static files collected to `/var/www/public/static`
- Gunicorn as WSGI server for Django
- Caddy Server handles reverse proxy and automatic HTTPS
- Debug mode controlled via `DEBUG` environment variable
