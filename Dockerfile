FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 AIAP_MODE=mock
WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN pip install --no-cache-dir .
COPY examples ./examples
COPY projects ./projects
CMD ["python", "-m", "ai_api_playbook.cli", "demo"]
