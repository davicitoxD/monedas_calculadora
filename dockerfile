FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

ENTRYPOINT ["python", "-u", "src/usconverter.py", "$AMOUNT", "$CURRENCY"]

# Define arguments as environment variables
ENV AMOUNT=""
ENV CURRENCY=""
