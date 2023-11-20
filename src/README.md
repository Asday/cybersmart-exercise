# `src/`

This directory contains only the source code for the project, with no particular opinion on how to run it, test it, or deploy it.

# Files

Path | Description
-|-
[`_/`](_/) | Django project settings.
[`completed_tasks/`](completed_tasks/) <br /> [`locations/`](locations/) <br /> [`tasks/`](tasks/) <br /> [`weather_reports/`](weather_reports/) | Django applications for the sole purpose of holding a model (and associated querysets, managers, and templates) each.  All contain a generic `admin.py` to automatically populate the admin, and a `models` module with a single file named after the model.  This granularity eases migration conflicts when merging long-lived branches, and allows for easy filename-based navigation to a model's definition.
[`wait_for_db/`](wait_for_db/) | Self-contained app providing a management command that blocks until the database is awake and ready, or times out and returns a non-zero exit code.
[`website/`](website/) | Django application to contain the frontend business logic and non-model-related templates.
