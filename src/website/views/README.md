# `src/website/views/`

This directory is a Python module containing all views for the project.  Each file contains a single eponymous class for easy filename-based navigation to a definition and shorter import blocks.

# Files

Path | Description
-|-
[`mixins/`](mixins/) | Python module containing view mixins for the project.
`TaskCreate.py` | Creation view for [`Task`s](../../tasks/models/Task.py).
`TaskDetail.py` | Detail view for [`Task`s](../../tasks/models/Task.py).
`Tasks.py` | List view for [`Task`s](../../tasks/models/Task.py), which also serves as the homepage.
`TaskUpdate.py` | Update view for [`Task`s](../../tasks/models/Task.py).
