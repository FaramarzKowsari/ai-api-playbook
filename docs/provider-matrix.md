# Provider matrix

**Last verified: 17 July 2026.** Capabilities and model identifiers change. Follow official documentation and pin tested versions before production deployment.

| Provider | Primary interface covered | Best represented capability | Live example |
|---|---|---|---|
| OpenAI | Responses, Realtime, Images, Embeddings | unified agentic and multimodal workflows | `examples/01_text/openai_responses.py` |
| Google | Gemini Interactions, Live, media | long-context multimodal and tools | `examples/01_text/gemini_interactions.py` |
| Anthropic | Messages and tool use | reasoning, tools, code and MCP | `examples/01_text/anthropic_messages.py` |
| Microsoft | Foundry model inference | enterprise endpoint, identity and governance | `examples/01_text/microsoft_foundry.py` |
| Mistral | Chat, Agents, OCR, embeddings | document intelligence | `examples/04_documents/mistral_ocr.py` |
| Hugging Face | Inference Providers | open-model routing | `examples/06_gateways/huggingface_router.py` |
| Cohere | Rerank | retrieval quality | `examples/07_search/cohere_rerank.py` |
| Pinecone | Vector database | semantic retrieval and filters | `examples/07_search/pinecone_vector_store.py` |
| ElevenLabs | TTS, STT, dubbing, agents | voice and audio generation | `examples/05_media/elevenlabs_tts.py` |
| Deepgram | STT, TTS, Voice Agent | realtime speech pipelines | `examples/05_media/deepgram_stt.py` |
| Runway | asynchronous media tasks | image/video generation and editing | `examples/05_media/runway_video.py` |
| Replicate | versioned hosted models | specialist and community models | `examples/06_gateways/replicate_model.py` |

## Official sources

- OpenAI: https://developers.openai.com/api/docs
- Gemini: https://ai.google.dev/gemini-api/docs
- Claude: https://platform.claude.com/docs
- Microsoft Foundry: https://learn.microsoft.com/azure/foundry/
- Mistral: https://docs.mistral.ai/
- Hugging Face: https://huggingface.co/docs/inference-providers/
- Cohere: https://docs.cohere.com/
- Pinecone: https://docs.pinecone.io/
- ElevenLabs: https://elevenlabs.io/docs/api-reference/introduction
- Deepgram: https://developers.deepgram.com/docs
- Runway: https://docs.dev.runwayml.com/
- Replicate: https://replicate.com/docs
