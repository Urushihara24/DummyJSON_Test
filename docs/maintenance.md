# Maintenance notes

This repository contains a working API regression suite against the public DummyJSON contract. Keep changes focused, reproducible, and aligned with observed upstream behavior.

## Before merging

- install dependencies from `requirements.txt`;
- run `pytest -v` locally;
- keep tests independent where possible;
- avoid committing credentials, tokens, local virtual environments, or generated artifacts;
- update the README when test scope or execution steps change.

## API assumptions

The suite targets an external public API, so upstream behavior can change independently of this repository. If an assertion starts failing, verify the live API contract before changing the expected result.
