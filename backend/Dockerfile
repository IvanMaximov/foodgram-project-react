FROM python:3.7

WORKDIR /app

COPY requirement.txt .

RUN apt update && \
    apt upgrade -y && \
    apt -y install gcc && \
    python3 -m pip install --upgrade pip && \
    pip install -r requirement.txt --no-cache-dir

COPY . ./

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:5000"]