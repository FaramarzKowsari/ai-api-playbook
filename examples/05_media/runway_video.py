"""Book pages 61-66: asynchronous Runway video job pattern.

SDK shapes change; verify against https://docs.dev.runwayml.com/ before live use.
"""

from __future__ import annotations

import os
import time


def create_and_wait(prompt: str) -> str:
    from runwayml import RunwayML

    client = RunwayML(api_key=os.environ["RUNWAYML_API_SECRET"])
    task = client.image_to_video.create(model="gen4.5", prompt_text=prompt, ratio="1280:720", duration=5)
    while True:
        current = client.tasks.retrieve(task.id)
        if current.status == "SUCCEEDED":
            return current.output[0]
        if current.status == "FAILED":
            raise RuntimeError(current.failure)
        time.sleep(2)


print("MOCK: queued -> processing -> succeeded" if os.getenv("AIAP_MODE", "mock") != "live" else create_and_wait("A clean data-flow animation"))
