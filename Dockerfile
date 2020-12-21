FROM python:3.8.5

ADD . /root
WORKDIR /root
RUN pip install -U -r requirements.txt

VOLUME /data_upload

CMD python dropbox_file_uploader.py 