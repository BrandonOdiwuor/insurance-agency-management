FROM postgres:12.4-alpine

ADD scripts/postgress_extension_installation.sh /docker-entrypoint-initdb.d/
RUN chmod 755 /docker-entrypoint-initdb.d/postgress_extension_installation.sh