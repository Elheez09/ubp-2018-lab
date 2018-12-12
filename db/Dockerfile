FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD="emauzumaki09"
ENV MYSQL_USER="zumakiem"
ENV MYSQL_PASSWORD="zumakiem"
ENV MYSQL_DATABASE="users"

COPY users.sql /docker-entrypoint-initdb.d
