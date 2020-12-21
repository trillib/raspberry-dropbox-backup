# Raspberry Pi Dropbox Backup

This repository provides a script where you can sync a local folder with a given dropbox folder. 
It's intended to be used on a Raspberry Pi which acts as a File Server and backs up a certain folder on Dropbox.
To get it running use the python script directly or build the container. The container is compatible with the ARM
Architecture from the Raspberry PI

## Getting started

Prerequisites:
* Create an application on the [Dropbox App Console](https://www.dropbox.com/developers/apps) and get an access token.
Be aware to set all the permissions and create the token again afterwards because it's not updating them if there's already
  an existing token.

Locally:
```
python sync_dropbox --token <ACCESS_TOKEN> <LOCAL_DIRECTORY> <DROPBOX_DIRECTORY> <TOKEN>
```

With docker:
```
docker build .
docker run -v <LOCAL_DIRECTORY>:/data_upload <IMAGE> <DROPBOX_FOLDER> <TOKEN>
```


## To be implemented
* Deletion of files
* Renaming of files