# Security Policy

## Scope

Security reports are welcome for issues in the API test harness, dependency chain, CI configuration, fixtures, or credential/data handling that could make the suite unsafe to run or expose sensitive local information.

This repository targets the public DummyJSON API and should not require private production credentials.

## Reporting

Do **not** put real credentials, cookies, authorization headers, personal data, or exploit details in a public issue.

Use GitHub private vulnerability reporting when it is available for this repository. If a private report is not available, send a sanitized summary through the work contact listed on the maintainer profile.

A useful report includes:

- affected commit and Python version;
- minimal reproduction steps;
- expected vs actual behavior;
- whether CI, dependency integrity, auth fixtures, or local data are affected;
- logs with tokens/cookies removed.

## Test-data boundary

Tests and fixtures must use only public/demo data appropriate for DummyJSON. Secrets, private account data, generated local credential files, and environment-specific artifacts must remain outside Git.