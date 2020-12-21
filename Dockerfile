FROM python:3.8.5

ADD . /root
WORKDIR /root
RUN pip install -U -r requirements.txt

VOLUME /data_upload
ENV TOKEN=

ENTRYPOINT python -u sync_dropbox.py --token $TOKEN /data_upload
CMD FileBackup