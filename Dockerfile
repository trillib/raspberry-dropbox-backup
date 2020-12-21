FROM python:3.8.5

ADD . /root
WORKDIR /root
RUN pip install -U -r requirements.txt

VOLUME /data_upload

ENTRYPOINT ["python", "-u", "sync_dropbox.py", "/data_upload"]
CMD ["FileBackup", "Token"]