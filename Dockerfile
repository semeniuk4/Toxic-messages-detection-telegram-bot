FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN [ "python3", "-c", "import nltk; nltk.download('stopwords', download_dir='/usr/local/nltk_data')" ]
RUN [ "python3", "-c", "import nltk; nltk.download('punkt', download_dir='/usr/local/nltk_data')" ]


COPY ./app /app/app
