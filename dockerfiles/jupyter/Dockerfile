FROM ghcr.io/prefix-dev/pixi:latest AS build

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY .pixi/config.toml /etc/pixi/config.toml
COPY --chown=appuser:appgroup pixi.toml pixi.lock ./

RUN pixi install --frozen --no-hard-links

FROM ubuntu:24.04

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        gcc \
        g++ \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app

RUN groupadd -r appgroup && useradd -r -m -d /home/appuser -g appgroup appuser

COPY --from=build /usr/local/bin/pixi /usr/local/bin/pixi
COPY --from=build /etc/pixi/config.toml /etc/pixi/config.toml
COPY --from=build /opt/pixi/envs /opt/pixi/envs
COPY --chown=appuser:appgroup pixi.toml pixi.lock ./
COPY --chown=appuser:appgroup . .

USER appuser

EXPOSE 8888

CMD ["pixi", "run", "lab"]
