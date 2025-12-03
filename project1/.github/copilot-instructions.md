# Copilot instructions for the IronX Fitness (project1) repository

These instructions help AI coding agents be productive in this Django project. Keep guidance actionable and specific to patterns found in the codebase.

- Project type: Django 3.2 app (single-project layout).
  - Root Django project: `project1/` (settings in `project1/settings.py`).
  - Main app: `authapp/` (models, views, templates live here).
  - Database: SQLite by default (`db.sqlite3` in repository root).
  - Static + media: static files in `static/`, collected to `staticfiles/`; uploaded media in `media/`.

- Quick dev commands (Windows PowerShell):
  - Install dependencies (assumes Python 3.8+ virtualenv created and activated):

    python -m pip install -r requirements.txt  # (if repository adds requirements)

  - Run migrations & check project:

    python manage.py migrate ; python manage.py check

  - Run dev server (binds to localhost:8000):

    python manage.py runserver

- Architecture & conventions (concrete, discoverable rules):
  - Templates: project-level `templates/` is included via `TEMPLATES.DIRS` and uses Django template tags and `{% load static %}`. Example: `templates/base.html` defines header/nav and includes many assets under `static/assets/...`.
  - App layout: `authapp` contains models for Category/Product/Customer/Trainer/Enrollment/etc. Views are function-based, not class-based. Use `authapp.views` examples when adding new views (patterns: `render(request, 'template.html', context)`, `get_object_or_404`, `messages` usage).
  - URL patterns: The project `ROOT_URLCONF` is `project1.urls` (edit that file to wire new endpoints). Follow existing paths (e.g., `/products/`, `/trainer`, `/gallery`, `/signup`).
  - Authentication: Uses Django's built-in `User` model; usernames are phone numbers in this project. Look at `signup` and `handlelogin` in `authapp/views.py` for validation patterns (phone numbers must be 10 digits, email uniqueness checks using `User.objects.get`).
  - File uploads: `ImageField` fields use `upload_to` paths like `products/`, `trainer/`, `gallery/`. `MEDIA_ROOT`/`MEDIA_URL` are configured in settings. When writing forms or testing uploads, ensure `MEDIA_ROOT` is writable and served in dev (`urlpatterns` in `project1/urls.py` likely needs `static()` in DEBUG).
  - Messages framework: Project maps `messages.ERROR` to Bootstrap `danger` via `MESSAGE_TAGS` in `settings.py`. Views call `messages.success`, `messages.warning`, `messages.error`, etc. Use these for user feedback.

- Patterns to follow (concrete examples):
  - Database lookups: prefer `get_object_or_404(Model, id=...)` as in `product_detail`.
  - Filtering: `Product.objects.filter(is_available=True)` and `Category.objects.all()` patterns are used in `product_list` to populate context with `categories` and `products`.
  - Authentication guard: check `request.user.is_authenticated` before protected views (see `attendance`, `profile`, `enroll`). Redirect to `/login` and add `messages.warning` like existing views.
  - Form POST handling: use `request.method == 'POST'`, read fields with `request.POST.get(...)`, create model instances and `.save()` as in `enroll`, `contact`, `attendance`.
  - Error handling: Views sometimes print exceptions and show friendly messages using `messages.error` or `messages.warning` (example in `product_list`). Keep this pattern for small recoverable errors. For unhandled exceptions, prefer letting errors surface during development.

- Tests & linting
  - There are no tests in the repository root besides `authapp/tests.py` (empty). When adding tests, use Django's TestCase in `authapp/tests.py` and run `python manage.py test`.

- Useful files to reference when changing behavior
  - `project1/settings.py` — static/media configuration, INSTALLED_APPS, TEMPLATES
  - `authapp/models.py` — all model definitions (Category, Product, Enrollment, Trainer, etc.)
  - `authapp/views.py` — canonical patterns for auth, messages, CRUD, template rendering
  - `templates/base.html` — central layout, static include patterns, navigation routes used elsewhere
  - `manage.py` — usual Django management entrypoint

- Integration points & external dependencies
  - Frontend assets reference vendor JS/CSS from `static/assets/vendor/*` — do not remove those references without updating `templates`.
  - The site relies on Django's messages and auth frameworks; avoid introducing a separate auth flow without updating templates and views.

- When modifying models
  - Add migrations: run `python manage.py makemigrations` then `python manage.py migrate`. Commit migration files under `authapp/migrations/`.
  - Be conservative with changing existing field types used in templates (e.g., product image fields, enrollment phone formats) — update templates and view code accordingly.

- Debugging tips (project-specific)
  - Views use prints for lightweight debugging (e.g., `print(products.count())` and `print(posts)` in `profile`) — replicate this style for quick local debugging but remove before committing if noisy.
  - To inspect media/static serving issues, check `STATICFILES_DIRS`, `STATIC_ROOT`, and `MEDIA_ROOT` in `project1/settings.py`.

- Examples to copy from repo
  - Signup validation snippet (from `authapp/views.py`): phone length enforcement (10 digits) and duplicate username/email checks before `User.objects.create_user(...)`.
  - Product listing filtering (from `product_list`): show how categories are passed into template and filtered by `category_id`.

- Safety & secrets
  - `SECRET_KEY` is currently in `settings.py`; do not publish or push to public repositories. Prefer using environment variables for production deployments.

- Merge guidance (if `.github/copilot-instructions.md` already exists)
  - Preserve any existing agent rules that are specific (exception handling, test commands). Merge new content above, but do not duplicate commands.

If anything here is unclear or you want me to include additional examples (URLs, specific templates, or tests), tell me what to add and I'll iterate.