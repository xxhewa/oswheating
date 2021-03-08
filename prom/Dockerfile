FROM prom/prometheus
COPY ./prometheus.yml /etc/prometheus/
ENTRYPOINT ["tail", "-f", "/dev/null"]
EXPOSE 9090