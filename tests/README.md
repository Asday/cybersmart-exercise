# Tests

Tests are run in docker by `pytest` using the convenience script [`ci`](../bin/ci).  The docker container is separate from the regular Python docker container in the same way the test code is separate from the code under test.

# Files

Path | Description
-|-
`main.py` | Tests yet to be categorised into their own modules.
`pytest.ini` | Configuration for the test runner.
`stories.py` | Integration tests as described by the [brief](../docs/brief.pdf)
