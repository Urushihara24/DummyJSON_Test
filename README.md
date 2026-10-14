# DummyJSON API Regression Suite

Working API QA automation suite for the public DummyJSON contract, focused on authentication, cart flows, negative authorization scenarios, reusable pytest fixtures, and repeatable CI execution.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pytest-34A853?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest">
  <img src="https://img.shields.io/badge/Requests-HTTP-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Requests">
  <a href="https://github.com/Urushihara24/DummyJSON_Test/actions/workflows/tests.yml"><img src="https://github.com/Urushihara24/DummyJSON_Test/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
</p>

| Coverage | Test design | Stack |
|---|---|---|
| Authentication and cart CRUD, including negative authorization and missing-resource scenarios | Reusable fixtures, independent checks, HTTP/status validation and response-contract assertions | Python 3.12 · pytest · requests · GitHub Actions |

## Coverage

- **Authentication:** successful/failed login, authenticated profile retrieval, unauthorized access.
- **Carts:** read, create, update and delete flows.
- **Negative paths:** invalid credentials, missing authorization and nonexistent resources.
- **Contract behavior:** assertions follow the actual upstream response schema instead of assuming conventional status codes or field names.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Project structure

```text
DummyJSON_Test/
├── tests/
│   ├── test_auth.py      # authentication and authorization checks
│   └── test_carts.py     # cart API checks
├── conftest.py           # reusable pytest fixtures
├── integration-fixture/  # integration support data
├── docs/                 # maintenance notes
├── requirements.txt
└── README.md
```

## API behavior captured by the suite

The automated checks intentionally reflect observed upstream behavior:

- login returns `accessToken` rather than a generic `token` field;
- invalid passwords currently return `400 Bad Request`;
- cart deletion is represented by `isDeleted: true` instead of physical removal;
- cart updates require the API's merge semantics.

These details are treated as external contract behavior. If upstream behavior changes, the live API contract is verified before expected results are updated.

## Engineering notes

- credentials and generated local artifacts are excluded from Git;
- shared setup is isolated in pytest fixtures;
- CI executes the suite on repository changes;
- tests are kept independent where the API allows it;
- negative checks validate both authorization behavior and missing-resource handling.

## Maintenance

Pre-merge and upstream-contract checks are documented in [`docs/maintenance.md`](docs/maintenance.md).

---

## Related work

- **[Auto-Pricing Bot](https://github.com/Urushihara24/monitoring-bot)** — production marketplace automation with Telegram control, seller APIs, Docker and safety guards.
- **[Commercial AI SaaS QA](https://github.com/Urushihara24/commercial-ai-saas-qa)** — sanitized commercial QA case with 150+ checks and selected defects.
- **[GitHub profile](https://github.com/Urushihara24)** — selected QA and Python engineering work.
