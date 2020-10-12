ARG ARCH="amd64"
ARG OS="linux"

FROM prom/prometheus

ARG ARCH="amd64"
ARG OS="linux"
COPY ./prometheus.yml /etc/prometheus/

RUN mkdir -p /prometheus && \
    chown -R nobody:nogroup /etc/prometheus /prometheus

USER nobody
EXPOSE 9090