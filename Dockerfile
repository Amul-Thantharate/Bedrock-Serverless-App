FROM amuldark/custom-ubuntu:latest

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY .env /app/.env
COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
