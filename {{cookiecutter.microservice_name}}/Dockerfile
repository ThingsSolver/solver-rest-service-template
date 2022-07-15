FROM thingsolver/solver-base:1.1

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /

ADD requirements.txt /
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ADD app /app
ADD tests /tests
ADD run_server.sh /

RUN chown -R app:root /app /tests run_server.sh requirements.txt && \
    chmod -R g=u /app /tests run_server.sh requirements.txt

USER app

EXPOSE 8080