"""Book pages 50-66: invoke a versioned model hosted on Replicate."""

from __future__ import annotations

import os


def run(model_version: str, prompt: str):
    import replicate

    return replicate.run(model_version, input={"prompt": prompt})


if os.getenv("AIAP_MODE", "mock") == "live":
    print(run(os.environ["REPLICATE_MODEL_VERSION"], "A precise educational diagram"))
else:
    print("MOCK: pin a version for reproducible outputs")
