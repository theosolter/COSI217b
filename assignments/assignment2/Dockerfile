FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN python -m spacy download en_core_web_sm

ENV FLASK_APP flask_app.py

EXPOSE 5000

# Add volume to persist data in database
VOLUME /app/data

CMD ["flask", "run", "--host=0.0.0.0"]