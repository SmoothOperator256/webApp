# syntax=docker/dockerfile:1
FROM mysql


# Configure database

COPY configureDB.sql /docker-entrypoint-initdb.d

# Final configuration
EXPOSE 3306

