FROM python:3.9

WORKDIR /app

ENV APP_VENV_DIR="/app/.env"
RUN python -m venv "${APP_VENV_DIR}"
ENV PATH="${APP_VENV_DIR}/bin:${PATH}"

COPY app app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r app/requirements.txt

CMD ["python", "app/app.py"]

