FROM prom/prometheus
COPY ./prometheus.yml /etc/prometheus/
RUN chgrp -R 0 /run && chmod -R g=u /run
EXPOSE 9090