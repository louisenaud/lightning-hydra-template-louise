FROM python:3.10-slim-buster

WORKDIR /docker

COPY requirements_old.txt requirements.txt

RUN pip3 install -r requirements_old.txt && rm -rf /root/.cache/pip

COPY . .

CMD [ "python3", "src/train.py" ]
