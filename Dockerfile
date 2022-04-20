FROM Python:latest

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

CMD python src/__init__.py
