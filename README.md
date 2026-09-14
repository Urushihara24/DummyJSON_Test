# API Tests for DummyJSON

> QA automation practice project focused on API checks, reusable pytest fixtures, negative scenarios, and CI.

A set of automated tests for the public DummyJSON API (`Auth` and `Carts` endpoints), written with Python and pytest.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pytest-34A853?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest">
  <img src="https://img.shields.io/badge/Requests-HTTP-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Requests">
  <img src="https://img.shields.io/badge/GitHub_Actions-CI-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

| Coverage | Design | Stack |
|---|---|---|
| Authentication and cart CRUD, including negative authorization and missing-resource scenarios | Reusable fixtures and independent tests that assert status codes and response contracts | Python 3.12, pytest, requests |

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Coverage

- **Auth:** successful and failed login, profile retrieval with and without a token.
- **Carts:** retrieve, create, update, and delete a cart.
- **Negative paths:** invalid credentials, missing authorization, and a nonexistent resource.

## Project structure

```text
DummyJSON_Test/
├── tests/
│   ├── test_auth.py      # Authentication tests
│   └── test_carts.py     # Cart tests
├── conftest.py           # pytest fixtures, including token retrieval
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

## Implementation notes

- DummyJSON is a fake API backed by an in-memory database.
- When a cart is deleted, the API marks it as `isDeleted: true` instead of physically removing it.
- PUT requests use `merge: true` to merge cart items correctly.
- Tests are independent of each other except for the token fixture.

## API behavior notes

During the assignment, several DummyJSON behavior details were discovered and reflected in the tests:

- The API returns `accessToken` instead of the expected `token`, so the tests follow the actual response schema.
- An invalid password returns `400 Bad Request` instead of the more typical `401 Unauthorized`, and the negative check accounts for that behavior.
