# Contributing

Contributions should preserve the repository's central promise: examples must be understandable, safe by default, testable without paid credentials, and honest about uncertainty.

## Pull request requirements

- Link the change to a book page or capability area.
- Add or update offline tests.
- Do not include credentials, copyrighted datasets, customer data, or generated media without clear rights.
- Document the provider documentation URL and verification date when changing an API integration.
- Include timeout, error, rate-limit, and cost behavior for new live calls.
- Keep examples small; move reusable logic into `src/ai_api_playbook`.

Run before submitting:

```bash
python -m unittest discover -s tests -v
python -m compileall -q src examples projects
ruff check .
```
