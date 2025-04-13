FROM python:3.13.2-slim

RUN apt-get update && apt-get install -y build-essential

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app
COPY . /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv venv && uv sync

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
