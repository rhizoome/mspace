FROM alpine:3.15
RUN apk add --no-cache \
    py3-pip \
    py3-cryptography
RUN pip install poetry
RUN adduser -D user
USER user
WORKDIR /code
COPY --chown=user:user poetry.lock pyproject.toml /code/
RUN poetry install --no-dev
COPY --chown=user:user . /code/
CMD poetry run hypercorn -w 1 -b 0.0.0.0:80 mspace:app
