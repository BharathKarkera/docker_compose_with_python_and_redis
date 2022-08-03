FROM python:latest
WORKDIR /my_code
COPY . /my_code
RUN pip install -r requirements.txt
CMD python app.py


