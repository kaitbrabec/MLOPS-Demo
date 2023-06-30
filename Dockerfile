FROM python:3.9 as python-base
RUN mkdir nicegui_server
WORKDIR /nicegui_server
ENV PYTHONPATH "${PYTHONPATH}:/nicegui_server/nicegui_backend"
ENV PYTHONUNBUFFERED 1
COPY pyproject.toml poetry.lock /nicegui_server/
RUN pip3 install poetry
COPY . /nicegui_server/.
RUN poetry config virtualenvs.create false
RUN poetry install --verbose


CMD ["uvicorn", "nicegui_backend.server:app", "--host", "0.0.0.0", "--port", "8080"]
