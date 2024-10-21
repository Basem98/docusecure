FROM python:3.12

WORKDIR /

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

USER app

WORKDIR /app

COPY --chown=app:app ./app  .

EXPOSE 3000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]