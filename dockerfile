FROM python:3.11

Env SDE="true"

ENV AMOUNT=""

ENV CURRENCY=""

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

ENTRYPOINT ["python", "-u", "dolarconverter/usconverter.py", "$AMOUNT", "$CURRENCY"]

