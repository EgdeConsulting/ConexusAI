FROM python:3.12.2

WORKDIR /backend

COPY ./backend/requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
