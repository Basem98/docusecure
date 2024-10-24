FROM python:3.12

WORKDIR /

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./app  .

EXPOSE 3001

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3001", "--reload"]