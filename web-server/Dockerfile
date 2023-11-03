FROM python:3.11.6

WORKDIR /WEB-SERVER
COPY requirements.txt /WEB-SERVER/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt


COPY . /WEB-SERVER

CMD {"uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"}