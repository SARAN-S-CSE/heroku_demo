FROM python:3.10.4
COPY ./requirements.txt /main/requirements.txt
WORKDIR /main
RUN pip install -r requirements.txt
COPY . /mian
CMD ["main.py"]