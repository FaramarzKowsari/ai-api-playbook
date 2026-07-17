# Multilingual AI Publishing & Knowledge Commerce Engine

The capstone converts an authorized manuscript into a reviewable publishing package. It does **not** publish automatically.

## Pipeline

1. Validate ownership, file type, size, and malware-scanning status.
2. Extract text, hierarchy, tables, images, and page provenance.
3. Produce book metadata as schema-validated JSON.
4. Generate grounded summaries and keyword candidates.
5. Create language-specific launch copy; do not treat translation as final editorial review.
6. Build a cited RAG index with page and section metadata.
7. Produce audio, image, video, and social asset briefs.
8. Run factual, policy, cost, and privacy checks.
9. Export a human-review package for Google Books, Zenodo, GitHub, and social channels.

## Run the offline proof of concept

```bash
python projects/publishing_engine/pipeline.py
```

The proof of concept uses deterministic local extraction and mock AI output. Live adapters can be added behind the same stage boundaries.
