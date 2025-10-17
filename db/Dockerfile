FROM mysql:latest

ENV MYSQL_DATABASE=db_site_velik
ENV MYSQL_ROOT_PASSWORD=root

COPY . /docker-entrypoint-initdb.d/

RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/

EXPOSE 3306