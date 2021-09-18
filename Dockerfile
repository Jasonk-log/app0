FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install requests

COPY . .

CMD [ "python", "./app1.py" ]
