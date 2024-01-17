FROM python:3.10.12-slim
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
WORKDIR /nova-test
COPY poetry.lock pyproject.toml /nova-test/

RUN pip install --upgrade --no-cache-dir pip==23.1.2 && \
    pip install -U --no-cache-dir poetry==1.5.1 && \
    poetry config --local virtualenvs.create false && \
    poetry install
COPY . .
RUN cp env.example .env
