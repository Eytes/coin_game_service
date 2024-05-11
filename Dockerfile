FROM python:3.12-slim as builder
WORKDIR /coin_game_service
RUN apt update \
    && apt upgrade -y  \
    && pip install --no-cache-dir --upgrade poetry
COPY poetry.lock pyproject.toml ./
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt


FROM python:3.12-slim
RUN groupadd -r coin_game_service && useradd --no-log-init -r -g coin_game_service coin_game_service
USER coin_game_service
WORKDIR /coin_game_service
COPY --from=builder /coin_game_service/requirements.txt ./requirements.txt
RUN apt update \
    && apt upgrade -y \
    && pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./ ./
EXPOSE 8080
CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]