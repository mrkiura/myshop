FROM python:3.9

RUN addgroup --system app && adduser --system --group app

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./app/pyproject.toml ./app/poetry.lock* /app/

ARG INSTALL_DEV=false

RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY ./app /app
RUN chmod +x run.sh

ENV PYTHONPATH=/app

RUN chown -R app:app $HOME

USER app

CMD ["./run.sh"]
