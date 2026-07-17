# Security policy

## Supported version

Security fixes are applied to the latest release line.

## Reporting

Do not open public issues containing credentials, personal data, exploit payloads, or customer records. Report a vulnerability privately through the repository's GitHub Security Advisory interface.

## Deployment checklist

1. Store provider keys in a managed secret store.
2. Never expose long-lived keys to browsers, mobile clients, notebooks, logs, or screenshots.
3. Set explicit request timeouts, concurrency caps, retry limits, and budget alarms.
4. Verify webhook signatures and reject stale timestamps.
5. Use idempotency keys for retries that can create charges or mutate state.
6. Redact authorization headers, cookies, access tokens, email addresses, phone numbers, and document identifiers from logs.
7. Treat model output as untrusted input; validate it before database writes or tool execution.
8. Restrict tool permissions and require human approval for purchases, deletion, publication, messages, or account changes.
9. Defend RAG and agent systems against prompt injection in retrieved content.
10. Obtain explicit consent before voice cloning, biometric processing, recording, or impersonation-adjacent workflows.

The examples are educational reference implementations, not a substitute for a threat model or compliance review.
