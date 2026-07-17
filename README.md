# AI APIs in Practice

**A Visual Guide to Multimodal, Agentic, and Revenue-Ready Applications**

Companion repository for the infographic book by **Faramarz Kowsari**. The project turns modern AI API capabilities into reproducible engineering patterns, offline-testable examples, and commercially realistic product blueprints.

> Status: first public engineering edition. Provider availability, model names, pricing, and regional access change frequently; consult `docs/provider-matrix.md` and each provider's official documentation before production use.

## What makes this repository different

- Capability-first organization instead of a fragile catalog of model names.
- Safe mock mode: examples run without paid credentials.
- Production patterns: timeouts, retries, redaction, idempotency, observability, evaluation, and unit economics.
- Python reference implementation plus TypeScript for browser/realtime patterns.
- Book-to-code traceability: every numbered infographic maps to a runnable example or technical note.
- Ten revenue-ready blueprints and one integrated publishing capstone.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
python -m ai_api_playbook.cli demo
python -m unittest discover -s tests -v
```

The default configuration uses deterministic mock responses. To call a provider, add the relevant key to `.env`, set `AIAP_MODE=live`, and explicitly select a provider.

## Repository map

| Path | Purpose |
|---|---|
| `src/ai_api_playbook/` | Provider-neutral core, HTTP transport, routing, RAG, safety, evaluation, and economics |
| `examples/` | Small, focused examples mapped to book pages |
| `projects/` | Commercial product blueprints and runnable proof-of-concept pipelines |
| `notebooks/` | Colab-ready learning notebooks |
| `docs/` | Provider matrix, book map, architecture, security, cost, and release guidance |
| `tests/` | Offline deterministic tests; no API key or network required |

## Capability map

1. API foundations: REST, SSE, WebSocket/WebRTC, asynchronous jobs, webhooks, batch.
2. Language and reasoning: prompting, structured outputs, tool calling, code, multimodality.
3. Agents: tools, search, code execution, computer use, MCP, multi-agent orchestration.
4. Knowledge systems: embeddings, chunking, vector stores, hybrid search, reranking, RAG evaluation.
5. Media: vision, OCR, image, speech, realtime voice, video, avatars, music and sound.
6. Production: secrets, privacy, retries, rate limiting, caching, cost controls, evals, observability.
7. Commercial systems: customer problem, measurable outcome, cost per successful job, pricing, and safeguards.

## Supported provider families

The core interface includes configurations or examples for OpenAI, Google Gemini, Anthropic Claude, Microsoft Foundry, Mistral, Hugging Face Inference Providers, Cohere, Pinecone, ElevenLabs, Deepgram, Runway, and Replicate. See `docs/provider-matrix.md` for the exact coverage and verification date.

The examples include Python integrations and a strict TypeScript WebRTC realtime client. Browser examples require a short-lived key minted by your own backend; never ship provider secrets to a client.

## Security baseline

- Never commit API keys. `.env` is ignored; `.env.example` contains names only.
- Keep privileged credentials on the server, not in browser or mobile clients.
- Use ephemeral/session credentials for client-side realtime flows when the provider supports them.
- Redact secrets and personal data from logs.
- Require human approval for high-impact actions.
- Verify webhook signatures and use idempotency keys for billable or mutating operations.

Read `SECURITY.md` before enabling live mode.

## Citation

Use the metadata in `CITATION.cff` and `.zenodo.json`. The repository URL and the author's ORCID are already configured. After a GitHub release is archived by Zenodo, add the DOI badge and DOI identifier to this README and `CITATION.cff`.

## Author

Faramarz Kowsari is an author, Software Engineer and AI researcher based in Istanbul. His work focuses on artificial intelligence, data engineering, visual education, digital publishing, and practical systems that connect knowledge to measurable outcomes.

- ORCID: https://orcid.org/0000-0003-1692-0453
- GitHub: https://github.com/FaramarzKowsari
- LinkedIn: https://www.linkedin.com/in/faramarzkowsari
- Wikidata: https://www.wikidata.org/wiki/Q140389378

## License

Code is released under the MIT License. Book text, diagrams, and visual prompt manuscript are separately licensed under CC BY 4.0 unless a file states otherwise.
