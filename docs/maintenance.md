# Maintenance notes

This repository is a small QA automation practice project. Keep changes focused and reproducible.

## Before merging

- install dependencies from `requirements.txt`;
- run `pytest -v` locally;
- keep tests independent where possible;
- avoid committing credentials, tokens, local virtual environments, or generated artifacts;
- update the README when test scope or execution steps change.

## API assumptions

The suite targets the public DummyJSON API, so upstream behavior can change independently of this repository. If an assertion starts failing, verify the live API contract before changing the expected result.
