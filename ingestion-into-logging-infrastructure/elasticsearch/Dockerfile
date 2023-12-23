ARG ELK_VERSION
FROM docker.elastic.co/elasticsearch/elasticsearch:${ELK_VERSION}
COPY scripts/docker-healthcheck .
HEALTHCHECK CMD sh ./docker-healthcheck

