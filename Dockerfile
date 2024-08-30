FROM alpine:latest
RUN apk add --no-cache \
    py3-pip \
    py3-cryptography
RUN pip install poetry
RUN adduser -D user
USER user
COPY --chown=user:user . /code/
WORKDIR /code
RUN poetry install --no-dev
CMD poetry run hypercorn -w 1 -b 0.0.0.0:80 mspace:app
