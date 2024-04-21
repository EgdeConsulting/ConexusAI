FROM python:3.12.2

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app","--reload", "--host", "0.0.0.0", "--port", "80"]
#CMD ["uvicorn", "app.main:app", "--reload,"]
#CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
